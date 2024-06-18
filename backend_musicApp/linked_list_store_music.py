class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_list(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next is not None:
                last = last.next
            last.next = new_node

    def display_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_list(self, key):
        temp = self.head
        if temp.data == key:
            self.head = temp.next
            temp = None
            return
        else:
            while temp.next is not None:
                print("hello")
                if temp.data == key:
                    temp = temp.next
                    break
        prev = temp
        temp = temp.next
        if temp is None:
            return


if __name__ == "__main__":
    list = LinkedList()
    choice = 0
    while True:
        print(" 1 insert list")
        print(" 2 display list")
        print(" 3 delete list")
        print(" 4 exit")
        choice = int(input("enter your choice"))
        if choice == 1:
            list.insert_list(input("enter a value"))
        elif choice == 2:
            list.display_list()
        elif choice == 3:
            list.delete_list(input("enter the delete value"))
        elif choice == 4:
            break
        else:
            print("invalid choice")
        
