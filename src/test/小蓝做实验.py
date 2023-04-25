def E_sieve() :
    # 埃氏筛
    for i in range(2, N) :
        if vis[i] == False:
            prime.append(i)
            for j in range(i * i, N, i):
                vis[j] = True


N = int(1e5)
prime = []
vis = [False] * N
E_sieve()
len_prime = len(prime)

def is_prime(num) :
    for i in range(len_prime) :
        if num % prime[i] == 0:
            return False
        else:
            return True

cnt = 0
with open("primes.txt", "r") as f :
    for line in f:
        num = line.rsplit()
        if num <= int(1e8) :
            if is_prime(num) :
                cnt += 1
print(cnt)
