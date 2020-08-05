# Configures a SSH Client.

file_line { 'Turn off passwd auth':
  path => '/etc/.ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}