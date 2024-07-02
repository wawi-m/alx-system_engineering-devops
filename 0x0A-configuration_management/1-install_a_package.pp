# check for python instal

package{ 'python3':
  ensure => installed,
}

# check for pip3 instal

package{ 'python3-pip':
  ensure => installed,
}

# Install Flask v 2.1.0 using pip3

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

# Install werkzeug using pip3

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
