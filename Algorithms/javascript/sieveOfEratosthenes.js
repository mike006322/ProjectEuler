function sieveOfEratosthenes(n) {
    //returns array of primes up to n
    let sieve=[], i, j, res=[];
    for (i = 2; i <= n; ++i) {
        if (!sieve[i]) {
            res.push(i);
            for (j = i << 1; j <= n; j += i) {
                sieve[j] = true;
            }
        }
    }
    return res;
}

module.exports.sieveOfEratosthenes = sieveOfEratosthenes;
