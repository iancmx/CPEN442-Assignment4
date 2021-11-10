import hashlib
import random

def SHA256(string=""):
    return hashlib.sha256(string.encode()).hexdigest()

def mine_coin_randomly(hash_of_preceding_coin=None, id_of_miner=None):
    prefix = "00000000"
    random.seed()
    blobs_count = 0
    while True:
        coin_blob = random.randint(0, 2**256)
        hash = SHA256("CPEN 442 Coin" + "2021" + hash_of_preceding_coin + str(coin_blob) + id_of_miner)

        if blobs_count % 1000000 == 0:
            print("Blob count: ", blobs_count)
            print("Current coin blob: ", coin_blob)
            print("Current hash: ", hash)

        if hash.startswith(prefix):
            print("CPEN442 coin successfully mined!")
            print("Coin blob: ", coin_blob)
            print("Hash: ", hash)
            break
        blobs_count += 1

def mine_coin_incrementally(hash_of_preceding_coin=None, id_of_miner=None):
    prefix = "00000000"
    max_nonce = 100000000000
    starting_nonce = 0
    random.seed()
    for coin_blob in range(starting_nonce, max_nonce):
        hash = SHA256("CPEN 442 Coin" + "2021" + hash_of_preceding_coin + str(coin_blob) + id_of_miner)

        if coin_blob % 10000000 == 0:
            print(coin_blob)
            print("{:.2%}".format(coin_blob/max_nonce))

        if hash.startswith(prefix):
            print("CPEN442 coin successfully mined!")
            print("Coin blob: ", coin_blob)
            print("Hash: ", hash)
            break


hash_of_preceding_coin = "a9c1ae3f4fc29d0be9113a42090a5ef9fdef93f5ec4777a008873972e60bb532"
id_of_miner = SHA256("74260878")
mine_coin_incrementally(hash_of_preceding_coin, id_of_miner)