# DoubleLinkedList
# 검색 프로세스의 개선
# 노드 포인터터 앞뒤로 있다
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search_from_head(self, data):
        if self.head == None:
            return False
            #방어코드

        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    def search_from_tail(self, data):
        if self.head == None:
            return False

        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False

    def insert_before(self, data, before_data):
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node == None:
                    print("before_data와 일치하는 Node가 없습니다")
                    return False
            new = Node(data)
            before_new = node.prev
            if before_new == None:
                self.head = new
            else:
                before_new.next = new
            new.prev = before_new
            new.next = node
            node.prev = new

            return True

    def insert_after(self, data, after_data):
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.head
            while node.data != after_data:
                node = node.next
                if node == None:
                    print("after_data와 일치하는 Node가 없습니다")
                    return False
            new = Node(data)
            after_new = node.next
            if new.next == None:
                self.tail = new
            else:
                after_new.prev = new
            new.next = after_new
            new.prev = node
            node.next = new

            return True

if __name__=="__main__":
    double_linked_list = NodeMgmt(0)
    for i in range(1, 10):
        double_linked_list.insert(i)

    double_linked_list.insert_before(-1, 0) #before head insert data
    double_linked_list.insert_before(1.5, 2)
    double_linked_list.insert_after(2.5, 2)
    double_linked_list.insert_after(10, 9) #after tail insert data
    
    double_linked_list.desc()
