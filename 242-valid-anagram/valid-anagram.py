from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 2
        # return Counter(t) == Counter(s) 

        # Solution 3 TC: O(n) SC: O(1)
        if len(s) != len(t):
            return False
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        for c in t:
            count[ord(c) - ord('a')] -= 1

        return all(c == 0 for c in count)
        
        # Solution 4
        # Solution 1
        # dic = {}
        # dic2 = {}
        # if len(s) != len(t):
        #     return False
        # # first method for storing value in dictionary
        # for i in range(len(s)):
        #     if s[i] in dic:
        #         dic[s[i]]+=1
        #     else:
        #         dic[s[i]] = 1
                
        # # second method for storing value in dictionary
        # for i in range(len(t)):
        #     dic2[t[i]] = 1+dic2.get(t[i],0)

        # for key, val in dic.items():
        #     if key in dic2:
        #         if dic[key] == dic2[key]:
        #             continue
        #         else:
        #             return False
        #     else:
        #         return False
        # return True

        set1 = {}
        set2 = {}

        for s1 in s:
            if s1 in set1:
                set1[s1] += 1
            else:
                set1[s1] = 1
        for s2 in t:
            if s2 in set2:
                set2[s2] += 1
            else:
                set2[s2] = 1
        
        for s1 in set1:
            if set1[s1] != set2[s1]:
                return False
        return True