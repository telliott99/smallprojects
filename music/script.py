import subprocess, os

user =  '/Users/telliott_admin/'
desk =  user + 'Desktop/'
dst = desk + 'Purchased/'

#-------------------

playlist_fn = 'Purchased.txt'
fh = open(playlist_fn)
data = fh.read().strip()
fh.close()

data = data[2:]      # remove BOM
L = list()

while data:
    c = data[0]
    junk = data[1]   # remove high-order UTF-16 byte
    data = data[2:]
    L.append(c)

s = ''.join(L)
L = s.split('\r')[1:]   # split on old-style newline

#-------------------
music = user + 'Music/iTunes/iTunes Media/Music/'

for e in L:
    path = e.split('\t')[-1]       # grab the last tab
    path = path.replace(':','/')   # use standard path sep
    
    src = path.replace('Macintosh HD','')   # strip Volume
    info = src.replace(music,'')   # only artist/album etc.
    album = '/'.join(info.split('/')[:-1])  # not song title
    
    '''    # debug
    print 'path:\n' + path
    print 'src:\n' + src
    print 'info:\n' + info
    print 'dst:\n' + dst + info
    print 'album:\n' + album
    '''
    
    try:
        # make full dir path if it doesn't already exist
        if not os.path.isdir(desk + 'Purchased/' + album):
            os.makedirs(desk + 'Purchased/' + album)
            
        subprocess.call(['cp', src, dst + info])
    except OSError as exc:
        print 'error\n' + path
        print exc
    
        
