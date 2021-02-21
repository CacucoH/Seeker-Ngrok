echo '[i] Updating...'
apk update > install.log
echo
echo '[i] Installing Dependencies...'
echo '    Installing Python3'
apk add python3 setuptools &>> install.log
echo '    Installing PHP'
apk add php &>> install.log
echo '    Installing SSH'
apk add openssh &>> install.log
echo '    Installing Requests'
pip3 install requests &>> install.log
echo
echo '[i] Setting Permissions...'
chmod 777 template/nearyou/php/info.txt
chmod 777 template/nearyou/php/result.txt
echo
echo '[i] Succesfully installed!'
