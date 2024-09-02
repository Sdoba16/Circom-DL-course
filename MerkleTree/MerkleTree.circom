pragma circom 2.1.9;

include "../node_modules/circom-ecdsa/circuits/ecdsa.circom";
include "../node_modules/circomlib/circuits/poseidon.circom";
include "../node_modules/circom-ecdsa/circuits/zk-identity/eth.circom";

template Verification(n, k, pathlen) {
    signal input R[k];
    signal input S[k];
    signal input PubKey[2][k];
    signal input path[pathlen];
    signal input order[pathlen];
    signal input root;
    signal input msghash[k];
    
    component ecdsaCheck = ECDSAVerifyNoPubkeyCheck(64, 4);
    ecdsaCheck.r <== R;
    ecdsaCheck.s <== S;
    ecdsaCheck.msghash <== msghash;
    ecdsaCheck.pubkey <== PubKey;

    ecdsaCheck.result === 1;
    component flattenPub = FlattenPubkey(n, k);
    for (var i = 0; i < k; i++) {
        flattenPub.chunkedPubkey[0][i] <== PubKey[0][i];
        flattenPub.chunkedPubkey[1][i] <== PubKey[1][i];
    }

    component pubToAddr = PubkeyToAddress();
    for (var i = 0; i < 512; i++) {
        pubToAddr.pubkeyBits[i] <== flattenPub.pubkeyBits[i];
    }

    component hash[pathlen + 1];
    hash[0] = Poseidon(1);
    hash[0].inputs[0] <== pubToAddr.address;

    for (var i = 1; i < pathlen+1; i++) {
        hash[i] = Poseidon(2);
        hash[i].inputs[0] <== (hash[i - 1].out - path[i - 1]) * order[i - 1] + path[i - 1];
        hash[i].inputs[1] <== hash[i - 1].out + (path[i - 1] - hash[i - 1].out) * order[i - 1];
    }
    hash[pathlen].out === root;
}

component main{public[root]} = Verification(64, 4, 3);