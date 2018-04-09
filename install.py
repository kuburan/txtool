#!/data/data/com.termux/files/usr/bin/python2

import sys, os

path = os.getcwd()
sys.path.append(path)
apt_folder = "/data/data/com.termux/files/usr/etc/apt"
bin = "/data/data/com.termux/files/usr/bin"
share = "/data/data/com.termux/files/usr/share"

if not os.path.isfile("%s/sources.list" % (apt_folder)):
    print "\n[x] sorry bos. txtool only available on termux.\n"
    sys.exit()

else:
    print "\n[*] installing txtool...\n"
    os.system("cd %s && rm -fr txtool" % (bin))
    os.system("cd %s && rm -fr txtool" % (share))
    os.system("cp txtool %s" % (bin))
    os.system("mkdir -p %s/txtool && cp -r core %s/txtool" %
             (share, share))
    os.system("cp -r module %s/txtool && cp -r other %s/txtool" %
             (share, share))
    os.system("apt-get install --assume-yes nmap php curl")
    os.system("pip2 install requests bs4")
    print "\n[*] Done !!! type command txtool to launch txtool\n"
