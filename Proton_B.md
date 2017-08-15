#### Proton.B

* disovered 2017
* backdoor
* steals credentials (e.g. Safari passwords)
* C&C servers

[analysis](https://www.cybereason.com/labs-proton-b-what-this-mac-malware-actually-does/)

files and directories:

```
~/Library/VideoFrameworks
~/Library/RenderFiles/activity_agent.app
~/Library/LaunchAgents/fr.handbrake.actibity_agent.plist
```

The download server for the popular Handbrake app was hacked for 5 days (May 2-6).  Downloading Handbrake got you an infection with Proton.B.

[link](https://blog.malwarebytes.com/threat-analysis/mac-threat-analysis/2017/05/handbrake-hacked-to-drop-new-variant-of-proton-malware/)