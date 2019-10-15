# Nginx Open Source

[![v 1.16.1](https://img.shields.io/badge/v-1.16.1-green.svg)](http://nginx.org/en/CHANGES-1.16)

* [Build](#build)
  * [Vault](#vault)
  * [Check](#check)
  * [Playbook](#playbook)

## Build

### Vault

Create a secret for `sudo` password:

* `ansible-vault create secret`: Create a vault password
  * Add `ansible_become_pass: YOUR_SUDO_PASSWORD`
* `echo "YOUR_VOULT_PASSWORD" > vault.txt`

### Check

`ansible-playbook --check --vault-password-file=vault.txt $(cat /etc/issue | awk 'NR==1 {print tolower($1)}')-playbook.yaml`

### Playbook

`ansible-playbook --vault-password-file=vault.txt $(cat /etc/issue | awk 'NR==1 {print tolower($1)}')-playbook.yaml`
