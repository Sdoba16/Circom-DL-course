from random import randint
import hashlib 

def is_prime(num, test_count):
    if num == 1:
        return False
    if test_count >= num:
        test_count = num - 1
    for x in range(test_count):
        val = randint(1, num - 1)
        if pow(val, num-1, num) != 1:
            return False
    return True

def generate_big_prime(n):
    found_prime = False
    while not found_prime:
        p = randint(2**(n-1), 2**n)
        if is_prime(p, 1000):
            return p
        
def generateTwoPrimes() :
    p = generate_big_prime(256)
    q = generate_big_prime(256)
    return p, q    

class PrivatKey :
    def __init__(self, n, d) :
        self.n = n
        self.d = d
        
    def signMessage(self, message) :
        return pow(message, self.d, self.n)
             
class PublicKey :
    def __init__(self, n, e) :
        self.n = n
        self.e = e
    def verifySignature(self, signature, message) :
        return 1 if pow(signature, self.e, self.n) == message else 0
        
class SignatureAlgorithm : 
    def generateKeyPair() :
        p, q = generateTwoPrimes()
        n = p * q
        z = (p - 1) * (q - 1)
        e = 65537
        d = pow(e, -1, z)
        sk = PrivatKey(n, d)
        pk = PublicKey(n, e)
        return sk, pk
    
    def signMessage(self, sk, message) :
        return sk.signMessage(message)
        
    def verifySignature(self, pk, signature, message) :
        return pk.verifySignature(signature, message)
        
class KeyPair :
    def __init__(self) :
        sigAlg = SignatureAlgorithm
        self.sk, self.pk = sigAlg.generateKeyPair()
    
    def getKeyPair(self) :
        return self.sk, self.pk

kp = KeyPair()
sa = SignatureAlgorithm()
message = int(hashlib.sha256("127789823899882".encode()).hexdigest(),16)
print(kp.sk.n, kp.sk.d)
print(kp.pk.n, kp.pk.e)
print(message)
print(sa.verifySignature(kp.pk, sa.signMessage(kp.sk, message), message))
print(sa.verifySignature(kp.pk, sa.signMessage(kp.sk, message) + 1, message))
print(sa.verifySignature(kp.pk, sa.signMessage(kp.sk, message), message+1))