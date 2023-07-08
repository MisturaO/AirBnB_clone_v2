# sets up my web servers for the deployment of web_static

exec {'update':
  provider => shell,
  command  => 'sudo apt -y update',
  before   => Exec['install nginx'],
}

exec {'install nginx':
  provider => shell,
  command  => 'sudo apt -y install nginx',
  require  => Exec['update'],
}

file {'/data':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
}

file {'/data/web_static':
    ensure  => directory,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    require => File['/data'],
}
file {'/data/web_static/shared':
    ensure  => directory,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    require => File['/data/web_static'],
}
file {'/data/web_static/releases':
    ensure  => directory,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    require => File['/data/web_static'],
}
file {'/data/web_static/releases/test':
    ensure  => directory,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    require => File['/data/web_static/releases'],
}
file {'/data/web_static/releases/test/index.html':
    ensure  => file,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    content => 'Hello Web Static',
    require => File['/data/web_static/releases/test'],
}
file {'/data/web_static/current':
    ensure => link,
    target => '/data/web_static/releases/test',
    owner  => 'ubuntu',
    group  => 'ubuntu',
}
$add = "\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
exec{'location hbnb_static':
  provider => shell,
  command  => "sudo sed -i '/server_name _;/a ${add};' /etc/nginx/sites-available/default",
  require  => Exec['install nginx'],
}
# restart nginx after config  update
exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
  require  => Exec['location hbnb_static'],
}