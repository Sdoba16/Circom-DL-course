pragma circom 2.1.9;

include "./powMod.circom";

template verifyRSA() {
    signal input pk[16];
    signal input signature[16];
    signal input message[16];

    component sigPowE = PowerMod(64, 16, 17);
    for(var i = 0; i < 16; i++) {
        sigPowE.base[i] <== signature[i];
        sigPowE.modulus[i] <== pk[i];
    }
    message === sigPowE.out;
}

component main = verifyRSA();
