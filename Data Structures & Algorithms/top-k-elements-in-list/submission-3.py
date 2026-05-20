class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_set = {}
        for i, num in enumerate(nums):
            if num not in hash_set: 
                hash_set[num] = 1
            else:
                hash_set[num] += 1
        
        sorted_hash_set = dict(sorted(hash_set.items(), reverse=True, key=lambda item: item[1]))
        return list(sorted_hash_set.keys())[:k]
