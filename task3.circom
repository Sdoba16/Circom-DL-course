pragma circom 2.1.9;

include "node_modules/circomlib/circuits/comparators.circom";

template NoRepetitions() {
    signal input nums[9];
    component isdiff[9][9];
    for (var i = 0; i < 9; i++) {
        for (var j = 0; j < 9; j++) {
            isdiff[i][j] = IsZero();
            isdiff[i][j].in <== nums[i] - nums[j];
            0 === isdiff[i][j].out * (i - j);
        }
    }
}

template InRange(n) {
    signal input lower;
    signal input upper;
    signal input num;

    component checkLower = LessEqThan(n);
    checkLower.in[0] <== lower;
    checkLower.in[1] <== num;

    component checkUpper = LessEqThan(n);
    checkUpper.in[0] <== num;
    checkUpper.in[1] <== upper;
}

template SudokuVerifier() {
    signal input requirement[9][9];
    signal input nums[9][9];
    component inrange[9][9];

    component numstoreq[9][9];
    for(var i = 0; i < 9; i++) {
        for(var j = 0; j < 9; j++) {
            0 === requirement[i][j] * (requirement[i][j] - nums[i][j]);
        }
    }

    for(var i = 0; i < 9; i++) {
        for(var j = 0; j < 9; j++) {
            inrange[i][j] = InRange(4);
            inrange[i][j].lower <== 1;
            inrange[i][j].upper <== 9;
            inrange[i][j].num <== nums[i][j];
        }
    }
    component sumcheck[27];
    component norepetitions[27];
    for(var i = 0; i < 9; i++) {
        norepetitions[i] = NoRepetitions();
        for(var j = 0; j < 9; j++) {
            norepetitions[i].nums[j] <== nums[i][j];
        }
    }
    
    for(var j = 0; j < 9; j++) {
        norepetitions[j+9] = NoRepetitions();
        for(var i = 0; i < 9; i++) {
            norepetitions[j+9].nums[i] <== nums[i][j];
        }
    }
    
    for (var k = 0; k < 3; k++) {
        for (var t = 0; t < 3; t++){
            norepetitions[18+t+3*k] = NoRepetitions();
            for(var i = 0; i < 3; i++) {
                for(var j = 0; j < 3; j++) {
                    norepetitions[18+t+3*k].nums[j+3*i] <== nums[i+3*t][j+3*k];
                }
            }
        }
    }
}

component main{public[requirement]} = SudokuVerifier();