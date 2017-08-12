### macOS Security

#### Basic recommendations

* I always install the latest updates for the macOS System software as soon as they are available, including new versions of the OS.


* I do not use Flash player.  I cannot caution you strongly enough against its use.

* I do not use Adobe Reader.  I cannot caution you strongly enough against its use.

* You must be **certain** that any app you do use can be trusted.  If you enter a username and password for a bad actor, you are probably *pwned*, and there is no reliable recovery from that save wiping the disk, reinstalling the OS and retrieving your data from offline storage.

* I do not have Sharing enabled, and do not login in remotely.  If you need such capabilities you should learn to `ssh`.
#### Antivirus

I do not have antivirus software running on my Mac.  

I have occasionally scanned with [ClamXav](https://www.clamxav.com) and not found anything.  I do not know of a virus for OS X, but one can pass on Windows viruses in emails or Word docs.  If you would like to check for this, ClamXav should detect it.

The basic problem with antivirus protection is that it cannot cope with new threats fast enough.  

Furthermore, Macs have not been targeted by virus writers, for reasons that are debated.
* [malwarebytes](https://blog.malwarebytes.com)

The history of threats on Mac is instructive, here is a write-up of [one](https://blog.malwarebytes.com/threat-analysis/mac-threat-analysis/).  

In this exploit, the download site for DVD-ripping software **HandBrake** was hacked.  For a period of four days, a version that installs [Proton.B](https://www.cybereason.com/labs-proton-b-what-this-mac-malware-actually-does/) was what you got with your download.  

The first thing the malware did was to ask for your password, so it could upgrade its priveleges.  The next thing it did was to steal your Keychain.

#### Passwords

* Low are held in the Keychain.

* Medium are held in an encrypted file which I decrypt for each use with a master password.  **Disk Utility** can do this for you.

Length and randomness are important, while a large character set is not so important.  [Here](https://www.troyhunt.com/passwords-evolved-authentication-guidance-for-the-modern-era/) is a good discussion of several password issues.  Requirements that encourage use of weak passwords (like resets every 3 months) are a bad idea.

* `cohacrtztnlkinlaiemilrbrhrvvwr`

using a utility that I wrote.

You can generate random passwords with the KeyChain Access utility.  [Here](http://osxdaily.com/2011/05/10/generate-random-passwords-command-line/) and [here](https://apple.stackexchange.com/questions/170453/access-keychain-access-password-generator-password-assistant-via-terminal-with) are other options.

A couple more ideas, from Terminal

```
> openssl rand -hex 20
c4ef62b60e7dc0e4117150dabf9b138e7b2da462
> openssl rand -base64 20
J93ov/tvvmRFalbw7XRpZBfOQz0=
>
```

and 

```
> printf "my passphrase" | md5
d2cb415e067c7b13409eeb425cae6418
> printf "my passphrase" | openssl dgst -sha256
2cec71ecf27a78e25ccbfdce41783760c2df45d8751c8a59c811a2005f1f05a7
>
```

The eternal question is how to backup such data securely, since the two requirements conflict.  I store my encrypted password file on Dropbox.  I also have backups stored on various hard drives, though these may not be completely up-to-date.

Someone I trust recommends [1Password](https://1password.com) (see [discussion](https://news.ycombinator.com/item?id=9728029)).

I use random text (basically, a password like the one above) for secret questions, though I did once give my mother's birth year as 1809.  Obviously, this needs to be saved securely so it can be copied and pasted.

For extra security, your everyday account used to surf the web should be a non-privileged user.

I used to write high security passwords (banking) down on a piece of paper.  Now I recommend that you set up a separate User for banking.  My Dropbox is only available from that account.

#### Actual Mac security threats.

It may be helpful to review recent actual security threats observed for macOS.

in progress