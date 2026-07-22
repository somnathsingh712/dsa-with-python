from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        # Count frequency of each element
        freq = Counter(nums)

        # Return k elements with highest frequency
        return heapq.nlargest(k, freq.keys(), key=freq.get)