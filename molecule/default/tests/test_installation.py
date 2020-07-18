"""
Role tests
"""

import os
import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages(host):
    """
    Test packages installed
    """

    assert host.package('ntp').is_installed


def test_user(host):
    """
    Test service user
    """

    service_user = host.user('ntp')

    assert service_user.exists
    assert service_user.group == 'ntp'

    if host.system_info.distribution == 'centos':
        assert service_user.home == '/etc/ntp'
        assert service_user.shell == '/sbin/nologin'
    elif host.system_info.codename == 'stretch':
        assert service_user.home == '/home/ntp'
        assert service_user.shell == '/bin/false'
    else:
        assert service_user.home == '/nonexistent'
        assert service_user.shell == '/usr/sbin/nologin'


def test_service(host):
    """
    Test service state
    """

    _service_name = 'ntp'

    if host.system_info.distribution == 'centos':
        _service_name = 'ntpd'

    service = host.service(_service_name)

    assert service.is_enabled
    assert service.is_running


def test_process(host):
    """
    Test process state
    """

    # Sometimes, two processes start on the service activate
    # Only one process running after container restart
    assert len(host.process.filter(comm='ntpd')) in (1, 2)


@pytest.mark.parametrize('item_type,path,user,group,mode', [
    ('directory', '/var/lib/ntp', 'ntp', 'ntp', 0o755),
    ('directory', '/var/log/ntpstats', 'ntp', 'ntp', 0o755),
    ('file', '/etc/ntp.conf', 'root', 'root', 0o644),
])
def test_paths_properties(host, item_type, path, user, group, mode):
    """
    Test files and folders properties
    """

    current_item = host.file(path)

    assert current_item.exists
    assert current_item.user == user
    assert current_item.group == group
    assert current_item.mode == mode

    if item_type == 'file':
        assert current_item.is_file
    elif item_type == 'directory':
        assert current_item.is_directory
