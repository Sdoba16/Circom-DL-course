import babyjj
import random
from poseidon_py import poseidon_hash

bj = babyjj.Babyjj()

class Signature :
    def __init__(self, R, S) :
        self.R = R
        self.S = S

class PrivateKey :
    def __init__(self, k) :
        self.k = k
        
        
    #def signMessage(self, message) :

class PublicKey :
    def __init__(self, sk) :
        h = poseidon_hash.poseidon_hash_single(sk.k)
        s = bin(h)[2:129]
        s = int(s, 2)
        self.A = bj.scalarMultiplication(s, bj.B)
    #def verifySignature(self, signature, message) :
        
class SignatureAlgorithm : 
    def generateKeyPair(self) :
        k = random.randint(1, bj.l)
        sk = PrivateKey(k)
        pk = PublicKey(sk)
        return sk, pk
    #def signMessage(self, sk, message) :
    #    return sk.signMessage(message)
    #def verifySignature(self, pk, signature, message) :
    #    return pk.verifySignature(signature, message)
        

sa = SignatureAlgorithm()
sk, pk = sa.generateKeyPair()
print(pk.A.x, pk.A.y)
print(bj.checkPoint(pk.A))
#print(sa.verifySignature(pk, sa.signMessage(sk, "message"), "message"))