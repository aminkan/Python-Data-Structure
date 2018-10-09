
class Node(object):

    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, data):
        self.size += 1
        if not self.head:
            self.head = Node(data)
        else:
            temp_node = self.head
            while temp_node.next_node is not None:
                temp_node = temp_node.next_node
            new_node = Node(data)
            temp_node.next_node = new_node
            new_node.prev_node = temp_node

    def delete(self, data):
        temp_node = self.head
        flag = False
        while temp_node.next_node is not None:
            if temp_node.data == data:
                temp_node.prev_node.next_node = temp_node.next_node
                temp_node.next_node.prev_node = temp_node.prev_node
                flag = True
                break
            else:
                temp_node = temp_node.next_node

        if not flag:
            print("there is nothing in the LinkList with this data")

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def loc(self, data):
        temp_node = self.head
        loc = 0
        flag = False
        while temp_node.next_node is not None:
            if temp_node.data == data:
                flag = True
                break
            else:
                loc += 1
                temp_node = temp_node.next_node

        if flag:
            return loc

        else:
            print("there is nothing in the LinkList with this data")
    def index(self, i):
        try:
            temp_node = self.head
            for j in range(i):
                temp_node = temp_node.next_node
            return temp_node.data
        except Exception:
            print("Index Error")
    def list(self, index= None):
        if index == None:
            return [self.index(i) for i in range(self.size)]
        else:
            try:
                if index > self.size:
                    raise Exception
                else:
                    return [self.index(i) for i in range(index)]
            except Exception:
                print("Index Error")


