txtool is made to help you for easly pentesting in termux,  
build on termux and only available for termux.  

Installation steps: 
===
* require python version 2.x  

```
$ git clone https://github.com/kuburan/txtool.git  
$ cd txtool  
$ apt install python2  
$ ./install.py 
$ txtool
```

How to contribute ?
===
if you are interesting with this project, you are welcome to open pull request
* fork this repository
* create new branch on your forked repository
* push your commit to new branch on your forked repository
* finally open new pull request

Know problem ?
===
* for ssh backdoor access, txtool used `paramiko` python library that required `PyNacl`
if you have an error installing PyNacl, follow my steps:
```
$ apt-get install --assume-yes libsodium libsodium-dev
$ SODIUM_INSTALL=system pip2 install pynacl
```
or you have another error, please submit a new issue.

# Screenshot  
![Screenshot](https://raw.githubusercontent.com/kuburan/txtool/master/screenshot/Screenshot_a.png)  
![Screenshot](https://raw.githubusercontent.com/kuburan/txtool/master/screenshot/Screenshot_b.png)  
![Screenshot](https://raw.githubusercontent.com/kuburan/txtool/master/screenshot/Screenshot_c.png)  
  
# Contact  
kuburan000@protonmail.ch  
