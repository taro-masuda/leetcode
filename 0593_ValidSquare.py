class Solution:
    def euclidSquare(self, v1: List[int]) -> int:
        return v1[0]*v1[0] + v1[1]*v1[1]
    
    def product(self, v1: List[int], v2: List[int]) -> int:
        return v1[0]*v2[0] + v1[1]*v2[1]
    
    def same(self, v1, v2) -> bool:
        return v1[0] == v2[0] and v1[1] == v2[1]
    
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if self.same(p1,p2) or self.same(p1,p3) or self.same(p1,p4) or self.same(p2,p3) or self.same(p2,p4) or self.same(p3,p4):
            return False
        
        v1 = [p1[0]-p2[0], p1[1]-p2[1]]
        v2 = [p3[0]-p4[0], p3[1]-p4[1]]
        v3 = [p1[0]-p3[0], p1[1]-p3[1]]
        v4 = [p1[0]-p4[0], p1[1]-p4[1]]
        
        if self.euclidSquare(v1) != self.euclidSquare(v2):
            return False
        else:
            diagonal = self.product(v1, v2) == 0 
            parallel = abs(self.product(v1, v2)) == self.euclidSquare(v1)
            if (not diagonal) and (not parallel):
                return False
            elif diagonal:
                if self.euclidSquare(v3) == self.euclidSquare(v4) and self.product(v3, v4) == 0:
                    return True
                else:
                    return False
            else: # parallel
                if (self.euclidSquare(v1) == self.euclidSquare(v4) and self.product(v1, v4) == 0) \
                    or (self.euclidSquare(v1) == self.euclidSquare(v3) and self.product(v1, v3) == 0):
                    return True
                else:
                    return False
