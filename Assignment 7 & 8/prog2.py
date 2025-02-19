# Write a Python program to create a class representing a queue data structure. Include methods
# for enqueueing and dequeuing elements.
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} enqueued into the queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        item = self.queue.pop(0)
        print(f"{item} dequeued from the queue.")
        return item

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue contents:", self.queue)

# Taking user input
def main():
    q = Queue()
    while True:
        print("\nMenu:")
        print("1. Enqueue element")
        print("2. Dequeue element")
        print("3. Display queue")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            item = input("Enter element to enqueue: ")
            q.enqueue(item)
        elif choice == "2":
            q.dequeue()
        elif choice == "3":
            q.display()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()