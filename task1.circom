pragma circom 2.1.9;

template Multiply() {
    signal input in1;
    signal input in2;

    signal output out;
    
    out <== in1 * in2;
}

template CheckEquation() {
    signal input a;
    signal input b;
    signal input N;

    component a_sq = Multiply();
    a_sq.in1 <== a;
    a_sq.in2 <== a;

    component a_4pow = Multiply();
    a_4pow.in1 <== a_sq.out;
    a_4pow.in2 <== a_sq.out;

    component a_6pow = Multiply();
    a_6pow.in1 <== a_4pow.out;
    a_6pow.in2 <== a_sq.out;

    component b7_a_sq_plus_b = Multiply();
    b7_a_sq_plus_b.in1 <== 7 * b;
    b7_a_sq_plus_b.in2 <== a_sq.out + b;

    a_6pow.out + b7_a_sq_plus_b.out + 42 === N;
}


component main {public[N]}= CheckEquation(); 