#!/data/data/com.termux/files/usr/bin/python2

import sys, os, subprocess, time
from urllib import urlopen

txtool_dir = "/data/data/com.termux/files/home/.txtool"
def get_version():
    define_version = open("/data/data/com.termux/files/usr/share/txtool/core/version.txt", "r").read().rstrip()
    return define_version

def check_version():
    url = ("https://raw.githubusercontent.com/kuburan/txtool/master/core/version.txt")
    check = urlopen(url).read().rstrip().decode('utf-8')
    f = open(txtool_dir + "/version.lock", "w")
    f.write(check)
    f.close()

def main():
    check_version()
    core = "/data/data/com.termux/files/usr/share/txtool/core"
    version = get_version()
    compare = open(txtool_dir + "/version.lock", "r").read().rstrip()
    if version in compare:
        print("\n[*] txtool is up to date.\n")
        os.system("rm -f %s/version.lock" % (txtool_dir))
        sys.exit()

    if not version in compare:
        print("\n[*] it seems the owner make some commit on master branch.")
        time.sleep(2)
        print("[*] txtool will be upgrade, plese wait a moment...")
        time.sleep(2)
        os.system("cd %s && rm -f upgrade.py" % (core))
        os.system("cd %s && wget https://raw.githubusercontent.com/kuburan/txtool/master/core/upgrade.py" % (core))
        subprocess.Popen("python2 /data/data/com.termux/files/usr/share/txtool/core/upgrade.py",
                          stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True).wait()
        print("[*] txtool has been updated to %s" % (compare))
        os.system("rm -f %s/version.lock" % (txtool_dir))
        sys.exit()

if __name__=='__main__':
    try:
        main()

    except(KeyboardInterrupt):
        print("\n[x] CTRL+C Detected, force program to stop !\n")
        sys.exit()
