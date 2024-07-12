#!/usr/bin/env bash
# change conf using puppet

file { '~/.ssh/config':
  ensure => 'present',
}

file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => 'PasswordAuthentication yes',
  replace => 'True',
}

file_line { 'Declare identity file':
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => 'IdentityFile',
  ensure => 'present'
}
