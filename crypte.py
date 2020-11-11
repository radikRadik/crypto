
#!/usr/bin/env python3

"""
#!/usr/bin/env python
qr(phrase=str()) --------------- crea file png con qrcode
wr() --------------------------- crea file pickle(chiavi)
encode_string(phrase=str())
    input: str()
    return:  str() codificata

decode_string(phrase = str()) 
    input:   str()
    return:  str() decodificata 

encrypt_file()
    input:  None
    return: None
    codifica file txt

decrypt_file()
    input:  None
    return: None
    decodifica file txt

"""


import random
import pickle
import os
import os.path
from sys import argv
import random
from sys import exit
try:
    import pyqrcode
    

except ModuleNotFoundError:
    """
    install packets if not installed
    """

    if os.system("pip3 install pyqrcode"):
        print("[!] check your internet connection")
        exit()


    if os.system("pip3 install pypng"):
        print("[!] check your internet connection")
        exit()
    else:
        print("[*] packets successifully installed")
    import pyqrcode



def qr(phrase):
    """
    da installare: pypng pyqrcode
    """

    big_code = pyqrcode.create(phrase , error='L', version=10, mode='binary')
    big_code.png('code.png', scale=6, module_color=[0, 0, 0, 128],
        background=[0xff, 0xff, 0xcc])
    # big_code.show()


len_key = 100

def wr(flag="gen", lnk=90):

    '''
    la funzione [wr] genera chiave pickle

    wr() ------------------- chiave generica, len(chiave) == 90
        flag="cryptocurrency"---- chiave per cryptocurrency
        lnk=int() ------------- lnk ==lunghezza della chiave

    creazione della chiave
    input: prende la prima chiave
    riscrive la chiave in formato dict
    '''

    global len_key
    len_key = lnk
    try:
        os.remove("key.pickle")
        os.remove("crypt.pickle")
        print("[ ] the key is deleted!" )
    except FileNotFoundError:
        print("[ ] pickle file is not found...")

    generic_key = """\\ 234567œ890’‘'ìqwertyu“”iopè+ùasdfghjklòàzxcvbnm,.—-><|!
    "£$%&/()=?^é*°ç_:;{}@#ç°_QWERTYUIOP1ASDFGHJKLZXCVBNM"""
    key_for_crypto_currency = "qwertyuiopasdfghjklzxcvbnm"
    key_for_crypto_currency += key_for_crypto_currency.upper() + "1234567890"

    if flag == 'gen':
        used_key = generic_key
        print("[ ] your generated key is valid for anyway...")
    elif flag == "cryptocurrency":
        used_key = key_for_crypto_currency
        print("[ ] your generated key for cryptocurrency ")
    else:
        used_key == generic_key
        print("[ ] your generated key is valid for anyway...")


    lst = list(set(used_key))
    df = {}
    for i in range(1, len_key):
        random.shuffle(lst)
        lst = [i for i in lst]
        df[i] = lst

    with open('key.pickle', 'bw') as dh:
        pickle.dump(lst, dh)
        print("[ ] a new 'key.pickle' is generated...")

    with open('crypt.pickle', 'bw') as dg:
        pickle.dump(df, dg)
        print("[ ] a new 'crypt.pickle' is generated...")    
    print(f"[ ] the length of key is {len_key}...")


def load_pickle_dict():
    with open('crypt.pickle', 'rb') as dg:
        d = pickle.load(dg)
    return d


def load_pickle_list():
    """
    the first key list
    """
    with open('key.pickle', 'rb') as dg:
        alfa = pickle.load(dg)
    return alfa


def encode_string(fras):

    global len_key
    fras = add_space(fras)
    encrypted_string = ""
    key_list = load_pickle_list()
    key_dict = load_pickle_dict()
    encoded_list = [] # list of index of any letter of the encrypted_string
    index = 0

    for i in fras:
        encoded_list.append(key_list.index(i))
    for i in range(1, len(encoded_list), len(key_dict)):
        for k in range(1, len(key_dict) + 1):
            try:
                encrypted_string += key_dict[k][encoded_list[index]]
            except IndexError:
                pass
            except KeyError:
                pass
            index += 1
    #qr(encrypted_string)

    return encrypted_string


def add_space(s):
	a = '9gf4nlbk7pcith5mra1s3edvz802qou6xwjy'
	lst = list(a)
	lst2 = list(a)

	random.shuffle(lst)
	aggiunta = "".join(lst)

	random.shuffle(lst2)
	aggiunta_finale = "".join(lst2)

	index_start = random.randint(1,35)
	index_end = random.randint(1,35)
	s = (a[index_start] + a[index_end] + aggiunta[index_start:]+ s + aggiunta_finale[:index_end] )
	return s


def remove_space(s):
	a = '9gf4nlbk7pcith5mra1s3edvz802qou6xwjy'
	lst = list(a)

	n = a.index(s[0])
	n_finale = a.index(s[1])
	aggiunta = len(lst[n:])

	ns = s[aggiunta+2:]

	return ns[:-n_finale]


def decode_string(phrase):
    global len_key
    encrypted_string = ""
    key_list = load_pickle_list()
    key_dict = load_pickle_dict()
    index = 0
    for i in range(1, len(phrase), len(key_dict)):
        for k in range(1, len(key_dict) + 1):
            try:
                ind = key_dict[k].index(phrase[index])
                index += 1
                encrypted_string += key_list[ind]
            except IndexError:
                pass
            except KeyError:
                pass
    #qr(encrypted_string)
    return remove_space(encrypted_string)
    # return encrypted_string


def decrypt_file(q=False):
    list_file = os.listdir()

    if "encrypted.txt" in list_file:
        with open("encrypted.txt", "r") as df:
            tex = df.read()

            if len(tex) == 0:
                print("[ ] 'encrypted.txt' is empty...'")
                return
        try:    
            tex = decode_string(tex)
            # impostando [q=True], si crea il codice qr del testo decriptato
            if q: qr(tex)
        except FileNotFoundError:
            print("[ ] the key not found...")
            wr()
            print("[ ] the new key is created with succes")
            return decrypt_file()
            
        with open("decrypted.txt", "w") as df:
            df.write(tex)
        print("[ ] file is decrypted...***")
        return
    print("[ ] the file 'encrypted.txt' is not found")
    make_file("encrypted.txt")
    decrypt_file()
            

def encrypt_file(q=False):
    list_file = os.listdir()
    if "decrypted.txt" in list_file:
        with open("decrypted.txt", "r") as df:
            tex = df.read()

            if len(tex) == 0:
                print("[ ] 'decrypted.txt' is empty...'")
                return
        try:
            tex = encode_string(tex)
            # impostando [q=True], si crea il codice qr del testo criptato
            if q: qr(tex)

        except FileNotFoundError:
            print("[ ] the key not found...")
            wr()
            print("[ ] the new key is created with succes")
            return encrypt_file()

        with open("encrypted.txt", "w") as df:
            df.write(tex)
        print("[ ] file is encrypted...")
        with open("decrypted.txt", "w") as df:
            df.write("")
        return

    print("[a ] the file 'decrypted.txt' is not found")
    make_file("decrypted.txt")
    encrypt_file()

def make_file(name_file):
    with open(name_file, "w") as df:
        df.write("")
    print(f"[ ] the new {name_file} is created...")



# if __name__ == '__main__':
# 	eval(argv[])