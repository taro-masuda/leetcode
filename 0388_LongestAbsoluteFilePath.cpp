class Solution {
public:
    int lengthLongestPath(string input) {
        vector<int> dirLength;
        vector<string> inputList;
        string delimiter = "\n";
        string token;
        size_t pos = 0;
        int maxCount = 0;
        while ((pos = input.find(delimiter)) != string::npos) {
            token = input.substr(0, pos);
            input.erase(0, pos + delimiter.length());
            inputList.push_back(token);
        }
        inputList.push_back(input);
        
        for (int i = 0; i < inputList.size(); i++) {
            string in = inputList[i];
            int cnt = std::count(in.cbegin(), in.cend(), '\t');
            if (in.find(".") == string::npos) {
                if (dirLength.size() <= cnt) dirLength.push_back(in.size() - cnt + 1); 
                else dirLength[cnt] = in.size() - cnt + 1;
            } else {
                int length = 0;
                for (int j = 0; j < cnt; j++) length += dirLength[j];
                length += in.size() - cnt;
                if (maxCount < length) maxCount = length;
            }
        }   
        return maxCount;
    }
};
