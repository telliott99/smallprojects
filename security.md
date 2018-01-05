### macOS Security

#### Basic recommendations

* The very best security recommendation I can make is that you should be prepared at any time to wipe the disk, reinstall macOS and retrieve your data from *offline* storage.

* I always install updates for the macOS System software as soon as they are available, including upgrades to new versions of the OS.

* I do not use Flash player.  I cannot caution you strongly enough against its use.

* I do not use Adobe Reader.  I cannot caution you strongly enough against its use.

* You must be certain that any app you do use can be trusted.  If you enter a username and password for a bad actor, you are probably *pwned*, and **there is no reliable recovery from that save following the first option above**.* I use and highly recommend [LittleSnitch](https://www.obdev.at/products/littlesnitch/index.html), which monitors network connections.  I am careful not to allow connections that I don't know the reason for.* I am also currently evaluating [BlockBlock](https://objective-see.com/products/blockblock.html) from Objective-See, and they have a number of other innovative products.  

(Update:  I stopped using BlockBlock because it bricks macOS updates, and I keep forgetting to turn it off before starting an update).

* I do not have Sharing enabled, and do not login in remotely.  If you need such capabilities you should learn to generate Public/Private key pairs and use `ssh`.

* I do not use Word, Powerpoint or Excel.  If you do, make sure Macros are disabled. 
#### Antivirus

I do not have antivirus software running on my Mac.  Most of the time AV is ineffective because the threat is new and they haven't caught up yet.  It also phones home a lot and you have no idea what it's saying.

I have occasionally scanned with [ClamXav](https://www.clamxav.com) and never found anything.  

One can pass on Windows viruses in emails or Word docs.  If you would like to check for this, ClamXav should detect it.

Furthermore, Macs have not been strongly targeted by virus writers, for reasons that are debated.The history of threats on Mac is instructive, here is a write-up of [one](https://blog.malwarebytes.com/threat-analysis/mac-threat-analysis/).

In this exploit, the download site for DVD-ripping software **HandBrake** was hacked.  For a period of four days, a version that installs [Proton.B](https://www.cybereason.com/labs-proton-b-what-this-mac-malware-actually-does/) was what you got with your download.  

The first thing the malware did was to ask for your password, so it could upgrade its privileges.  The next thing it did was to steal your Keychain.

If you're interested in this topic Objective-See has a [page](https://objective-see.com/malware.html) where you can see a list of Mac malware.  Don't download them, but there is a link for information about each one.I am always looking for new threats on the web by monitoring sites like* [hacker news](https://news.ycombinator.com)* [Brian Krebs](https://krebsonsecurity.com)
* [malwarebytes](https://blog.malwarebytes.com)
As an aside, I frequently remove all website info from Safari, and clear the history as well, but that's more so I can read interesting NYT articles.

#### PasswordsOne can classify passwords as low, medium and high security.  

* Low are held in the Keychain.

* Medium are held in an encrypted file which I decrypt for each use with a master password.  **Disk Utility** can do this for you.

Length and randomness are most important, while a large character set is less important.  

Complexity goes like SZ^N (size of the character set raised to the power of the length of the password).

[Here](https://www.troyhunt.com/passwords-evolved-authentication-guidance-for-the-modern-era/) is a good discussion of several password issues.  Requirements that encourage use of weak passwords (like resets every 3 months) are a bad idea.I generate long random passwords, e.g.

* `cohacrtztnlkinlaiemilrbrhrvvwr`
* `wTbJFUDuZPXBrUTvgqkHLFPRCBwvly`

using a simple utility that I wrote.

You can generate random passwords with the KeyChain Access utility.  [Here](http://osxdaily.com/2011/05/10/generate-random-passwords-command-line/) and [here](https://apple.stackexchange.com/questions/170453/access-keychain-access-password-generator-password-assistant-via-terminal-with) are other options.

A couple more simple ideas, from Terminal

```
> openssl rand -hex 20
c4ef62b60e7dc0e4117150dabf9b138e7b2da462
> openssl rand -base64 20
J93ov/tvvmRFalbw7XRpZBfOQz0=
>
```

You probably want to remove characters like `=/` from the output.

Also

```
> printf "my passphrase" | md5
d2cb415e067c7b13409eeb425cae6418
> printf "my passphrase" | openssl dgst -sha256
2cec71ecf27a78e25ccbfdce41783760c2df45d8751c8a59c811a2005f1f05a7
>
```

#### Backups

The eternal question is how to backup data securely, since the two requirements (frequency and security) conflict.

I store my encrypted password file on Dropbox.  I also have backups stored on various hard drives, though these may not be completely up-to-date.

Someone I trust recommends [1Password](https://1password.com) (see [discussion](https://news.ycombinator.com/item?id=9728029)).

I use random text (basically, a password like the one above) for any secret question, though I did once give my mother's birth year as 1809.  Obviously, this needs to be saved securely so it can be copied and pasted.  That's why web forms that disable password pasting are evil.

For extra security, your everyday account used to surf the web should be a non-admin user.

I used to write high security passwords (banking) down on a piece of paper.  Now I recommend that you set up a separate User for banking.  My Dropbox is only available from that account.

#### Actual Mac security threats.

It may be helpful to review recent actual security threats observed for macOS.

(in progress)

* [Fruitfly](Fruitfly.md) (2017)
* [Proton.B](Proton_B.md)
* [Pollicare](Pollicare.md)
