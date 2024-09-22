# This Puppet manifest fixes the Apache 500 error by installing missing packages and restarting Apache.

package { 'php5':
  ensure => installed,
}

service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => Package['php5'],
}

