
import os, sys
print "\n            WELCOME\n                 IN\n      TOOLS Himel Gazi\n           CODE: BY Himel Gazi     FACEBOOK HACKING SYSTEM FAST CRACK \n      From Narsingdi [Bangladesh] \n"           
print '\x1b[1;33mAlready have the ID and password?'
print '\x1b[1;32mPlease Login '
import os, sys

def wa():
    os.system('xdg-open https://api.whatsapp.com/send?phone=8801627600547&text=Assalamualaikum')


def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)


user = raw_input('ID: ')
import getpass
sandi = raw_input('Password: ')
if sandi == 'handsome' and user == 'Himel':
    print 'You Have Login My System'
    sys.exit
else:
    print 'Login FAILED, Please contact me'
    wa()
    restart()
