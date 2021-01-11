from Linked_List import LinkedList

# class Node:
#     def __init__(self, data=None, prev=None, next=None):
#         self.data = data
#         self.prev = prev
#         self.next = next
#
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#
#     def print(self):
#         if self.head is None:
#             print('Doubly linked list is currently empty')
#
#         itr = self.head
#         dlls = ''
#         while itr:
#             dlls = dlls + str(itr.data) + ' <--> '
#             itr = itr.next
#         print(dlls)
#
#     def get_length(self):
#         count = 0
#         itr = self.head
#         while itr:
#             count += 1
#             itr = itr.next
#         return count
#
#     def get_last_node(self):
#         itr = self.head
#         while itr.next:
#             itr = itr.next
#         return itr
#
#     def insert_at_beginning(self, data):
#         node = Node(data, None, self.head)
#         self.head = node
#
#     def insert_at_end(self, data):
#         if self.head is None:
#             self.head = Node(data, None, None)
#             return
#
#         itr = self.head
#         while itr.next:
#             itr = itr.next
#         itr.next = Node(data, itr, None)
#
#     def insert_at(self, data, index):
#         if index < 0 or index > self.get_length():
#             raise Exception('Invalid Index')
#
#         if index == 0:
#             return self.insert_at_beginning(data)
#
#         itr = self.head
#         count = 0
#         while itr:
#             if count == index-1:
#                 node = Node(data, itr, itr.next)
#                 if node.next:
#                     node.next.prev = node
#                 itr.next = node
#                 break
#             itr = itr.next
#             count += 1
#
#     def remove_at(self, index):
#         if index < 0 or index > self.get_length():
#             raise Exception('Invalid Index')
#
#         itr = self.head
#         count = 0
#         while itr:
#             if count == index - 1:
#                 itr.next = itr.next.next
#                 itr.next.prev = itr
#                 break
#             itr = itr.next
#             count += 1
#
#     def insert_after_value(self, after_data, insert_data):
#         itr = self.head
#         while itr:
#             if itr.data == after_data:
#                 node = Node(insert_data, itr, itr.next)
#                 itr.next = node
#                 break
#             itr = itr.next
#
#     def remove_by_value(self, data):
#         if self.head is None:
#             return
#
#         if self.head == data:
#             self.head = self.head.next
#
#         itr = self.head
#         while itr.next:
#             if itr.next.data == data:
#                 itr.next = itr.next.next
#                 break
#             itr = itr.next
#
#     def print_forward(self):
#         itr = self.head
#         frwds= ''
#         while itr:
#             frwds = frwds + str(itr.data) + ' --> '
#             itr = itr.next
#         return print('Doubly Linked List in forward: ', frwds)
#
#     def print_reverse(self):
#         if self.head is None:
#             return print('List is empty')
#
#         last_node = self.get_last_node()
#         itr = last_node
#         revs = ''
#         while itr:
#             revs += str(itr.data) + ' --> '
#             itr = itr.prev
#         return print('Doubly Linked List in reverse: ', revs)






if __name__ == '__main__':
    # dll = DoublyLinkedList()
    # dll.print()
    # dll.insert_at_beginning(30)
    # dll.print()
    # dll.insert_at_beginning(10)
    # dll.print()
    # dll.insert_at_end(40)
    # dll.print()
    # dll.insert_at(20, 1)
    # dll.print()
    # dll.insert_at_end(50)
    # dll.print()
    # dll.insert_at(25,2)
    # dll.print()
    # dll.remove_at(2)
    # dll.print()
    # dll.insert_after_value(40, 45)
    # dll.print()
    # dll.remove_by_value(45)
    # dll.print()
    # dll.print_forward()
    # dll.print_reverse()
    ll = LinkedList()
    ll.insert_values([1, 2, 3, 4, 5, 6])
    ll.print()
    ll.insert_at(2, 200)
    ll.print()