Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provision "shell", path: "install-api-env.sh"
  config.vm.network "public_network",
    use_dhcp_assigned_default_route: true
end
