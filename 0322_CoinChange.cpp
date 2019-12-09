class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        sort(coins.begin(), coins.end(), greater<int>());
        if (coins.size() == 0) return -1;
        else if(amount ==0) return 0;
        
        int currentAmount = 0;
        int coinCount = 0;
        int idx = 0;
        while (true){
            if (currentAmount + coins[idx] < amount) {
                if(coinChange(coins, amount-coins[idx]) != -1){
                    currentAmount += coins[idx];
                    coinCount++;
                } else {
                    idx++;
                    if (idx == coins.size()){
                        coinCount = -1;
                        break;
                    }
                }
            } else if (currentAmount + coins[idx] == amount) {
                coinCount++;
                currentAmount = amount;
                break;
            } else {
                idx++;
                if (idx == coins.size()){
                    coinCount = -1;
                    break;
                }
            }
        }
        return coinCount;
    }
};
