ntp
===

[![Build Status](https://travis-ci.org/infOpen/ansible-role-ntp.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-ntp)

Install ntp package.

Requirements
------------

This role requires Ansible 1.4 or higher, and platform requirements are listed
in the metadata file.

Role Variables
--------------

Follow the possible variables with their default values

    # Package variables
    #------------------
    ntp_package_state  : present


    # Service variables
    #------------------
    ntp_service_state   : started
    ntp_service_enabled : True


    # Common commands
    #----------------
    ntp_peer           : []
    ntp_broadcast      : []
    ntp_manycastclient : []
    ntp_server :
      - 0.ubuntu.pool.ntp.org
      - 1.ubuntu.pool.ntp.org
    ntp_restrict :
      - "-4 default kod notrap nomodify nopeer noquery"
      - "-6 default kod notrap nomodify nopeer noquery"
      - "127.0.0.1"
      - "::1"


    # Auxiliary Commands
    #-------------------
    ntp_broadcastclient : []
    ntp_manycastserver  : []
    ntp_multicastclient : []


    # Authentication Commands
    #------------------------
    ntp_autokey : False
    ntp_revoke  : False


    # Miscellaneous Options
    #----------------------

    # The log file (False : syslog)
    ntp_logfile : False

    # The drift file
    ntp_driftfile : /var/lib/ntp/ntp.drift

    # Features management. If empty, default feature status is used
    ntp_enabled_feature  : []
    ntp_disabled_feature : []

    # Include a file
    ntp_includefile : False

    # Interface rules
    ntp_interface_drop   : []
    ntp_interface_ignore :
      - wildcard
    ntp_interface_listen :
      - "{{ ansible_default_ipv4.address }}"
      - "127.0.0.1"
      - "::1"

Specific OS family vars :

    # Debian
    ntp_packages :
      - ntp
    ntp_service_name: ntp

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: infopen.ntp }

License
-------

MIT

Author Information
------------------

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
