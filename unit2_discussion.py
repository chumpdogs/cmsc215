"""
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
This example uses network configuration changes and support tickets.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # The newest change is kept at the end and is the first to be undone.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            raise IndexError("Cannot undo a change: the stack is empty.")
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Check the most recent change without undoing it.
        if self.is_empty():
            raise IndexError("Cannot view the last change: the stack is empty.")
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New tickets join at the back; earlier tickets stay at the front.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            raise IndexError("Cannot process a ticket: the queue is empty.")
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Look at the oldest waiting ticket without processing it.
        if self.is_empty():
            raise IndexError("Cannot view the next ticket: the queue is empty.")
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def show_empty_case(description, operation):
    """Show an expected empty-structure error without crashing the program."""
    try:
        print(description, operation())
    except IndexError as error:
        print(description, error)


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.
    print("\n=== STACK: UNDO NETWORK CHANGES ===")
    changes = Stack()
    for change in ["Set hostname", "Create VLAN 32", "Assign port 5 to VLAN 32", "Enable port 5"]:
        changes.push(change)
        print("Applied:", change)
    print("Most recent change:", changes.peek())
    while not changes.is_empty():
        print("Undo:", changes.pop())
    show_empty_case("Pop on empty stack:", changes.pop)
    show_empty_case("Peek on empty stack:", changes.peek)

    single_change = Stack()
    single_change.push("Restart interface")
    print("Single item removed:", single_change.pop())
    print("Single-item stack now empty:", single_change.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.
    print("\n=== QUEUE: NETWORK SUPPORT TICKETS ===")
    tickets = Queue()
    for ticket in ["VPN access", "Printer connectivity", "Switch port down", "Password reset"]:
        tickets.enqueue(ticket)
        print("Ticket received:", ticket)
    print("Next ticket:", tickets.front())
    while not tickets.is_empty():
        print("Ticket handled:", tickets.dequeue())
    show_empty_case("Dequeue on empty queue:", tickets.dequeue)
    show_empty_case("Front on empty queue:", tickets.front)

    single_ticket = Queue()
    single_ticket.enqueue("Check cable")
    print("Single ticket handled:", single_ticket.dequeue())
    print("Single-item queue now empty:", single_ticket.is_empty())


if __name__ == "__main__":
    main()
