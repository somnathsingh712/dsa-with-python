from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        result = []

        for i in range(len(nums)):

            # Remove indices outside the current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add current index
            dq.append(i)

            # Record the maximum for each complete window
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result