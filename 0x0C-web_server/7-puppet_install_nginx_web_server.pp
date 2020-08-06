# Installs NGINX and configures it.

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => 'Holberton School',
}

file_line { 'Redirection':
  path  => '/etc/nginx/sites-available/default',
  after => 'server_name _;',
  line  => 'location /redirect_me {return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;}'
}

service { 'nginx':
  ensure => running,
  require => Package['nginx'],
}