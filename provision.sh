echo "Installing pip"
apt-get install -y python-pip

echo "Installing python requirements via pip"
pip install -r /vagrant/requirements.txt

echo "Setting executable permission on start script"
chmod +x /vagrant/start.sh




