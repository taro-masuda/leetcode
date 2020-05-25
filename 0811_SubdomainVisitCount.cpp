class Solution {
public:
    vector<string> split(string s, string delimiter) {
        vector<string> elements;
        size_t pos = 0;
        while ((pos = s.find(delimiter)) != string::npos) {
            string token = s.substr(0, pos);
            elements.push_back(token);
            s.erase(0, pos + delimiter.length());
        }
        elements.push_back(s);
        return elements;
    }
    
    vector<string> subdomainVisits(vector<string>& cpdomains) {
        int N = cpdomains.size();
        unordered_map<string,int> umap;
        for (int i = 0; i < N; i++) {
            string cpdomain = cpdomains[i];
            vector<string> timesAndDomains = split(cpdomain, " ");
            int time = stoi(timesAndDomains[0]);
            string domains = timesAndDomains[1];
            vector<string> domainDots = split(domains, ".");
            int subdomainNum = domainDots.size();
            for (int j = 0; j < subdomainNum; j++) {
                string domain = "";
                for (int k = j; k < subdomainNum; k++) {
                    domain += domainDots[k];
                    if (k < subdomainNum -1) domain += ".";
                }
                if (umap.find(domain) != umap.end()) umap[domain] += time;
                else umap[domain] = time;
            }
        }
        vector<string> out;
        for (auto it = umap.begin(); it != umap.end(); ++it) {
            out.push_back(to_string(it->second) + " "+ it->first);
        }
        
        return out;
    }
};
