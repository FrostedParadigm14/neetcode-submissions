import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for i in range(k, len(nums)):
            if heap[0] < nums[i]:
                heapq.heapreplace(heap, nums[i])

        return heapq.heappop(heap)