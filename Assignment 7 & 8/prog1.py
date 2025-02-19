# Write a Python program to create a class representing a linked list data structure. Include
# methods for displaying linked list data, inserting and deleting nodes.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert(self, data):#insert at end
        new_node = Node(data)
        if self.head == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next != 0:
                current = current.next
            current.next = new_node

    def delete(self, data):
        if not self.head:
            print("List is empty.")
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        
        if current.next:
            current.next = current.next.next
        else:
            print("Data not found in the list.")


def main():
    ll = LinkedList()
    while True:
        print("\nMenu:")
        print("1. Insert node")
        print("2. Delete node")
        print("3. Display list")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            data = int(input("Enter data to insert: "))
            ll.insert(data)
        elif choice == "2":
            data = int(input("Enter data to delete: "))
            ll.delete(data)
        elif choice == "3":
            ll.display()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
