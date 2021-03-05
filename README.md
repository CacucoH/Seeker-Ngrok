## Seeker + Ngrok: Specially for iSH

Hey Guys, the Seeker isnt my project: i just modified it with pyngrok. So, you dont need to start ngrok session - it will start automaticly! 
The link to the original project: https://github.com/thewhiteh4t/seeker

## Installation:
```
apk add bash
git clone https://github.com/CacucoH/Seeker-Ngrok
cd Seeker-Ngrok
bash install.sh


#If pip3 not installed automaticly install it
```
## Using:
Congradulations! You just installed the programm!
Now you can start it with 
```
python3 seeker.py -t manual
```
Have fun :)
## Bonus:
Now iSH doesnt have apk installed. If you dont have apk installed yet just type
```
wget -qO- http://dl-cdn.alpinelinux.org/alpine/v3.12/main/x86/apk-tools-static-2.10.5-r1.apk | tar -xz sbin/apk.static && ./sbin/apk.static add apk-tools && rm sbin/apk.static
```
