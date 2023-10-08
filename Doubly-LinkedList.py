class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None
        self.prev  = None

class DoublyLinkedList:
    """
        From scratch Doubly-Linked-List implementation with available methods:
         - print_content to print all values of nodes of DLL.
         - append to append any node at the end of DLL.
         - pop to delete last node in DLL.
         - prepend to add new nodes in beginning of DLL.
         - pop_first to delete first node in DLL.
         - get to fetch any node by index in DLL.
         - set_value to change value of any node by index in DLL.
         - insert to insert new nodes at any position by index in DLL.
         - remove to remove any node at any position by index in DLL.
    """
    def __init__(self, value):
        new_node    = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """
        Adds new node at the end of DLL.

        :param value: value of new added node.
        :return: True if appending process is done else none.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail      = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        """
        Adds new node at the beginning of DLL.
        :param value: value of new added node.
        :return: True if prepending process is done.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.head is None:
            return None
        temp = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        """
        Gets any node by index in DLL.
        :param index: index of required node.
        :return: The node if getting process is done else none.
        """
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        """
        Changes value of any node in DLL by it's index.
        :param index: index of node being changed.
        :param value: new value of node being changed.
        :return: True if setting value process is done else false.
        """
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        """
        Inserts a new node at any position by index in DLL.
        :param index: index in which node will be inserted.
        :param value: value of node being inserted.
        :return: True if inserting process is done else false.
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1

        return True

    def remove(self, index):
        """
        Removes any node by it's index in DLL.
        :param index: index of node being removed.
        :return: The removed node if removing process is done else none.
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = temp.prev = None
        self.length -= 1
        return temp


if __name__ == "__main__":
    DLL = DoublyLinkedList(2)
    DLL.print_list()
    print('*' * 50)
    DLL.append(90)
    DLL.append(80)
    DLL.print_list()
    print('*' * 50)
    DLL.pop()
    DLL.print_list()
    print('*' * 50)
    DLL.prepend(800)
    DLL.print_list()
    print('*' * 50)
    DLL.pop_first()
    DLL.print_list()
    print('*' * 50)