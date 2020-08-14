# Installs NGINX and configures it.

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => 'Holberton School',
}

file_line { 'HEADER':
  path  => '/etc/nginx/sites-available/default',
  after => 'server_name _;',
  line  => 'add_header X-Served-By $hostname'
}

service { 'nginx':
  ensure => running,
  require => Package['nginx'],
}