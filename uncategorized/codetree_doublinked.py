N, M = map(int, input().split())
knight = list(map(int, input().split()))
call = [int(input()) for _ in range(M)]

# Please write your code here.
node_map = {}
class Node :
    def __init__(self, value, prev, next) :
        self.value = value 
        self.prev = prev 
        self.next = next 
    
head = Node(None,None,None)
tail = Node(None,head,None)
head.next = tail 

# for k in knight :
for k in knight : 
    new_node = Node(k,None,None)
    temp = tail.prev 
    new_node.next=tail 
    tail.prev = new_node 
    temp.next = new_node 
    new_node.prev = temp
    node_map[k] = new_node

head.next.prev = tail.prev
tail.prev.next = head.next 

for c in call :
    pointer = node_map[c]
    
    print(pointer.next.value, pointer.prev.value)

    pointer.next.prev = pointer.prev 
    pointer.prev.next = pointer.next
    
    










