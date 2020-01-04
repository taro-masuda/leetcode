class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        string out = "";
        long numer = (long)numerator;
        long denom = (long)denominator;
        if (numer < 0 && denom > 0) {
            numer *= -1;
            out += "-";
        } else if (numer > 0 && denom < 0) {
            denom *= -1;
            out += "-";
        } else if (numer < 0 && denom < 0) {
            denom *= -1;
            numer *= -1;
        }
        
        long quotient = numer / denom;
        
        /* digit(s) before the decimal point */
        if (quotient > 0) {
            out += to_string(quotient);
        } else {
            out += "0";
        }
        if (numer % denom == 0) return out;
        else out += ".";
        
        numer -= quotient * denom;
        numer *= 10;
        
        /* digit(s) after the decimal point */
        vector<int> v_quotient;
        vector<int> v_residual;
        string after_decimal = "";
        long residual;
        int ind = 0;
        while (true) {
            quotient = numer / denom;
            residual = numer % denom; 
            
            auto i_q = find(v_quotient.begin(), v_quotient.end(), quotient);
            auto i_r = find(v_residual.begin(), v_residual.end(), residual);
            if (i_q != v_quotient.end() && i_r != v_residual.end()) {
                int iq = std::distance(v_quotient.begin(), i_q);
                int ir = std::distance(v_residual.begin(), i_r);
                int idx = -1;
                for (int i = 0; i < v_residual.size(); i++) {
                    if (v_quotient[i] == quotient && v_residual[i] == residual) {
                        idx = i;
                        break;
                    }
                }
                if (idx >= 0) {
                    int i = 0;
                    while (i <= idx-1) {
                        out += after_decimal[i];
                        i++;
                    }
                    out += "(";
                    while (i < after_decimal.size()) {
                        out += after_decimal[i];
                        i++;
                    }
                    out += ")";
                    auto pos = out.find("(0)");
                    if (pos != string::npos) out.replace(pos, out.size(), "");
                    return out;
                } else {
                    after_decimal += to_string(quotient);
                    v_quotient.push_back(quotient);
                    v_residual.push_back(residual);
                }
            } else {
                after_decimal += to_string(quotient);
                v_quotient.push_back(quotient);
                v_residual.push_back(residual);
            }
            numer -= quotient * denom;
            numer *= 10;
        }
        if (numer / denom > 0) out += to_string(numer / denom);
        return out;
    }
};
