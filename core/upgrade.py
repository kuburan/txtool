#!/data/data/com.termux/files/usr/bin/python2

import os
module_dir = '/data/data/com.termux/files/usr/share/txtool/module'
core_dir = '/data/data/com.termux/files/usr/share/txtool/core'
os.system("cd %s && rm -f fungsi.py" % (core_dir))
os.system("cd %s && wget https://raw.githubusercontent.com/kuburan/txtool/master/core/fungsi.py" % (core_dir))
os.system("cd %s && rm -f module1.py module9.py" % (module_dir))
os.system("cd %s && wget https://raw.githubusercontent.com/kuburan/txtool/master/module/module1.py" % (module_dir))
os.system("cd %s && wget https://raw.githubusercontent.com/kuburan/txtool/master/module/module9.py" % (module_dir))
os.system("rm -f CHANGELOG && wget https://raw.githubusercontent.com/kuburan/txtool/master/CHANGELOG")
os.system("cd %s && rm -f version.txt" % (core_dir))
os.system("cd %s && wget https://raw.githubusercontent.com/kuburan/txtool/master/core/version.txt" % (core_dir))
