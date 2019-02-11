# -*- coding:utf8 -*-

#def test_ruby_is_installed(host):
#    assert host.exists("ruby")
#    assert "2.5.3" in host.run("ruby -v").stdout
#
#def test_passenger_is_installed(host):
#    assert host.exists("passenger")
#    assert "5.2.2" in host.run("passenger -v").stdout

def test_passenger_is_listen(host):
    assert host.socket("tcp://0.0.0.0:3000").is_listening
