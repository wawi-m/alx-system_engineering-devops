#create killmenow

file { '/usr/local/bin/killmenow':
  ensure  => present,
  mode    => '755',  # Ensure executable permission
  content => '#!/bin/bash\nwhile true; do sleep 2; done\n',
}

# kill a process

exec{ 'kill_killmenow_process':
  command     => '/usr/bin/pkill -f killmenow',
  path        => ['/usr/bin', '/bin'],
  user        => 'root',
  refreshonly => true,
}
