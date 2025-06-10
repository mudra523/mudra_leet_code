class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]

            sentances = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    for sub in dfs(end):
                        if sub:
                            sentances.append(word + " " + sub)
                        else:
                            sentances.append(word)
            memo[start] = sentances
            return sentances
        return dfs(0)            