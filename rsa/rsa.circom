pragma circom 2.1.9



function mod_exp(n, k, a, p, e) {
    var eBits[1024]; // length is k * n
    for (var i = 0; i < k; i++) {
        for (var j = 0; j < n; j++) {
            eBits[j + n * i] = (e[i] >> j) & 1;
        }
    }

    var out[100]; // length is k
    for (var i = 0; i < 100; i++) {
        out[i] = 0;
    }
    out[0] = 1;

    // repeated squaring
    for (var i = k * n - 1; i >= 0; i--) {
        // multiply by a if bit is 0
        if (eBits[i] == 1) {
            var temp[200]; // length 2 * k
            temp = prod(n, k, out, a);
            var temp2[2][100];
            temp2 = long_div(n, k, k, temp, p);
            out = temp2[1];
        }

        // square, unless we're at the end
        if (i > 0) {
            var temp[200]; // length 2 * k
            temp = prod(n, k, out, out);
            var temp2[2][100];
            temp2 = long_div(n, k, k, temp, p);
            out = temp2[1];
        }

    }
    return out;
}

template verifyRSA(k) {
    signal input pk[2*k];
    signal input message;
    signal input signature[k];
    
    signal input e[k];
    signal input n[k];
    for(var i = 0; i < k; i++) {
        e[i] <== pk[i];
        n[i] <== pk[k + i]
    }
    
    sigPowe = mod_exp(64, k, signature, n, e)
    message === sigPowe
}

