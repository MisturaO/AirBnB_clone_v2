# sets up my web servers for the deployment of web_static

exec {'update':
  provider => shell,
  command  => 'sudo apt -y update',
  before   => Exec['install nginx']
}

exec {'install nginx':
  provider => shell,
  command  => 'sudo apt -y install nginx',
  require  => Exec['update']
}

file {'/data'
    enable => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
}

file {'/data/web_static'
    enable => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
}
file {'/data/web_static/shared'
    enable => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
}
file {'/data/web_static/releases'
    enable => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
}
file {'/data/web_static/releases/test'
    enable => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
}
file {'/data/web_static/releases/test/index.html'
    enable  => file,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    content => 'Hello Web Static'
}
file {'/data/web_static/current'
    enable => link,
    target => '/data/web_static/releases/test'
    owner  => 'ubuntu',
    group  => 'ubuntu',
}
add = "\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
exec{'location hbnb_static':
  provider => shell,
  command  => "sudo sed -i '/server_name _;/a ${add};' /etc/nginx/sites-available/default",
}
# restart nginx after config  update
exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}