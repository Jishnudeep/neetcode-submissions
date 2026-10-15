from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = Counter(nums)

        frequency_items = frequency.most_common()

        result = [x[0] for x in frequency_items]

        return result[:k]