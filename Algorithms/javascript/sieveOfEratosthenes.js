function sieveOfEratosthenes(c) {
    let a=[], i, j, b=[];
    for (i = 2; i <= c; ++i) {
        if (!a[i]) {
            b.push(i);
            for (j = i << 1; j <= c; j += i) {
                a[j] = true;
            }
        }
    }
    return b;
}

module.exports.sieveOfEratosthenes = sieveOfEratosthenes;
