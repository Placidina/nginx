#!/usr/bin/env python3

import boto3
import yaml
import sys
import argparse
import re
import os


def parse_args():
    parser = argparse.ArgumentParser(description='Nginx AWS Sync - AWS instances to upstream servers')
    parser.add_argument('-c', '--config', dest='config', default='config.yaml', help='Configurations file')
    return parser.parse_args()


def config(config_path):
    with open(config_path, 'r') as conf:
        try:
            return yaml.safe_load(conf)
        except yaml.YAMLError as e:
            sys.exit(e)


def client(credentials):
    return boto3.client(
        'ec2',
        region_name=credentials['region'],
        aws_access_key_id=credentials['accessKey'],
        aws_secret_access_key=credentials['secretKey']
    )


def update(upstream, ips):
    global reload

    servers = []
    lines = None
    path = '{}/{}.conf'.format(upstream['path'], upstream['name'])

    with open(path, 'r') as conf:
        lines = conf.readlines()
        conf.close()

    with open(path, 'w') as conf:
        for line in lines:
            server = re.match(r'server\s(\d{1,3}\.\d{1,3}\.\d{1,9}\.\d{1,9}):\d{1,6};', line.strip())

            if server:
                if server[1] not in ips:
                    reload = True
                    continue

                servers.append(server[1])

            conf.write(line)

        conf.truncate()
        conf.close()

    with open(path, 'a') as conf:
        for ip in ips:
            if ip not in servers:
                reload = True
                conf.write('server {}:{};\n'.format(ip, upstream['port']))

        conf.truncate()
        conf.close()


if __name__ == "__main__":
    args = vars(parse_args())
    conf = config(args['config'])
    ec2 = client(conf['credentials'])

    reload = False

    for ups in conf['upstream']:
        response = ec2.describe_instances(
            Filters=[{'Name': 'tag:upstream', 'Values': [ups['name']]},
                     {'Name': 'instance-state-name', 'Values': ['running']}])

        ips = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                ips.append(instance['PrivateIpAddress'])

        update(ups, ips)

    if reload:
        os.system("/etc/init.d/nginx reload")
