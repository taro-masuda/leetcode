class MaxStack {
public:
    /** initialize your data structure here. */
    stack<pair<int,int>> s;
    
    void push(int x) {
        if (!s.empty()) s.push(pair(x, max(x, s.top().second)));
        else s.push(pair(x,x));
    }
    
    int pop() {
        int ans = s.top().first;
        s.pop();
        return ans;
    }
    
    int top() {
        return s.top().first;
    }
    
    int peekMax() {
        return s.top().second;        
    }
    
    int popMax() {
        int ans = s.top().second; 
        stack<pair<int,int>> stmp;
        while (s.top().first != ans) {
            stmp.push(s.top()); s.pop();
        }
        s.pop();
        while (!stmp.empty()) {
            if (!s.empty()) {
                s.push(pair(stmp.top().first, 
                            max(s.top().second, stmp.top().first))); 
            } else s.push(pair(stmp.top().first, stmp.top().first));
            stmp.pop();
        }
        return ans;
    }
};

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack* obj = new MaxStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->peekMax();
 * int param_5 = obj->popMax();
 */
