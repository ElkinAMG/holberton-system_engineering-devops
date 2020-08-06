# Installs NGINX and configures it.

package { 'nginx':}

file { '/var/www/html/index.html':
  content => 'Holberton School',
}

file_line { 'Redirection':
  path  => '/etc/nginx/sites-available/default',
  line  => '\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}'
  after => 'server_name _;',
}
