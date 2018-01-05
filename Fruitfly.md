#### Fruitfly malware

* disovered Jan 2017
* backdoor
* captures screenshots, keystrokes, webcam
* allows file writes, data exfiltration etc.
* C&C servers

[patched](http://appleinsider.com/articles/17/01/18/fruitfly-malware-patched-by-apple-relies-on-ancient-mac-system-calls)

discovered by:  [Patrick Wardle](https://blog.malwarebytes.com/threat-analysis/2017/01/new-mac-backdoor-using-antiquated-code/)

OSX.Backdoor.Quimitchin

consists of two files:

```
~/.client
SHA256: ce07d208a2d89b4e0134f5282d9df580960d5c81412965a6d1a0786b27e7f044
 
~/Library/LaunchAgents/com.client.client.plist
SHA256: 83b712ec6b0b2d093d75c4553c66b95a3d1a1ca43e01c5e47aae49effce31ee3
```

other info:

* [link1](https://arstechnica.com/information-technology/2017/07/perverse-malware-infecting-hundreds-of-macs-remained-undetected-for-years/)

* [link2](http://www.zdnet.com/article/new-analysis-fruitfly-mac-malwware-almost-undetectable-backdoor/)

