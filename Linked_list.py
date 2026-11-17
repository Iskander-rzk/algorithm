class LinkedList:
    class __Node:
        def __init__(self, value):
            self.value = value
            self.next = None

        def __repr__(self):
            return f"value={self.value}"

    def __init__(self):
        self.__head = None
        self.__tail = None

    def add_first(self, value):
        new_node = self.__Node(value)
        if self.__is_empty():
            self.__initialize(new_node)
        else:
            new_node.next = self.__head
            self.__head = new_node

    def add_last(self, value):
        new_node = self.__Node(value)
        if self.__is_empty():
            self.__initialize(new_node)
        else:
            self.__tail.next = new_node
            self.__tail = new_node

    def remove_first(self):
        if self.__is_empty():
            raise ValueError("Cannot remove an element from empty list")

        removed_value = self.__head.value

        if self.__has_one_node():
            self.__reset()
        else:
            next = self.__head.next
            self.__head.next = None
            self.__head = next

        return removed_value

    def remove_last(self):
        if self.__is_empty():
            raise ValueError("Cannot remove an element from empty list")

        removed_value = self.__tail.value

        if self.__has_one_node():
            self.__reset()
        else:
            last = self.__get_note_before_last()
            last.next = None
            self.__tail = last

        return removed_value

    def remove(self, value):
        if self.__is_empty():
            raise ValueError("Cannot remove an element from empty list")

        if self.__head.value == value:
            self.remove_first()
            return

        if self.__tail.value == value:
            self.remove_last()
            return

        current = self.__head
        prev = self.__head

        while current.next:
            if current.value == value:
                prev.next = current.next
                current.next = None
                return

            prev = current
            current = current.next

        raise ValueError("Value not found in this list")

    def get_nth_from_end(self, n):
        if self.__is_empty():
            raise ValueError("LinkedList is empty")

        if n <= 0:
            raise ValueError("Invalid value of n")

        prev = self.__head
        current = self.__head

        for _ in range(n):
            if current is None:
                raise ValueError("n is larger than the size of list")
            current = current.next

        while current:
            current = current.next
            prev = prev.next

        return prev.value



    def __get_note_before_last(self):
        if self.__is_empty() or self.__has_one_node():
            return None

        current = self.__head
        while current.next != self.__tail:
            current = current.next

        return current

    def __has_one_node(self):
        return self.__head == self.__tail

    def __reset(self):
        self.__head = self.tail = None

    def __is_empty(self):
        return self.__head is None

    def __initialize(self, node):
        self.__head = self.__tail = node





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        num = ListNode(0)
        current = num
        n = 0
        while l1 is not None or l2 is not None or n != 0:
            if l1:
                n1 = l1.val
            else:
                n1 = 0
            if l2:
                n2 = l2.val
            else:
                n2 = 0
            Sum = n1 + n2 + n
            newNode = ListNode(Sum % 10)
            n = Sum // 10
            current.next = newNode
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return num.next

'''