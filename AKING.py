import os, platform, time
print('\n\x1b[1;37m Checking Update...');time.sleep(0.5)
def Update():
    exit('\033[1;31m(×) Commands On Update Please Wait For Update ❤ ')
def Run():
        bit = platform.architecture()[0]
        if bit == '64bit':
            print("\x1b[1;92m Congratulations ! Your Device Support this Tools")
            os.system('xdg-open https://facebook.com/groups/351076900316263/')
            from AKING import login
            login()
        elif bit == '32bit':
            print("\n\x1b[1;92m Congratulations ! Your Device Support this Tools")
            os.system('xdg-open https://facebook.com/groups/351076900316263/')
            from AKING32 import login
            login()
        else:
            exit('\033[1;31m[×] Connection Error')
Run()
