# Nginx Open Source

[![v 1.16.1](https://img.shields.io/badge/v-1.16.1-green.svg)](http://nginx.org/en/CHANGES-1.16)

* Nginx custom modules
  * `lua-nginx-module`
  * `set-misc-nginx-module`
  * `ModSecurity-nginx`
  * `ngx-devel-kit`

* Resty libraries:
  * `lua-resty-core`
  * `lua-resty-lrucache`
  * `lua-resty-http`
  * `lua-resty-balancer`
  * `lua-resty-dns`
  * `lua-resty-cookie`
  * `lua-resty-lock`

* Lua libraries:
  * `cjson`

* `ModSecurity`

* `owasp-modsecurity-crs`

* [Build](#build)
  * [Ansible](#ansible)
    * [Vault](#vault)
    * [Check](#check)
    * [Playbook](#playbook)

## Build

### Ansible

Build using `ansible`.

#### Vault

Create a secret for `sudo` password:

* `ansible-vault create secret`: Create a vault password
  * Add `ansible_become_pass: YOUR_SUDO_PASSWORD`
* `echo "YOUR_VOULT_PASSWORD" > vault.txt`

#### Check

* Ubuntu:
  * `ansible-playbook --check --vault-password-file=vault.txt ubuntu-playbook.yaml`

#### Playbook

* Ubuntu:
  * `ansible-playbook --vault-password-file=vault.txt ubuntu-playbook.yaml`
