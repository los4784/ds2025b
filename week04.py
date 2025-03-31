class Node:
    def __init__ (self, data, link=None):
        self.data = data
        self.link = link


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if not self.head:   # 링크리스트가 노드가 하나도 없는 상태면
            self.head = Node(data)  #  새 노드를 head 연결
            return
        current = self.head # current변수 선언, self.head값을 받음
        while current.link:
            current = current.link  # 다음노드를 이용
        current.link = Node(data)

    def __str__(self):  #
        node = self.head
        while node is not None:
            out_texts = out_texts + f"{node.data} +  -> "
            node = node.link
        return out_texts  + "end"

ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)