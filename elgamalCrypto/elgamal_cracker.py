import string
import time
from tqdm import tqdm 

slow = 0.05


k_different = input("encryption secrete different (1/0)? ")
while k_different not in "10":
    print("you must enter 1 or 0")
    k_different = input("encryption secrete different (1/0)? ")
k_different = int(k_different)

cipher = list(eval(input("Enter Cipher : ")))


print()

def crack():
    message = []
    creacked_messages = []
    beta = None
    start = 0
    start_again = True
    while start<len(string.printable) :
        if start_again:
            beta = int(cipher[0] / ord(string.printable[start]))
            start_again = False
            message.append(string.printable[start])
            print("".join(message), end='\r')
            time.sleep(slow)

        for  c in cipher[1:]:
            for m in string.printable:
                check = c / ord(m) == beta
                if check:
                    time.sleep(slow)
                    message.append(m)
                    print("".join(message), end='\r')
                    found = True
                    break
            else:
                start+=1
                start_again = True
                message = []
                break
        if len(message)==len(cipher):
            print(f"\"{''.join(message)}\"")
            creacked_messages.append(''.join(message))
            start+=1
            start_again = True
            message = []

    print(f"creacked message : {creacked_messages}")


def cracken_k(cipher):
    tmp_msg = []
    for m in string.printable:
        # print(f"{msg}{m}", end='\r')
        if cipher[0] % ord(m) == 0:
            tmp_msg.append(m)
    return tmp_msg

def crack_k_different():
    global cipher
    message = []
    for C in cipher:
        tmp_msg = cracken_k(C)
        message.append(tmp_msg)
        print(tmp_msg)
    print()
    print()
    print(f"Cracked Message : {message}")


if __name__== "__main__":
    if k_different==0:
        crack()
    if k_different==1:
        crack_k_different()