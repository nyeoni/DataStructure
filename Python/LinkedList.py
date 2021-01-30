# LinkedList
# 연결리스트 / 배열과 다르게 연결된 공간에 데이터를 나열
# data와 pointer 로 구성되어 있음 --> Node(data, pointer)
# 미리 데이터 공간을 할당하지 않아도 되지만 연결을 위한 별도의 데이터 공간이 필요하므로 저장효율이 높지않음

class Node:
    def __init__(self, data, next=None):
        # 객체 생성 알아보기
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
            print(self.head.data)
            # 방어코드
        else:
            node = self.head
            while node.next != None:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head == '':
            # 방어코드
            print("해당 값을 가진 노드가 없습니다.")
            return

        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = temp.next
                    del temp
                    return
                else:
                    node = node.next

    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                temp = node.data
                return temp
            else:
                node = node.next

            
if __name__=="__main__":
    linkedlist = NodeMgmt(0)
    for i in range(1,10):
        linkedlist.add(i)
    # 추가 및 출력
    # linkedlist.desc()

    linkedlist.delete(3)
    linkedlist.delete(0)
    linkedlist.delete(9)
    # 삭제 및 출력
    linkedlist.desc()