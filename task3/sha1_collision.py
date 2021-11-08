import hashlib

def SHA1(string=""):
    return hashlib.sha1(string.encode()).hexdigest()

def find_sha1_collision(hash):
    for nonce in range(560000000,2**256):
        new_hash = SHA1(str(nonce))
        if new_hash == hash:
            print("COLLISION FOUND")
            print("Nonce: ", nonce)
            break

        if nonce % 10000000 == 0:
            print("Current nonce: ", nonce)
            print("Current hash: ", new_hash)


hash = "70481D0F497236A27A2424E6C87D1C6CB606BFF5".lower()
print(hash)
find_sha1_collision(hash)
