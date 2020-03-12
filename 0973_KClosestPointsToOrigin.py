class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        d_list = []
        for x in points:
            d_list.append(x[0]*x[0] + x[1]*x[1])
            
        d_list_sort = sorted(d_list)
        
        out = []
        for i,d in enumerate(d_list):
            if d <= d_list_sort[K-1]:
                out.append(points[i])
                if len(out) == K:
                    break
                
        return out
