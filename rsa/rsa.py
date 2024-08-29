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

class SignatureAlgorithm : 
    def generateKeyPair() :
        p, q = generateTwoPrimes()
        n = p * q
        z = (p - 1) * (q - 1)
        e = 65537
        d = pow(e, -1, z)
        sk = (n, d)
        pk = (n, e)
        return sk, pk

sa = SignatureAlgorithm
sk, pk = sa.generateKeyPair()
print(sk, pk)