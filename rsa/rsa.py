from random import randint

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
    
class PublicKey :
    def __init__(self, n, e) :
        self.n = n
        self.e = e
        

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
        
class KeyPair :
    def __init__(self) :
        sigAlg = SignatureAlgorithm
        self.sk, self.pk = sigAlg.generateKeyPair()
    
    def getKeyPair(self) :
        return self.sk, self.pk

kp = KeyPair()
print(kp.sk.d, kp.pk.e)