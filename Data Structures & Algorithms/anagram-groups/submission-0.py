class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_hash = {}

        for i, strs in enumerate(strs):
            letter_list = []
            for char in strs: 
                letter_list.append(char)
            
            letter_list = sorted(letter_list)
            new_word = "".join(letter_list)
            if new_word not in word_hash:
                word_hash[new_word] = []
                word_hash[new_word].append(strs)
            else:
                word_hash[new_word].append(strs)

        print(word_hash)
        return [x for x in word_hash.values()]

