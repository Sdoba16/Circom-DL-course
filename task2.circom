pragma circom 2.1.9;

include "node_modules/circomlib/circuits/poseidon.circom";

template Poseidon3() {
    signal input a;
    signal input b;
    signal input c;
    signal input N;

    component pos_abc = Poseidon(3);
    pos_abc.inputs[0] <== a;
    pos_abc.inputs[1] <== b;
    pos_abc.inputs[2] <== c;

    N === pos_abc.out;
}

component main {public[N]} = Poseidon3();