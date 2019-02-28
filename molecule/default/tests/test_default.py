import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ruby_is_installed(host):
    assert 0 == host.run('bash -lc "type ruby"').rc


def test_passenger_is_installed(host):
    assert 0 == host.run('bash -lc "type passenger"').rc


def test_passenger_is_listen(host):
    assert host.socket("tcp://0.0.0.0:3000").is_listening
