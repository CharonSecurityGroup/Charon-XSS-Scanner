
'''
#####################################################################################
# About :                                                                           #
#                                                                                   #
# Programmer: Ch4120n                                                               #
# Phone Number: +98 9304113043                                                      #
#                                                                                   #
# Copyright :                                                                       #
#                                                                                   #
# Charon PWNXSS (C) <2023> <Charon Security Agency>                                 #
# This Program Is Free Software: You Can Redistribute It                            #
# It Under The Terms Of The  `Charon General Black License` As Published By         #
# The Black Hacking Software Foundation , Either Version 1 Of The License.          #
# This Program Is Distributed In The Hope That It Will Be Useful,                   #
# But Without Any Warranty .  See The                                               #
# `Charon General Black License` For More Details.                                  #
# You Should Have Received A Copy Of The  `Charon General Black License`            #
# Along With This Program. If Not, See <http://charonsecurityagency.github.io/cgbl> #
#                                                                                   #
#####################################################################################

'''

import requests, json, random
##### Warna ####### 
N = '\033[0m'
W = '\033[1;37m' 
B = '\033[1;34m' 
M = '\033[1;35m' 
R = '\033[1;31m' 
G = '\033[1;32m' 
Y = '\033[1;33m' 
C = '\033[1;36m'

##### Styling ######
underline = "\033[4m"
##### Default ######
agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'} 
line="—————————————————" 
#####################
def session(proxies,headers,cookie):
	r=requests.Session()
	r.proxies=proxies
	r.headers=headers
	r.cookies.update(json.loads(cookie))
	return r

def ART_RANDOM():
	a1 = rf'''

 ██████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ███╗   ██╗    ██╗  ██╗███████╗███████╗ ██████╗ █████╗ ███╗   ██╗
██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗████╗  ██║    ╚██╗██╔╝██╔════╝██╔════╝██╔════╝██╔══██╗████╗  ██║
██║     ███████║███████║██████╔╝██║   ██║██╔██╗ ██║     ╚███╔╝ ███████╗███████╗██║     ███████║██╔██╗ ██║
██║     ██╔══██║██╔══██║██╔══██╗██║   ██║██║╚██╗██║     ██╔██╗ ╚════██║╚════██║██║     ██╔══██║██║╚██╗██║
╚██████╗██║  ██║██║  ██║██║  ██║╚██████╔╝██║ ╚████║    ██╔╝ ██╗███████║███████║╚██████╗██║  ██║██║ ╚████║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝

{' '*82}{'_'*25}
{' '*80}     (Version 1.0) Final
{' '*80}     <Powered By Ch4120N>

'''
	a2 = rf'''

 ▄▄·  ▄ .▄ ▄▄▄· ▄▄▄         ▐ ▄     ▐▄• ▄ .▄▄ · .▄▄ ·  ▄▄·  ▄▄▄·  ▐ ▄ 
▐█ ▌▪██▪▐█▐█ ▀█ ▀▄ █·▪     •█▌▐█     █▌█▌▪▐█ ▀. ▐█ ▀. ▐█ ▌▪▐█ ▀█ •█▌▐█
██ ▄▄██▀▐█▄█▀▀█ ▐▀▀▄  ▄█▀▄ ▐█▐▐▌     ·██· ▄▀▀▀█▄▄▀▀▀█▄██ ▄▄▄█▀▀█ ▐█▐▐▌
▐███▌██▌▐▀▐█ ▪▐▌▐█•█▌▐█▌.▐▌██▐█▌    ▪▐█·█▌▐█▄▪▐█▐█▄▪▐█▐███▌▐█ ▪▐▌██▐█▌
·▀▀▀ ▀▀▀ · ▀  ▀ .▀  ▀ ▀█▄▀▪▀▀ █▪    •▀▀ ▀▀ ▀▀▀▀  ▀▀▀▀ ·▀▀▀  ▀  ▀ ▀▀ █▪

{' '*52}{'_'*25}
{' '*50}     (Version 1.0) Final
{' '*50}     <Powered By Ch4120N>
'''
	a3 = rf'''

   _____ _                            __   __ _____ _____  _____          _   _ 
  / ____| |                           \ \ / // ____/ ____|/ ____|   /\   | \ | |
 | |    | |__   __ _ _ __ ___  _ __    \ V /| (___| (___ | |       /  \  |  \| |
 | |    | '_ \ / _` | '__/ _ \| '_ \    > <  \___ \\___ \| |      / /\ \ | . ` |
 | |____| | | | (_| | | | (_) | | | |  / . \ ____) |___) | |____ / ____ \| |\  |
  \_____|_| |_|\__,_|_|  \___/|_| |_| /_/ \_\_____/_____/ \_____/_/    \_\_| \_|
                                                                                
{' '*52}{'_'*25}
{' '*50}     (Version 1.0) Final
{' '*50}     <Powered By Ch4120N>
'''
	a4 = rf'''
                   /^\
          _.-`:   /   \   :'-._
        ,`    :  |     |  :    '.
      ,`       \,|     |,/       '.
     /           `-...-`           \
    :              .'.              :
    |    Charon   . ' .   XSSCAN    |{' '*10}    (Version 1.0) Final
    |             ' . '             |{' '*10}    <Created By Ch4120N>
    :              '.'              :
     \           ,-"""-,           /
      `.       /'|     |'\       ,'
        `._   ;  |     |  ;   _,'
           `-.:  |     |  :,-'
                 |     |
                 |     |
                 |     |
                 |     |
                 |     |
                 \     /
                  \   /
                   \_/

'''
	a5 = rf'''

 ██████ ██   ██  █████  ██████   ██████  ███    ██     ██   ██ ███████ ███████  ██████  █████  ███    ██ 
██      ██   ██ ██   ██ ██   ██ ██    ██ ████   ██      ██ ██  ██      ██      ██      ██   ██ ████   ██ 
██      ███████ ███████ ██████  ██    ██ ██ ██  ██       ███   ███████ ███████ ██      ███████ ██ ██  ██ 
██      ██   ██ ██   ██ ██   ██ ██    ██ ██  ██ ██      ██ ██       ██      ██ ██      ██   ██ ██  ██ ██ 
 ██████ ██   ██ ██   ██ ██   ██  ██████  ██   ████     ██   ██ ███████ ███████  ██████ ██   ██ ██   ████ 

{' '*82}{'_'*25}
{' '*80}     (Version 1.0) Final
{' '*80}     <Powered By Ch4120N>
'''
	arts = [a1, a2, a3, a4, a5]
	return random.choice(arts)

logo = ART_RANDOM()