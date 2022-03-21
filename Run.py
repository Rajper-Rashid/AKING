#coding=utf-8
try:
    import os,sys,subprocess,requests
except ModuleNotFoundError:
    os.system('pip install requests futures bs4')
    os.system('python Run.py')
current_os=subprocess.check_output('uname -om',shell=True)
if 'aarch64' in str(current_os):
    if not os.path.isfile('a64'):
        os.system('curl -L https://github.com/AKING110/AKING/Aking64')
        os.system('chmod 777 Aking64')
        os.system('./Aking64')
    else:
        os.system('./Aking64')
elif 'arm' in str(current_os):
    if not os.path.isfile('a32'):
        os.system('curl -L https://github.com/AKING110/AKING/Aking32')
        os.system('chmod 777 Aking32')
        os.system('./Aking32')
    else:
        os.system('./Aking32')
else:
    print('\n  Your Device Is Not Support Please Change Other Device.')
    print('  Owner whatsapp: +923237528063\n\n')
    os.sys.exit()