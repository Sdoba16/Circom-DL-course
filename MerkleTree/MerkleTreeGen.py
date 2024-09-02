from poseidon import Poseidon

class MerkleTree :
    def __init__(self, leafs) :
        self.leafs = leafs
        self.size = 1
        self.log = 1
        while self.size < len(leafs) :
            self.size *= 2
            self.log += 1     
        print(self.size)
        self.hashes = [0 for i in range(self.size * 2 - 1)]
        for i in range(self.size * 2 - 2, -1, -1) :
            if i > self.size - 2 :
                self.hashes[i] = Poseidon(1, [leafs[i - self.size + 1]]) if len(leafs) > i - self.size + 1 else Poseidon(1, [0])
            else : 
                self.hashes[i] = Poseidon(2, [self.hashes[i * 2 + 1], self.hashes[i * 2 + 2]])
        self.root = self.hashes[0]

    def genPath(self, leafPos) :
        path = MerklePath(self, leafPos)
        return path
    
    def checkPath(self, leaf, path, root) :
        return(path.checkPath(leaf, root))
               
class MerklePath :
    def __init__(self, Tree, leafPos) :
        self.path = [0 for i in range(Tree.log - 1)]
        self.order = [0 for i in range(Tree.log - 1)]
        index = leafPos + Tree.size - 1
        i = 0
        while(index != 0) :
            self.path[i] = Tree.hashes[index + 1 if index % 2 else index - 1]
            self.order[i] = index % 2
            index = (index - 1) // 2
            i += 1
    
    def checkPath(self, leaf, root) :
        hash = Poseidon(1, [leaf])
        print(hash)
        for i in range(len(self.path)) :
            if self.order[i] == 1:
                hash = Poseidon(2, [hash, self.path[i]])
                print(hash)
            else : 
                hash = Poseidon(2, [self.path[i], hash])
                print(hash)
        return hash == root

MT = MerkleTree([832617623827897388383003283720239102039746790391,
                 930289383278657357873891283273829138923002938833,
                 892398287019823783902393452526142131132314256738,
                 127378388499211119993993830093999040030030003030,
                 838894900202838764689388268183889020176467378887,
                 898421110635513333007180035030047104493247739736,
                 387823762737827372839329183012983092801908299033,
                 678398899007777777777772662673738820001919883838
                 ])
print(MT.hashes)
root = MT.root
print(root)
path = MT.genPath(5)
print(path.path)
print(path.order)
print(path.checkPath(898421110635513333007180035030047104493247739736, root))