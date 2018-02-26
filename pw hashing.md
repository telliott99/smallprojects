#### Security topics

password hashing

```
>>> from werkzeug.security import generate_password_hash
>>> from werkzeug.security import check_password_hash
>>> h = generate_password_hash('JwVLh-SfkcM')
>>> h
'pbkdf2:sha256:50000$jcNeO590$c2bf0cf0661b46d7c0ea848def136e898c273d14ed563e0ef9de1976c37b515e'
>>> pw = 'JwVLh-SfkcM'
>>> h = generate_password_hash(pw)
>>> check_password_hash(h,pw)
True
>>>
```

In the above example, the protocol is given first, with the number of reps ``'pbkdf2:sha256:50000``, then the salt ``jcNeO590``, and finally, the hash ``c2bf0c..``  

The symbol ``$`` is a separator.

basic [configuration](flask-config/README.md)

Examples of ways to configure an app from environment variables or files.  Multiple configurations for development, staging and production.  SECRET_KEY management.

<hr>

Getting and setting [cookies](flask-security/flask-cookie/README.md) using response objects.

```
r = make_response(render_template(
            'readcookie.html'))
        r.set_cookie('userID', user)
```

<hr>

Session [cookies](flask-session-login/README.md).

<hr>
 
WTF form [validation](flask-wtf-validate/README.md) and csrf_token.

<hr>

Password salting and hashing using ``werkzeug``.