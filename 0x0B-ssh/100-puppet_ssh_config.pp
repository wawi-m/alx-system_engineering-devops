#!/usr/bin/env bash
# change conf using puppet
file { '/etc/ssh/ssh_config':
  ensure => 'file',
  content => "\
PasswordAuthentication no
IdentityFile ~/.ssh/school
",
}
