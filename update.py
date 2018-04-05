#!/data/data/com.termux/files/usr/bin/python2

import os
PREFIX = '/data/data/com.termux/files/usr'
def x():
    os.system("git pull")
    os.system("cp txtool %s/bin" % (PREFIX))
    os.system("rm -fr %s/share/txtool/*" % (PREFIX))
    os.system("mkdir -p %s/share/txtool" % (PREFIX))
    os.system("cp -r {core,module,other} %s/share/txtool" % (PREFIX))

if os.path.isfile("%s/bin/git" % (PREFIX)):
    x()

else:
    print("\ninstalling git....")
    os.system("apt-get install --assume-yes git")
    x()
