class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def max_heap(i):
            left = 2*i + 1
            right = left + 1
            largest = i
            
            if left < len(stones) and stones[left] > stones[largest]:
                largest = left
            if right < len(stones) and stones[right] > stones[largest]:
                largest = right
                
            if largest != i:
                stones[largest], stones[i] = stones[i], stones[largest]
                max_heap(largest)
        
        def build():
            for i in range(len(stones)//2, -1, -1):
                max_heap(i)
                
        def pop():
            x = stones[0]
            stones[:] = stones[1:]
            build()
            return x
        
        build()
        print(stones)
        
        while len(stones) > 1:
            first = pop()
            second = pop()
            stones.append(first-second)
            build()
            
            
        return stones[0]