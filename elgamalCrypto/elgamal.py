import random
import sys

sys.set_int_max_str_digits(1000000)

ALPHA = None
BETA = None
CIPHER = []
k = None
a = None
PRIME = None


def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)

def power(a, b, c):
    x = 1
    y = a

    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)

    return x % c


def generate_prime(bits):
    p = random.randint(2**bits, 2**(bits+1))
    while not is_prime(p):
        p = random.randint(2**bits, 2**(bits+1))
    return p

def generate_prime_alpha(bits):
    global generator_bits
    p = random.randint(2**bits, 2**(bits+1)-1)
    alpha = random.randint(2**generator_bits+1, 2**(generator_bits+1)-1 )
    while gcd(p,alpha)!=1:
        alpha = random.randint(2**generator_bits+1, 2**(generator_bits+1)-1 )
    return p, alpha


def gen_key(p):
    mn = 2**key_bits+1
    mx = 2**(key_bits+1)-1
    key = random.randint(mn, mx)
    while gcd(p, key)!=1:
        key = random.randint(mn, mx)
    return key


def is_prime(p):
    if p%2==0:
        return False
    for i in range(3, int(p**0.5)+1, 2):
        if p%i==0:
            return False
    else:
        return True


def random_sentence():
    with open("sentence.txt", 'r') as file:
        s = file.readlines()
    return random.choice(s).strip()    



def encrypt(msg):
    global CIPHER
    global k
    global BETA
    global PRIME
    BETA_K = power(BETA, k, PRIME)
    for  m in msg:
        if k_different:
            k = gen_key(PRIME)
            y = power(ALPHA, k, PRIME)
            BETA_K = power(BETA, k, PRIME)
            c = ord(m) * BETA_K
            CIPHER.append((c, y))
        else:
            c = ord(m) * BETA_K
            CIPHER.append(c)
    return CIPHER


def decrypt():
    global PRIME
    global a
    global CIPHER
    global y
    y_a = power(y, a, PRIME)
    message = ""
    for c in CIPHER:
        if k_different:

            y_a = power(c[1], a, PRIME)
            m = chr( int(c[0] / y_a))
            message+=m
        else:
            m = chr(int(c / y_a))
            message+=m
    print(message)



if __name__ == "__main__":
    prime_bits = 64
    key_bits = 16
    generator_bits = 32
    k_different = False
    # PRIME = generate_prime(prime_bits)
    # ALPHA = random.randint(1, PRIME - 1)
    # PRIME, ALPHA = generate_prime_alpha(prime_bits)
    # print(PRIME, ALPHA)
    PRIME  = random.randint(2**prime_bits,  2**(prime_bits+1)-1)
    ALPHA = random.randint(2, PRIME-1)

    a = gen_key(PRIME)
    BETA = power(ALPHA, a, PRIME)
    k = gen_key(PRIME)
    y = power(ALPHA, k, PRIME)
    message = input("Enter message : ")
    if message.strip()=="":
        message = random_sentence()
    encrypt(message)
    print(f"PUBLIC KEY (p,alpha,beta): ({PRIME},{ALPHA},{BETA})")
    print(f"y : {y}")
    print(f"cipher : {CIPHER}")
    print()
    decrypt()