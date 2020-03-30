class Solution {
public:
    vector<vector<string>> findDuplicate(vector<string>& paths) {
        unordered_map<string, vector<string>> umap;
        for (string path: paths) {
            size_t pos = 0;
            string token;
            string delimiter = " ";
            string dir;
            if ((pos = path.find(delimiter)) != string::npos) {
                dir = path.substr(0, pos);
                path.erase(0, pos + delimiter.length());
            }
            vector<string> files;
            while ((pos = path.find(delimiter)) != string::npos) {
                token = path.substr(0, pos);
                files.push_back(token);
                path.erase(0, pos + delimiter.length());
            }
            token = path.substr(0, pos);
            files.push_back(token);
            // map duplicate file content into the same mapped arrays
            for (string file: files) {
                unsigned bgn = file.find('(');
                unsigned end = file.find(')');
                string content = file.substr(bgn+1, end-bgn-1);
                string filename = file.substr(0, bgn);
                umap[content].push_back(dir + "/" + filename);
            }
        }
        
        vector<vector<string>> out;
        for (auto it = umap.begin(); it != umap.end(); ++it) {
            vector<string> vs;
            if (it->second.size() < 2) continue;
            for (string filename :it->second) vs.push_back(filename);
            out.push_back(vs);
        }
        return out;
    }
};
