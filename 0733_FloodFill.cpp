class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        int R = image.size(); int C = image[0].size();
        stack<pair<int, int>> s;
        s.push(pair(sr, sc));
        set<pair<int,int>> visited;
        visited.insert(pair(sr,sc));
        int prevColor = image[sr][sc];
        // Depth First Search
        while(!s.empty()) {
            pair<int,int> topVal = s.top(); s.pop();
            int r = topVal.first;
            int c = topVal.second;
            image[r][c] = newColor;
            // top
            if (r > 0) {
                if (visited.find(pair(r-1,c)) == visited.end() && image[r-1][c] == prevColor) {
                    s.push(pair(r-1,c));
                    visited.insert(pair(r-1,c));
                }
            }
            // bottom
            if (r < R-1) {
                if (visited.find(pair(r+1,c)) == visited.end() && image[r+1][c] == prevColor) {
                    s.push(pair(r+1,c));
                    visited.insert(pair(r+1,c));
                }
            }
            // left
            if (c > 0) {
                if (visited.find(pair(r,c-1)) == visited.end() && image[r][c-1] == prevColor) {
                    s.push(pair(r,c-1));
                    visited.insert(pair(r,c-1));
                }
            }
            // right
            if (c < C-1) {
                if (visited.find(pair(r,c+1)) == visited.end() && image[r][c+1] == prevColor) {
                    s.push(pair(r,c+1));
                    visited.insert(pair(r,c+1));
                }
            }
        }
        return image;
    }
};
