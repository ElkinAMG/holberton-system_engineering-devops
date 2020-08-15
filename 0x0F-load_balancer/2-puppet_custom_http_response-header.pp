# Installs NGINX and configures it.

exec { "NGINX":
  command => "sudo apt-get -y update;
  	     sudo apt-get -y upgrade;
	     sudo apt-get -y install nginx;
	     sudo echo \"Holberton School\" > /var/www/html/index.html;
	     sudo sed -i \"11i \\\tadd_header X-Served-By \$hostname;\n\" /etc/nginx/nginx.conf;
	     sudo service nginx start;",
}