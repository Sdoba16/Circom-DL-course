import babyjj
import random
from poseidon_py import poseidon_hash
import hashlib

bj = babyjj.Babyjj()

class Signature :
    def __init__(self, R, S) :
        self.R = R
        self.S = S

class PrivateKey :
    def __init__(self, k) :
        self.k = k
        
    def signMessage(self, message) :
        h = poseidon_hash.poseidon_hash_single(sk.k)
        r0 = bin(h)[129:]
        r0 = int(r0, 2)
        s = bin(h)[2:129]
        s = int(s, 2)
        A = bj.scalarMultiplication(s, bj.B)
        h1 = poseidon_hash.poseidon_hash(r0, message)
        r = bin(h1)[2:]
        r = int(r, 2)
        R = bj.scalarMultiplication(r, bj.B)
        h = poseidon_hash.poseidon_hash_many([R.x, R.y, A.x, A.y, message])
        S = (r + h * s) % bj.l
        sig = Signature(R, S)
        return sig

class PublicKey :
    def __init__(self, sk) :
        h = poseidon_hash.poseidon_hash_single(sk.k)
        s = bin(h)[2:129]
        s = int(s, 2)
        self.A = bj.scalarMultiplication(s, bj.B)
        
    def verifySignature(self, signature, message) :
        R = signature.R
        S = signature.S
        A = pk.A
        leftPart = bj.scalarMultiplication(bj.c * S, bj.B)
        h = poseidon_hash.poseidon_hash_many([R.x, R.y, A.x, A.y, message])
        rightPart = bj.pointSum(bj.scalarMultiplication(bj.c, R), bj.scalarMultiplication(bj.c * h, A))
        return 1 if leftPart.x == rightPart.x and leftPart.y == rightPart.y else 0
        
class SignatureAlgorithm : 
    def generateKeyPair(self) :
        k = random.randint(1, bj.l)
        sk = PrivateKey(k)
        pk = PublicKey(sk)
        return sk, pk
    
    def signMessage(self, sk, message) :
        return sk.signMessage(message)
    
    def verifySignature(self, pk, signature, message) :
        return pk.verifySignature(signature, message)
        

sa = SignatureAlgorithm()
sk, pk = sa.generateKeyPair()
print(pk.A.x, pk.A.y)
print(bj.checkPoint(pk.A))
message = int(hashlib.sha256("127789823899882".encode()).hexdigest(),16) % bj.l
print(sa.verifySignature(pk, sa.signMessage(sk, message), message))
print(sa.verifySignature(pk, sa.signMessage(sk, message), message+1))