# Redo the task #0 but by using Puppet:

exec {'update':
    command => 'apt update',
    path    => ['/usr/bin', '/usr/sbin'],
}

exec {'install nginx':
    command => 'apt install -y nginx',
    path    => ['/usr/bin', '/usr/sbin'],
}

service {'nginx':
    ensure  => 'running',
    enabled => true,
}

file {'/data/web_static/releases/test/':
    ensure  => 'directory',
    recurse => true,
}

file {'/data/web_static/releases/test/index.html':
    ensure  => 'file',
    content => 'Hello world!',
}

file {'/data/web_static/shared/':
    ensure  => 'directory',
    recurse => true,
}

exec {'symlink current':
    command => 'ln -sfn /data/web_static/releases/test/ /data/web_static/current',
    path    => ['/usr/bin', '/usr/sbin'],
}

exec {'change ownership':
    command => 'sudo chown -R ubuntu:ubuntu /data/',
    path    => ['/usr/bin', '/usr/sbin'],
}

exec {'configure nginx':
    command => "sed -i '/pass PHP/i \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default",
    path    => ['/usr/bin', '/usr/sbin'],
}

exec {'restart nginx':
    command => 'sudo service nginx restart',
    path    => ['/usr/bin', '/usr/sbin'],
}
