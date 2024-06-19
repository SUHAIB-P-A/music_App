class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

# INSERTING
    def insert_list(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next is not None:
                last = last.next
            last.next = new_node

# DISPLAY
    def display_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# DELETE
    def delete_list(self, key):
        temp = self.head
        # assume the delete elament is the first element in the list
        if temp.data == key:
            self.head = temp.next
            temp = None
            return
        # search the delete element for the list
        else:
            while temp.next is not None:
                if temp.data == key:
                    break
                prev = temp
                temp = temp.next
        if temp is None:
            return
# joining list
        prev.next = temp.next
        temp = None

# SEARCHING
    def searchlist(self, key):
        counter = 1
        temp = self.head
        # assume first element
        if temp.data == key:
            print("iteam ("+temp.data+") found, at the position "+str(counter))
            return
        # search for the key element
        else:
            while temp.next is not None:
                if temp.data == key:
                    print("iteam ("+temp.data+") found, at the position "+str(counter))
                    break
                counter += 1
                prev = temp
                temp = temp.next
        if temp is None:
            return


if __name__ == "__main__":
    list = LinkedList()
    choice = 0
    while True:
        print(" 1 Insert list")
        print(" 2 Display list")
        print(" 3 Delete list")
        print(" 4 Search")
        print(" 5 Exit")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            list.insert_list(input("Enter a value : "))
        elif choice == 2:
            list.display_list()
        elif choice == 3:
            list.delete_list(input("Enter the delete value : "))
        elif choice == 4:
            list.searchlist(input("Enter the search element : "))
        elif choice == 5:
            break
        else:
            print("invalid choice")
