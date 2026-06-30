class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        
        def heapSort(arr):
            for i in range(n//2-1,-1,-1):
                heapify(arr,n,i)
            for i in range(n-1,0,-1):
                arr[0],arr[i]=arr[i],arr[0]
                heapify(arr,i,0)   
        def heapify(arr,n,i):
            left=2*i+1;right=2*i+2
            largest=i
            if left<n and arr[left]>arr[largest]:
                largest=left
            if right<n and arr[right]>arr[largest]:
                largest=right
            if largest!=i:
                arr[i],arr[largest]=arr[largest],arr[i]
                heapify(arr,n,largest)
        heapSort(nums)
        return nums