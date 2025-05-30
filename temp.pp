exec {'configure nginx':
    command => 'sed -i \'/pass PHP/i\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\' /etc/nginx/sites-available/default',
    path    => ['/usr/bin', '/usr/sbin'],
}
