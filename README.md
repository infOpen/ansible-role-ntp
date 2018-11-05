# ntp

[![Build Status](https://travis-ci.org/infOpen/ansible-role-ntp.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-ntp)

Install ntp package.

## Requirements

This role requires Ansible 2.4 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- CentOS 7
- Debian Jessie
- Debian Stretch
- Ubuntu Xenial
- Ubuntu Bionic

and use:
- Ansible 2.4.x
- Ansible 2.5.x
- Ansible 2.6.x
- Ansible 2.7.x

### Running tests

#### Using Docker driver

```
$ tox
```

You can also configure molecule options and molecule command using environment variables:
* `MOLECULE_OPTIONS` Default: "--debug"
* `MOLECULE_COMMAND` Default: "test"

```
$ MOLECULE_OPTIONS='' MOLECULE_COMMAND=converge tox
```

## Role Variables

### Default role variables

``` yaml
# Package variables
#------------------
ntp_package_state: 'present'


# Config file variables
#----------------------
ntp_config_file_dest: '/etc/ntp.conf'
ntp_config_file_owner: 'root'
ntp_config_file_group: 'root'
ntp_config_file_mode: '0644'


# Service variables
#------------------
ntp_service_state: 'started'
ntp_service_enabled: True


# Common commands
#----------------
ntp_peer: []
ntp_broadcast: []
ntp_manycastclient: []
ntp_server:
  - '0.ubuntu.pool.ntp.org'
  - '1.ubuntu.pool.ntp.org'
ntp_restrict:
  - '-4 default kod notrap nomodify nopeer noquery'
  - '-6 default kod notrap nomodify nopeer noquery'
  - '127.0.0.1'
  - '::1'


# Auxiliary Commands
#-------------------
ntp_broadcastclient: []
ntp_manycastserver: []
ntp_multicastclient: []


# Authentication Commands
#------------------------
ntp_autokey: False
ntp_revoke: False


# Miscellaneous Options
#----------------------

# The log file (False: syslog)
ntp_logfile: False

# The drift file
ntp_driftfile: '/var/lib/ntp/ntp.drift'

# Features management. If empty, default feature status is used
ntp_enabled_feature: []
ntp_disabled_feature: []

# Include a file
ntp_includefile: False

# Interface rules
ntp_interface_drop: []
ntp_interface_ignore:
  - 'wildcard'
ntp_interface_listen:
  - "{{ ansible_default_ipv4.address }}"
  - '127.0.0.1'
  - '::1'
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infOpen.ntp }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
