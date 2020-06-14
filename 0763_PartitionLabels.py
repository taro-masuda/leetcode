class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        partition_sizes = []
        i = 0
        while i < len(S):
            c = S[i]
            stt = i
            end = i
            for j in range(i, len(S)):
                if c == S[j]:
                    end = j
            charset = set(list(S[stt:end]))
            for j in range(end,len(S)):
                if S[j] in charset:
                    end = j
                    charset = set(list(S[stt:end]))
            partition_sizes.append(end-stt+1)
            i = end+1
        return partition_sizes
