from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Solution 3 TC = O(n)
        hasMap = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            hasMap[tuple(count)].append(s)
        return list(hasMap.values())


        # Solution 2 TC: O(k⋅nlogn) SC: O(\U0001d458⋅\U0001d45b)
        # anagrams = defaultdict(list)
        # for word in strs:
        #     # Sort the word and use it as the key
        #     sorted_word = ''.join(sorted(word))
        #     anagrams[sorted_word].append(word)
        # # Convert the dictionary values to a list
        # return list(anagrams.values())
       
        # Solution 1. TC: O(L) SC: O(L)
        # def createKey(word):
        #     temp = [0]*26
        #     for ch in word:
        #         index = ord(ch) - ord('a')
        #         temp [index]+=1
        #     return temp

        # dic = dict()
        # for word in strs:
        #     key = createKey(word)
        #     if tuple(key) in dic:
        #         dic[tuple (key) ].append (word)
        #     else:           
        #         dic[tuple(key)] = [word]
        # res = []

        # for key , value in dic.items () :
        #     res. append (value)
        # return res