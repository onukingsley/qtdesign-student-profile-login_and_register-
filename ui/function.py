from passlib.hash import cisco_pix as ci
from passlib.hash import crypt16 as sa
from documentation import __version__

def checkempty(arrays):
    msg = False
    for case in arrays:
        if not case:
            msg = True

    return msg
