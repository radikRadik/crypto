import crypte
import os

# crea una nuova chiave
os.remove("key.pickle")
print('[ ] file pickle deleted')
os.remove("crypt.pickle")
crypte.wr(lnk=500)

