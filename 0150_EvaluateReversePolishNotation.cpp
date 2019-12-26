class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> nums;
        for (int i = 0; i < tokens.size(); i++){
            if(tokens[i] == "+" || tokens[i] == "-" || tokens[i] == "*" || tokens[i] == "/"){
                int latter = nums.top();
                nums.pop();
                int former = nums.top();
                nums.pop();
                if (tokens[i] == "+") nums.push(former+latter);
                else if (tokens[i] == "-") nums.push(former-latter);
                else if (tokens[i] == "*") nums.push(former*latter);
                else if (tokens[i] == "/") nums.push(former/latter);
            } else {
                nums.push(stoi(tokens[i]));
            }
        }
        return nums.top();
    }
};
