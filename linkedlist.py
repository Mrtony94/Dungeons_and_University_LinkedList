class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def add_last(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = Node(data)

    def find(self, data):
        n = self.head
        if not n:
            return None
        else:
            found = False
            while n is not None and not found:
                if n.data == data:
                    found = True
                n = n.next
            return found

    def find_all(self, data):
        n = self.head
        if not n:
            return None
        else:
            list_results = []
            while n is not None:
                if n.data == data:
                    list_results.append(n.data)
                n = n.next
            return list_results

    def delete(self, data):
        if self.head is None:
            print("List is empty so no element was deleted.")
        else:
            n = self.head
            n_prev = None
            found = False
            while n is not None and not found:
                if n.data == data:
                    if n_prev is None:
                        self.head = n.next
                    elif n.next is None:
                        n_prev.next = None
                    else:
                        n_prev.next = n.next
                    found = True
                n_prev = n
                n = n.next

    @staticmethod
    def iterate_backwards(node):
        if node.next:
            LinkedList.iterate_backwards(node.next)
        print(node.data)

    def print_backwards_v2(self):
        if self.head is None:
            print("List is empty.")
        else:
            LinkedList.iterate_backwards(self.head)

    def print_backwards(self):
        if self.head is None:
            print("List is empty")
        else:
            new_list = []
            n = self.head
            while n is not None:
                new_list.append(n.data)
                n = n.next
            for e in reversed(new_list):
                print(e)

    def delete_all(self, data):
        if self.head is None:
            print("List is empty so no element was deleted.")
        else:
            n = self.head
            n_prev = None
            found = False
            while n is not None:
                if n.data == data:
                    if n_prev is None:
                        self.head = n.next
                    elif n.next is None:
                        n_prev.next = None
                    else:
                        n_prev.next = n.next
                n_prev = n
                n = n.next

    def print_linked_list(self):
        n = self.head
        player = 1
        if not n:
            print("Linked list is empty")
        else:
            while n is not None:
                print(f"User {player}: {n.data}")
                n = n.next
                player += 1

    def size(self):
        count = 0
        if self.head is not None:
            n = self.head
            while n is not None:
                count += 1
                n = n.next
        return count
