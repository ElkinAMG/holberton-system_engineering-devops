# Installs NGINX and configures it.

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => 'Holberton School',
}

file_line { 'HEADER':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}

service { 'nginx':
  ensure => running,
  require => Package['nginx'],
}