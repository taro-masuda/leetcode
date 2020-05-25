class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        if N == 0:
            return []
        dic = {}
        for i in range(N):
            for j in range(i+1,N):
                complement = target - nums[i] - nums[j]
                if complement in dic:
                    dic[complement].append((i,j))
                else:
                    dic[complement] = [(i,j)]
                    
        out = []
        quad = set()
        for i in range(N):
            for j in range(i+1,N):
                added = nums[i] + nums[j]
                if added in dic:
                    for (k,l) in dic[added]:
                        if k == i or k == j or l == i or l == j:
                            continue
                        ind = [nums[i],nums[j],nums[k],nums[l]]
                        ind.sort()
                        if (ind[0],ind[1],ind[2],ind[3]) not in quad:
                            out.append(ind)
                            quad.add((ind[0],ind[1],ind[2],ind[3]))
        return out
