##################################################
# Workbench Settings
##################################################
Vagrant.require_version ">= 1.7.3"

PROJECT_ENV = File.basename(Dir.getwd)

if File.exist?('../Vagrantfile')
  WORKBENCH_HOST = "workbench"
  WORKBENCH_VAGRANTFILE = "../Vagrantfile"
else
  WORKBENCH_HOST = "dockerhost"
  WORKBENCH_VAGRANTFILE = __FILE__
end

Vagrant.configure("2") do |config|

  ##################################################
  # Launch dev container
  # - vagrant up slacker
  ##################################################
  config.vm.define "slacker", autostart: true do |lucee|
    lucee.vm.provider "docker" do |docker|
      docker.name = PROJECT_ENV
      docker.build_dir = "."
      docker.env = {
        VIRTUAL_HOST: PROJECT_ENV + ".*"
      }
      # docker.volumes = [
      #   "/vagrant/" + PROJECT_ENV + "code:/app"
      # ]
      docker.vagrant_machine = WORKBENCH_HOST
      docker.vagrant_vagrantfile = WORKBENCH_VAGRANTFILE
      docker.force_host_vm = true
    end
    puts '############################################################'
    puts '# ' + PROJECT_ENV.upcase
    puts '#  - hosted at: http://' + PROJECT_ENV + '.dev'
    puts '############################################################'
  end

  ##################################################
  # Solo Docker Host; 
  #   fallback for missing parent boot2docker env
  ##################################################
  config.vm.define "dockerhost", autostart: false do |dh|
    dh.vm.box = "dduportal/boot2docker"
    dh.vm.network "private_network", ip: "192.168.56.100"
    dh.vm.synced_folder ".", "/vagrant/" + PROJECT_ENV, type: "virtualbox"

    dh.vm.provider "virtualbox" do |vb|
      vb.memory = 2048
      vb.customize ["modifyvm", :id, "--nictype2", "virtio"]
    end

    puts '############################################################'
    puts '#  WARNING: BACKUP HOST... http://192.168.56.100'
    puts '# '
    puts '#  Could not find Workbench Boot2Docker. Consider Setting'
    puts '#  up the complete development environment:'
    puts '#    https://github.com/Daemonite/workbench'
    puts '############################################################'
  end

# /config
end
