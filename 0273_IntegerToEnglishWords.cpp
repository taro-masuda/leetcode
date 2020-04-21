class Solution {
public:
    string ones[10] = {"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"};
    string eles[10] = {"Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", 
                       "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty"};
    string tys[9] = {"", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    
    string hundredsToWords(int num) {
        string ans = "";
        int hundreds = num / 100;
        if (hundreds > 0) {
            ans += ones[hundreds-1] + " Hundred ";
        }
        int tens = num % 100;
        if (tens > 20) {
            ans += tys[tens/10-1] + " ";
            if (tens%10 > 0) ans += ones[tens%10-1];
        } else if (tens > 10) {
            ans += eles[tens-11];
        } else if (tens > 0) {
            ans += ones[tens-1];
        }
        if (ans[ans.size()-1] == ' ') ans.erase(ans.end()-1);
        return ans;
    }
    string numberToWords(int num) {
        string ans = "";
        if (num == 0) return "Zero";
        if (num >= 1e9 && num < 2e9) ans += "One Billion ";
        else if (num >= 2e9) ans += "Two Billion ";
        int millions = (num / (int)1e6) % 1000;
        if (millions > 0) ans += hundredsToWords(millions) + " Million ";
        int thousands = ((num - millions*(int)1e6) / 1000) % 1000;
        if (thousands > 0) ans += hundredsToWords(thousands) += " Thousand ";
        int hundreds = num % 1000;
        if (hundreds > 0) ans += hundredsToWords(hundreds);
        if (ans[ans.size()-1] == ' ') ans.erase(ans.end()-1);
        return ans;
    }
};
