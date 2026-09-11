class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        bucket={}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
            
        bucket = [[]for _ in range(len(nums)+1)]
        for num, freq in seen.items():
            bucket[freq].append(num)
        result= []
        for freq in range(len(bucket)-1,0,-1):
            for num in bucket[freq]:
                result.append(num)
                if len(result)==k:
                    return result
                    
