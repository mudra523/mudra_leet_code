class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        w_len = len(words[0])
        total_len = w_len * len(words)
        w_count = {}

        for w in words:
            w_count[w] = w_count.get(w, 0) + 1

        res = []

        for i in range(len(s) - total_len + 1):
            seen_words = {}
            j = 0
            while j < len(words):
                w_index = i + j * w_len
                word = s[w_index:w_index + w_len]
                if word not in w_count:
                    break
                seen_words[word] = seen_words.get(word, 0) + 1
                if seen_words[word] > w_count[word]:
                    break

                j += 1
            if j == len(words):
                res.append(i)

        return res            
