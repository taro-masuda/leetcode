class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        
        card_dict_count = {}
        intmax = 0
        intmin = 10**10
        for h in hand:
            if intmax < h:
                intmax = h
            if intmin > h:
                intmin = h
            if h in card_dict_count:
                card_dict_count[h] += 1
            else:
                card_dict_count[h] = 1
        
        for i in range(intmin, intmax+1):
            if not i in card_dict_count:
                continue
            while card_dict_count[i] > 0:
                for j in range(i, i+W):
                    if j > intmax:
                        return False
                    if not j in card_dict_count:
                        return False
                    else:
                        card_dict_count[j] -= 1
        
        return True
