class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
        From scratch Linked-List implementation with available methods:
         - print_content to print all values of nodes of LL.
         - append to append any node at the end of LL.
         - pop to delete last node in LL.
         - prepend to add new nodes in beginning of LL.
         - pop_first to delete first node in LL.
         - get to fetch any node by index in LL.
         - set_value to change value of any node by index in LL.
         - insert to insert new nodes at any position by index in LL.
         - remove to remove any node at any position by index in LL.
         - reverse to reverse nodes order in LL.
    """
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_content(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """
        Adds new node at the end of LL.

        :param value: value of new added node.
        :return: True if appending process is done else none.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

        return True

    def pop(self):
        if self.head is None:
            return None

        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = self.tail = None

        return temp

    def prepend(self, value):
        """
        Adds new node at the beginning of LL.
        :param value: value of new added node.
        :return: True if prepending process is done.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

        return True

    def pop_first(self):
        if self.head is None:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp

    def get(self, index):
        """
        Gets any node by index in LL.
        :param index: index of required node.
        :return: The node if getting process is done else none.
        """
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp

    def set_value(self, index, value):
        """
        Changes value of any node in LL by it's index.
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
        Inserts a new node at any position by index in LL.
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
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        """
        Removes any node by it's index in LL.
        :param index: index of node being removed.
        :return: The removed node if removing process is done else none.
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        # after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


if __name__ == "__main__":
    LL = LinkedList(2)
    LL.append(3)
    LL.append(4)
    LL.append(5)
    LL.print_content()
    print('*' * 50)
    LL.reverse()
    LL.print_content()
    print('*' * 50)
