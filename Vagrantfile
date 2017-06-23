# -*- mode: ruby -*-
# vi: set ft=ruby :
# See https://github.com/discourse/discourse/blob/master/docs/VAGRANT.md
#
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box= "ubuntu/trusty64"

  config.vm.network :private_network, ip: "192.168.33.40"  
  
  config.vm.provider :virtualbox do |v|
    v.customize ["modifyvm", :id, "--memory", "1024"]
    v.customize ["modifyvm", :id, "--cpus", "2"]
    v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
    v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    v.customize ["modifyvm", :id, "--nictype1", "virtio"]
  end

  config.vm.synced_folder ".", "/home/vagrant/exportDDB",
    mount_options: ["dmode=775,fmode=664"]
  
  config.vm.provision "file", source: "config/.aws/credentials", destination: "~/.aws/credentials"

  config.vm.provision "shell",
    inline: "sudo apt-get update"
    
  config.vm.provision "docker" do |d|
    d.pull_images "python:2"
  end 

  config.vm.provision "shell",
    inline: "apt-get install -y tofrodos wget zip python-pip"
  
   config.vm.provision "shell",
    inline: "sudo pip install awscli boto3"
    
  config.vm.provision "shell",
    inline: "wget https://github.com/docker/compose/releases/download/1.12.0/docker-compose-Linux-x86_64"
    
  config.vm.provision "shell",
    inline: "sudo mv docker-compose-Linux-x86_64 /usr/local/bin/docker-compose"
    
  config.vm.provision "shell",
    inline: "sudo chmod +x /usr/local/bin/docker-compose"  
  
end