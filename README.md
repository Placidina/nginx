# Nginx Open Source

[![v 1.16.1](https://img.shields.io/badge/v-1.16.1-green.svg)](http://nginx.org/en/CHANGES-1.16)

* [Build](#build)
  * [Ansible](#ansible)
    * [Vault](#vault)
    * [Check](#check)
    * [Playbook](#playbook)
  * [Docker](#docker)

## Build

### Ansible

Build using `ansible`.

#### Vault

Create a secret for `sudo` password:

* `ansible-vault create secret`: Create a vault password
  * Add `ansible_become_pass: YOUR_SUDO_PASSWORD`
* `echo "YOUR_VOULT_PASSWORD" > vault.txt`

#### Check

Replace `EXAMPLE`:

`ansible-playbook --check --vault-password-file=vault.txt EXAMPLE-playbook.yaml`

#### Playbook

Replace `EXAMPLE`:

`ansible-playbook --vault-password-file=vault.txt EXAMPLE-playbook.yaml`

### Docker

Build using `docker`.

`docker build -t placidina/nginx:1.6.1 .`
