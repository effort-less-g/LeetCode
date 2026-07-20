from queue import PriorityQueue

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        queue = PriorityQueue()

        count = 0
        size = len(nums)
        res = nums[0]

        for num in nums:
            # print(num, 'number')
            queue.put(num)
            count += 1
            # print(f"COUNT {count}")
            if k < count:
                res = queue.get()
                # print("RESULT", res)

        # print(count, k)
        res = queue.get()
        # print(res)

        # while not queue.empty():
        #     print(queue.get())

        return res

        # queue.put(nums[-1])
        # queue.put(nums[1])

        # print(queue.get())
     
        
        # queue = [nums[0]]
        # for i in range(1, len(nums)):

        #     # print(queue, nums[i])

        #     if len(queue) >= k and nums[i] < queue[-1]:
        #         # print("PASS")
        #         continue
            
        #     if len(queue) >= k and k != 1:
        #         queue.pop()
        #     elif k == 1:
        #         return max(nums)
            
        #     j = 0
        #     while nums[i] < queue[j]:
        #         j += 1
        #         if j == len(queue):
        #             break
        #     queue.insert(j, nums[i])
                
            

        # # print(queue)
        # return queue[-1]


