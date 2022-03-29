import os, platform

try:
   import requests

except:
   os.system('pip2 install requests')

import requests

bit = platform.architecture()[0]
if bit == '64bit':
    from Aking import readline___Public_Xml
    readline___Public_Xml()
elif bit == '32bit':
    print('YOUR DEVICE IS NOT SUPPORTED BRO')
