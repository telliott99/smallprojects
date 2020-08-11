#### Passwords

Passwords are an essential feature of modern computer and web use.  Security requires the use of random passwords that are long enough.  

Almost no one can remember such passwords.  The trick is to save them in a file which is encrypted using a good password which you can remember.  (Or a password which is written down on paper).

To generate passwords, I just do ``pw`` in Terminal:

    > pw 20
    uimeirhccnfigyfrrmqy

``pw`` is a Python script that lives in ``~/Dropbox/bin``, which is on my ``$PATH``.  The listing:

    #! python3
    import sys, secrets
    
    s =  'abcdefghijklmnopqrstuvwxyz'
    # s += '0123456789'
    n = int(sys.argv[1])
    L = [secrets.choice(s) for i in range(n)]
    pw = ''.join(L)
    print(pw)

You could make it even easier by using ``openssl``: :

    > alias pw="openssl rand -base64 20"
    > pw 
    g7sjK3jei9O0Bfv/ZT891tXywKk=
    >
    
Write that into ``~/.zshrc``.

#### Scripting encryption and decryption

I wrote three short ``zsh`` scripts for managing encryption and decryption.

**codec**:

    #! zsh

    ifn=$1
    echo $1
    
    if [[ $2 == -d ]]; then
      openssl enc -d -a -aes-256-cbc -salt -in $ifn -out $ifn.dec
    else
      openssl enc -a -aes-256-cbc -in $ifn -out $ifn.enc
    fi
    
What this does is read and echo a filename input.  Then it uses ``openssl enc`` to either encrypt or decrypt.  The ``openssl enc`` utility automatically prompts for the password.

To use it in decrypting a password file ``pw.txt.enc``:

**openpw**

    #! zsh

    ifn="/path/to/pw.txt.enc"
    codec $ifn -d
    open -a TextEdit $ifn.dec
    
    sleep 2
    rm $ifn.dec 

The decoded passwords appear in TextEdit, while the decrypted file is deleted from disk.

For encrypting:

**savepw**

    #! zsh

    ifn="/path/to/pw.txt"
    codec $ifn

To use these, I simply open Terminal and enter

    openpw

or

    savepw

One reason this helps is that, in fact, I have two encrypted password files:  a regular one for most accounts and credit cards, and a super-secret one for banking.  

I stripped out the code that handles the different cases, but I choose between the two by simply entering anything as an additional argument:

    > openpw s
    special
    /path/to/pw.txt.enc
    enter aes-256-cbc decryption password:
