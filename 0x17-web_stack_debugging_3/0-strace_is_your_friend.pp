# This Puppet manifest installs PHP and restarts Apache
package { 'php5':
  ensure => installed,
}

service { 'apache2':
  ensure => running,
  enable => true,
  subscribe => Package['php5'],
}

