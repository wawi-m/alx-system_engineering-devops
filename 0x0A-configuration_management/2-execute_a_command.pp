# executes kill command

exec{ 'pkill_killmenow_process':
  command     => '/usr/bin/pkill -f killmenow',
  path        => ['/usr/bin', '/bin'],
}
