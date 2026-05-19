import random


class rsa_keys:

    def generate(rng_start,rng_end):
        rng_start = int(rng_start)
        rng_end = int(rng_end)

        print("generating random prime number........")
        p = rsa_keys.generate_prime(rng_start,rng_end)
        q = rsa_keys.generate_prime(rng_start,rng_end)
        while p == q:
            q = rsa_keys.generate_prime(rng_start,rng_end)
        print(f"genarated prime numbers are {p} and {q}")

        print("generating public and private key .......")
        public_key , private_key = rsa_keys.generate_keys(p,q)
        print(f"your public key is  {public_key}\nyour private key is  {private_key}")



    def check_prime(prime):
        if prime%2==0:
            return False
        for i in range(3,int(prime**0.5)+2,2):
            if prime%i==0:
                return False
        else:
            return True



    def generate_prime(start,end):
        prime = random.randrange(start,end+1)
        while rsa_keys.check_prime(prime) == False:
            prime = random.randrange(start,end+1)
        
        return prime 


    def check_coprime(a,b):
        while b != 0:
            a , b = b , a%b 
        if a == 1:
            return False
        else:
            return True

    def MUL_INVERSE(e,phi):
        for i in range(1,phi):
            if (e*i)%phi==phi-1:
                return phi - i 
            if (e*i)%phi == 1:
                return i


    def multiplicative_inverse(e, phi):
        if e == 0:
            x = 0 
            y = 1
            return x,y
        x,y = rsa_keys.multiplicative_inverse(phi%e,e)
        x , y = y - (phi//e)*x , x
        return x , y      


    def generate_keys(p,q):
        n = p*q
        phi = (p-1) * (q-1)

        e = random.randrange(2,phi)
        while rsa_keys.check_coprime(e,phi) :
            e = random.randrange(2,phi)

        d , unwanted_value = rsa_keys.multiplicative_inverse(e,phi)
        d %= phi
        return (e,n) , (d,n)


class rsa_cipher:

    def encrypt(message,key):
        cipher = []
        e,n = key
        for char in message:
            mod = pow(ord(char),e,n)
            cipher.append(str(mod))
        cipher = ','.join(cipher)
        return cipher

    
    def Decrypt(cipher,key):
        cipher = cipher.split(",")
        message = ""
        d,n = key
        for cip in cipher:
            char = chr(pow(int(cip),d,n))
            message += char
        return message



class _main_:

    def __main__(command):
        comm = command.split(' ')
        if comm[0] == "keys":
            try:
                range_ = comm[1].split(',')
                rsa_keys.generate(range_[0],range_[1])
            except:
                print("you type a wrong command bro :((\ntry this - keys 10000,99999")
        if comm[0] == "encrypt":
            message = input("enter message to encrypt : ")
            try:
                key = eval(input("enter public key : "))
                cipher = rsa_cipher.encrypt(message,key)
                print(f"RSA cipher is \n{cipher}")
            except:
                print("there is a problem while calculating :(\nenter key in this formate (e,d)")
        if comm[0] == "decrypt":
            cipher = input("enter cipher : ")
            try:
                key = eval(input("enter private key : "))
                message = rsa_cipher.Decrypt(cipher,key)
                print(f"Decrypted message is \n{message}\n")
            except:
                print("there is a problem while calculating :(\nenter key in this formate (d,d)")
        if command=="exit":
            pass

        else:
            print("command not found try again ")


skatch = '''
    RRRRRRRRRR      SSSSSSSSSSS        AAAA
    R         R    S           S      A    A
    R  RRRR    R   S   SSSSS   S     A  AA  A
    R  R   R   R   S  SS    S  S    A  A  A  A
    R  RRRR    R   SS  SS   SSSS   A  A    A  A
    R        RR     SS   SS       A   AAAAAA   A
    R  R   RRR         SS   SS   A              A
    R  RRR  R      SSSS   SS  S  A   AAAAAAAA   A
    R  R  R  R     S  S    S  S  A  A        A  A
    R  R   R  R    S  SSSSS   S  A  A        A  A
    R  R    R  R   S          S  A  A        A  A
    RRRR     RRRR   SSSSSSSSSS   AAAA        AAAA

'''

mode = '''select modes from here
to generate public and private key type "keys" and followed by range -- 
for example = "keys 1000,9999"
to encrypt message type "encrypt"
to decrypt message type "decrypt"
to quit type "exit"
'''
print(skatch)
print(mode)

while True:
    command = input(">>> ")
    _main_.__main__(command)
    if command == "exit":
        break
