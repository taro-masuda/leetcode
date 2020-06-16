class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        combi = []
        if target == 0:
            combi.append([])
        q = []
        for i,candidate in enumerate(candidates):
            if candidate == target:
                combi.append([candidate])
            elif candidate < target:
                q.append((i,[candidate]))
        while len(q) > 0:
            idx, top = q[0]
            sum_top = sum(top)
            if sum_top == target:
                combi.append([top])
            elif sum_top < target:
                for candidate in candidates[idx:]:
                    top_copy = copy.deepcopy(top)
                    if sum_top + candidate == target:
                        top_copy.append(candidate); combi.append(top_copy)
                    elif sum_top + candidate < target:
                        top_copy.append(candidate); q.append((idx, top_copy))
                    idx += 1
            q.pop(0)
        return combi
