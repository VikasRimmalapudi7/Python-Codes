from queue import PriorityQueue
nums=[5,3,56,2,6,1]
q=PriorityQueue(nums)

while q:
    item=q.get()
    print(item)