# kill a process

exec{ 'kill_killmenow_process':
  command     => '/usr/bin/pkill -f killmenow',
  path        => ['/usr/bin', '/bin'],
  user        => 'root',
  refreshonly => true,
  subscribe   => File['~/alx-system_engineering-devops/0x0A-configuration_management/killmenow'],
}
