class Solution {
public:
    bool isPrime(int n) {
        if (n < 2 || (n % 2 == 0 && n > 2)) return false;
        for(int i = 2; i * i <= n; i++){
            if (n % i == 0) return false;
        }
        return true;
    }
    
    int countPrimes(int n) {
        int num_prime = 0;
        for(int i = 2; i < n; i++){
            bool is_prime = isPrime(i);
            if (is_prime) num_prime++;
        }
        return num_prime;
    }
};
