vector<long> SieveOfEratosthenes(long n) {
	vector<bool> sieve((int)n / 2, true);
	for (int i = 3; i < sqrt(n) + 1; i += 2) {
		if (sieve[i / 2]) {
			for (int j = i * i / 2; j < sieve.size(); j += i) {
				sieve[j] = false;
			}
		}
	}
	vector<long> res;
	res.push_back(2);
	for (long i = 1; i < n / 2; i++) {
		if (sieve[i])
			res.push_back(2 * i + 1);
	}
	return res;
}
