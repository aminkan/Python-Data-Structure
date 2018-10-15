""""
created by: aminkan

10/16/2018
"""
class Node(object):

    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None

class LinkedList(object):

    def __init__(self):
        self.__head = None
        self.__size = 0

    def size(self):
        return self.__size + 1

    def insert(self, data):
        self.__size += 1
        if not self.__head:
            self.__head = Node(data)
        else:
            temp_node = self.__head
            while temp_node.next_node is not None:
                temp_node = temp_node.next_node
            new_node = Node(data)
            temp_node.next_node = new_node
            new_node.prev_node = temp_node

    def delete(self, data):
        temp_node = self.__head
        flag = False
        while temp_node is not None:
            if temp_node.data == data:
                if temp_node.next_node is not None and temp_node.prev_node is not None:
                    temp_node.prev_node.next_node = temp_node.next_node
                    temp_node.next_node.prev_node = temp_node.prev_node
                elif temp_node.next_node is None and temp_node.prev_node is not None:
                    temp_node.prev_node.next_node = None
                elif temp_node.prev_node is None and temp_node.next_node is not None:
                    temp_node.next_node.prev_node = None
                    self.__head = temp_node.next_node
                self.__size -= 1
                flag = True
                break
            else:
                temp_node = temp_node.next_node

        if not flag:
            print("there is nothing in the LinkList with this data")


    def delete_index(self, index):
        if index > self.__size:
            print("Index Error")
        else:
            temp_node = self.__head
            for i in range(index):
                temp_node = temp_node.next_node
            if temp_node.next_node is not None and temp_node.prev_node is not None:
                temp_node.prev_node.next_node = temp_node.next_node
                temp_node.next_node.prev_node = temp_node.prev_node
            elif temp_node.next_node is None and temp_node.prev_node is not None:
                temp_node.prev_node.next_node = None
            elif temp_node.prev_node is None and temp_node.next_node is not None:
                temp_node.next_node.prev_node = None
                self.__head = temp_node.next_node


            self.__size -= 1
    def insert_head(self, data):
        self.__size += 1
        new_node = Node(data)
        new_node.next_node = self.__head
        self.__head = new_node

    def loc(self, data):
        temp_node = self.__head
        loc = 0
        flag = False
        while temp_node is not None:
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
            temp_node = self.__head
            for j in range(i):
                temp_node = temp_node.next_node
            return temp_node.data
        except Exception:
            print("Index Error")
    def list(self, index= 0):
        l = []
        if index == 0:
            return [self.index(i) for i in range(self.__size)]
        if index > 0 and index <= self.__size:
            return [self.index(i) for i in range(index)]
        else:
            print("Index Error")




