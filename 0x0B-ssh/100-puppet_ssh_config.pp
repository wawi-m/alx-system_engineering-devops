#!/usr/bin/env bash
# change conf using puppet
file { '/etc/ssh/ssh_config':
  ensure  => 'file',
  content => "\
PasswordAuthentication no
IdentityFile ~/.ssh/school
",
}
file_line { 'Turn off passwd auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
file_line { 'Declare identity file':
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}
