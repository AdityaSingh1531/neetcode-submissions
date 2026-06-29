class Node:
    def __init__(self,key,val):
        self.a = [key,val]
        self.next=None
class MyHashMap:

    def __init__(self):
        self.hash=[Node(0,0) for i in range(10000)]
    def put(self, key: int, value: int) -> None:
        cur = self.hash[key%10000]
        while cur.next:
            if cur.next.a[0] == key:
                cur.next.a[1]=value
                return 
            cur=cur.next
        cur.next=Node(key,value)

    def get(self, key: int) -> int:
        cur = self.hash[key%10000]
        while cur.next:
            if cur.next.a[0] == key:
                return cur.next.a[1]
            cur=cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.hash[key%10000]
        while cur.next:
            if cur.next.a[0] == key:
                cur.next=cur.next.next
                return
            cur=cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)