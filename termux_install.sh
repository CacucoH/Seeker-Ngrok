echo '[!] Updating...'
apk add update > install.log
echo
echo '[!] Installing Dependencies...'
echo '    Python3'
apk add install python &>> install.log
echo '    PHP'
apk add install php &>> install.log
echo '    ssh'
apt-get -y install openssh &>> install.log
echo '    Requests'
pip3 install requests &>> install.log
echo
echo '[!] Setting Permissions...'

chmod 777 template/nearyou/php/result.txt
echo
echo '[!] Installed.'