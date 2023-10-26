# Practical-1
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

if __name__ == "__main__":
    plaintext = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))
    encrypted_text = caesar_cipher(plaintext, shift)
    decrypted_text = caesar_decipher(encrypted_text, shift)
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)

# Practical-2
import string
import random

def generate_cipher_alphabet(seed):
    # Create a shuffled version of the alphabet based on the provided seed
    alphabet = list(string.ascii_lowercase)
    random.seed(seed)
    random.shuffle(alphabet)
    return ''.join(alphabet)

def monoalphabetic_cipher(text, cipher_alphabet):
    # Create a dictionary to map each letter to its corresponding cipher letter
    mapping = {letter: cipher_alphabet[i] for i, letter in enumerate(string.ascii_lowercase)}
    
    # Encrypt the text using the cipher alphabet
    encrypted_text = ''.join([mapping.get(char, char) for char in text])
    
    return encrypted_text

def monoalphabetic_decipher(encrypted_text, cipher_alphabet):
    # Create a dictionary to map each cipher letter back to its original letter
    reverse_mapping = {cipher_alphabet[i]: letter for i, letter in enumerate(string.ascii_lowercase)}
    
    # Decrypt the text using the reverse mapping
    decrypted_text = ''.join([reverse_mapping.get(char, char) for char in encrypted_text])
    
    return decrypted_text

if __name__ == "__main__":
    seed = input("Enter a seed for generating the cipher alphabet: ")
    cipher_alphabet = generate_cipher_alphabet(seed)
    
    plaintext = input("Enter the text to encrypt: ")
    encrypted_text = monoalphabetic_cipher(plaintext, cipher_alphabet)
    
    print("Cipher Alphabet:", cipher_alphabet)
    print("Encrypted text:", encrypted_text)
    
    decrypted_text = monoalphabetic_decipher(encrypted_text, cipher_alphabet)
    print("Decrypted text:", decrypted_text)


# Practical-3
def encrypt_rail_fence(text,rails):
    fence=[[]for _ in range(rails)]
    rail = 0
    direction = 1

    for char in text:
        fence[rail].append(char)
        rail += direction

        #change direction when reaching the top or bottom rail
        if rail ==0 or rail == rails-1:
            direction *= -1

    #Combine the fence rails into a single string
    encrypted_text = ''.join([''.join(rail) for rail in fence])
    return encrypted_text

def decrypt_rail_fence(encrypted_text,rails):
    fence = [[] for _ in range(rails)]
    rail_lengths = [0]*rails
    rail =0
    direction = 1

    for i in range(len(encrypted_text)):
        rail_lengths[rail] += 1
        rail +=direction

        #Change direction when reaching the top or bottom rail
        if rail == 0 or rail == rails-1:
            direction *=-1

    #fill in the fence with the encrypted text
    index = 0
    for rail in range(rails):
        fence[rail] = list(encrypted_text[index:index +rail_lengths[rail]])
        index += rail_lengths[rail]

    #Reconstrut the original message
    rail = 0
    direction = 1
    decrypted_text =[]
    for _ in range(len(encrypted_text)):
        decrypted_text.append(fence[rail].pop(0))
        rail += direction

        #change direction when reaching the top or bottom rail
        if rail == 0 or rail == rails  -1:
            direction *= -1

    return "".join(decrypted_text)

#example usage

message = "BHARAT"
rails = 3
encrypted = encrypt_rail_fence(message,rails)
print("Encrypted: ",encrypted)

decrypted = decrypt_rail_fence(encrypted,rails)
print("Decrypted: ",decrypted)

# Practical-4 
import random
import math
def is_prime(num):
    if num<=1:
        return False
    if num<=3:
        return True
    if num%2==0 or num%3==0:
        return False
    i=5
    while i*i<=num:
        if num%i==0 or num%(i+2)==0:
            return False
        i+=6
    return True
def gcd (a,b):
    while b:
        a,b=b,a%b
    return a
def mod_inverse(a,m):
    m0,x0,x1=m,0,1
    while a>1:
        q=a//m
        m,a=a%m,m
        x0,x1=x1-q*x0,x0
    return x1+m0 if x1<0 else x1
def generate_keypair(p,q):
    if not(is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    if p==q:
        raise ValueError("p and q cannot be equal.")
    n=p*q
    phi=(p-1)*(q-1)
    e=random.randrange(2,phi)
    while gcd(e,phi)!=1:
        e=random.randrange(2,phi)
    d=mod_inverse(e,phi)
    return ((n,e),(n,d))
def encrypt(public_key,plaintext):
    n,e=public_key
    encrypted=[pow(ord(char),e,n)for char in plaintext]
    return encrypted
def decrypt(private_key,ciphertext):
    n,d=private_key
    decrypted=[chr(pow(char,d,n))for char in ciphertext]
    return ''.join(decrypted)
if __name__=="__main__":
    p=61
    q=53
    public_key,private_key=generate_keypair(p,q)
    message="ganesh"
    print("Original message:",message)
    encrypted_message=encrypt(public_key,message)
    print("Encrypted message:",encrypted_message)
    decrypted_message=decrypt(private_key,encrypted_message)
    print("Decrypted message:",decrypted_message)


# Practical-5
import math

int1  = int(input("Enter the modulo p: "))
int2 = int(input(f"Enter the root primitive of {int1}: "))

a = int(input("Choose the 1st secret number(Alice): "))
b = int(input("Choose the 2nd secret number(Bob): "))

A= int(math.pow(int2,a)%int1)
B= int(math.pow(int2,b)%int1)

A_ = int(math.pow(B,a)%int1)
B_ = int(math.pow(A,b)%int1)
if A_ == B_:
    print("Alice & Bob can comminicate with each other")
else:
    print("Alice & Bob cannot communicate with each other")

# Practical-6
from hashlib  import md5
str1 = input("Enter the Plain text: ")

if str1.isalpha()==True:
    hashed = "Message digest after implementation of md5 algorithm: "+md5(str1.encode('utf-8')).hexdigest()
else:
    print("Enter the alphabetic characters only")

print(hashed)

# Practical-7
from hashlib import sha256
str1 = input("Enter the Plain Text: ")

if str1.isalpha()==True:
    print("Calculated HMAC-SHA256 Signature for the given text is: ")
    hashed = sha256(str1.encode('utf-8')).hexdigest()
else:
    print("Enter the alphabetic characters only")
print(hashed)