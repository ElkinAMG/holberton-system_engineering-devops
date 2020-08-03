# Kills a process

exec { 'kill_process':
  command => 'pkill -f ./killmenow',
}