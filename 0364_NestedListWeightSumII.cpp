/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Constructor initializes an empty nested list.
 *     NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     NestedInteger(int value);
 *
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Set this NestedInteger to hold a single integer.
 *     void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     void add(const NestedInteger &ni);
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class Solution {
public:
    vector<pair<int,int>> depthValues(vector<NestedInteger>& nestedList, int depth) {
        vector<pair<int,int>> values; //value, depth
        for (NestedInteger ni : nestedList) {
            if (ni.isInteger()) values.push_back(pair(ni.getInteger(), depth));
            else {
                vector<pair<int,int>> vp = depthValues(ni.getList(), depth+1);
                values.insert(values.end(), vp.begin(), vp.end());
            }
        }
        return values;
    }
    
    int depthSumInverse(vector<NestedInteger>& nestedList) {
        vector<pair<int,int>> values; // value, depth
        for (NestedInteger ni : nestedList) {
            if (ni.isInteger()) values.push_back(pair(ni.getInteger(), 1));
            else {
                vector<pair<int,int>> vp = depthValues(ni.getList(), 2);
                values.insert(values.end(), vp.begin(), vp.end());
            }
        }
        int maxDepth = 0;
        for (pair<int,int> p : values) {
            maxDepth =  max(maxDepth, p.second);
        }
        int out = 0;
        for (pair<int,int> p : values) {
            out += p.first * (maxDepth - p.second + 1);
        }
        return out;
    }
};
