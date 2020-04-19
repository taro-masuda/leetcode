class Solution {
public:
    string intToRoman(int num) {
        string roman = "";
        int thousands = num / 1000;
        if (thousands > 0) {
            for (int i = 0; i < thousands; i++) roman += 'M';
        }
        int hundreds = (num - thousands*1000) / 100;
        if (hundreds == 5) roman += 'D';
        else if (hundreds == 4) roman += "CD";
        else if (hundreds == 9) roman += "CM";
        else if (hundreds >= 6) {
            roman += 'D';
            for (int i = 0; i < hundreds - 5; i++) roman += 'C'; 
        } else {
            for (int i = 0; i < hundreds; i++) roman += 'C';
        }
        int tens = (num - thousands*1000 - hundreds*100) / 10;
        if (tens == 5) roman += 'L';
        else if (tens == 4) roman += "XL";
        else if (tens == 9) roman += "XC";
        else if (tens >= 6) {
            roman += 'L';
            for (int i = 0; i < tens - 5; i++) roman += 'X';
        } else {
            for (int i = 0; i < tens; i++) roman += 'X';
        }
        int ones = num % 10;
        if (ones == 5) roman += 'V';
        else if (ones == 4) roman += "IV";
        else if (ones == 9) roman += "IX";
        else if (ones >= 6) {
            roman += 'V';
            for (int i = 0; i < ones - 5; i++) roman += 'I';
        } else {
            for (int i = 0; i < ones; i++) roman += 'I';
        }
        return roman;
    }
};
