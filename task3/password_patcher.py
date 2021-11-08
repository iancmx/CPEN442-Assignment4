import hashlib
import sys

def SHA1(string=""):
    return hashlib.sha1(string.encode()).digest()


def patch_password(filename="", password=""):
    if len(filename) == 0:
        return
    new_sha1_hash = SHA1(password)

    try:
        fh = open(filename, 'r+b')
    except OSError:
        print("Could not open file")

    with fh:
        fh.seek(0x0001D433)
        fh.write(new_sha1_hash)

    print("Patch Complete")

patch_password(sys.argv[1], sys.argv[2])
