n=1000
limit_sieve = 10000
primes = set()
notPrimes = set()
i = 2
while len(primes)<n:
 if not i in notPrimes:
   primes.add(i);
   for notPrime in range(i*2, limit_sieve, i):
    notPrimes.add(notPrime)
 i+=1
 sum(primes)
