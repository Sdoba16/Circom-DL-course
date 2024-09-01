pragma circom 2.1.9;

include "../node_modules/circomlib/circuits/babyjub.circom";
include "../node_modules/circomlib/circuits/escalarmulany.circom";
include "../node_modules/circomlib/circuits/poseidon.circom";
include "../node_modules/circomlib/circuits/bitify.circom";

template EdDSAVerifier() {
    signal input pk[2];
    signal input signature[3];
    signal input message;

    component pkOnCurve = BabyCheck();
    pkOnCurve.x <== pk[0];
    pkOnCurve.y <== pk[1];

    component ROnCurve = BabyCheck();
    ROnCurve.x <== signature[0];
    ROnCurve.y <== signature[1];

    component leftPart = BabyPbk();
    leftPart.in <== signature[2];
    
    component hash = Poseidon(5);
    hash.inputs[0] <== signature[0];
    hash.inputs[1] <== signature[1];
    hash.inputs[2] <== pk[0];
    hash.inputs[3] <== pk[1];
    hash.inputs[4] <== message;

    component HashMulA = EscalarMulAny(254);
    component HashBits = Num2Bits_strict();
    HashBits.in <== hash.out;

    HashMulA.e <== HashBits.out;
    HashMulA.p[0] <== pk[0];
    HashMulA.p[1] <== pk[1];

    component rightPart = BabyAdd();
    rightPart.x1 <== signature[0];
    rightPart.y1 <== signature[1];
    rightPart.x2 <== HashMulA.out[0];
    rightPart.y2 <== HashMulA.out[1];
    leftPart.Ax === rightPart.xout;
    leftPart.Ay === rightPart.yout;
}

component main = EdDSAVerifier();