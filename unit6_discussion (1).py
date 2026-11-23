"""
=================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
=================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.
=================================================
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ==============================
    # TODO (Student): CREATE A HASH TABLE
    # ==============================
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.
    print("\n=== CREATE A HASH TABLE ===")

    # Ticket numbers are unique keys. Their descriptions are the values.
    # Python's dictionary hashes keys so it can find their associated values
    # efficiently, rather than searching a list entry by entry.
    tickets = {}
    tickets["INC1001"] = "Open: Password reset"
    tickets["INC1002"] = "Open: Printer not connecting"
    tickets["INC1003"] = "Open: Account locked"
    tickets["INC1004"] = "Open: Software installation"
    tickets["INC1005"] = "Open: Network outage"

    for ticket_id, description in tickets.items():
        print(f"{ticket_id}: {description}")

    # ==============================
    # TODO (Student): LOOKUP OPERATIONS
    # ==============================
    # Look up existing and missing keys, and explain the result.
    print("\n=== LOOKUP OPERATIONS ===")
    print("INC1003:", tickets.get("INC1003", "Ticket not found"))
    print("INC9999:", tickets.get("INC9999", "Ticket not found"))
    # get() lets us check for a missing key without triggering KeyError.

    # ==============================
    # TODO (Student): UPDATE OPERATIONS
    # ==============================
    # Update a ticket value while keeping the same key.
    print("\n=== UPDATE OPERATIONS ===")
    print("Before update:", tickets["INC1001"])
    tickets["INC1001"] = "Resolved: Password reset"
    print("After update:", tickets["INC1001"])
    # Assigning to an existing key replaces that key's value.

    # ==============================
    # TODO (Student): DELETE OPERATIONS
    # ==============================
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.
    print("\n=== DELETE OPERATIONS ===")
    print("Before deletion:", tickets)
    removed = tickets.pop("INC1005", None)
    print("Removed:", removed)
    print("After deletion:", tickets)
    # Removing a key also removes its value from the dictionary.

    # ==============================
    # TODO (Student): EDGE CASES
    # ==============================
    # Demonstrate at least two edge cases.
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    # Explain what happens in each case.
    print("\n=== EDGE CASES ===")
    print("Missing ticket:", tickets.get("INC9999", "Ticket not found"))
    # get() returns the default message instead of raising KeyError.

    missing_removed = tickets.pop("INC9999", None)
    print("Delete nonexistent ticket:", missing_removed)
    # pop(key, None) safely returns None if the key is missing.

    tickets["INC1006"] = "Open: New laptop setup"
    print("New ticket added through assignment:", tickets["INC1006"])
    # Assigning a value to a previously missing key inserts a new entry.

    empty_tickets = {}
    print("Lookup in an empty dictionary:",
          empty_tickets.get("INC1001", "Ticket not found"))

    # ==============================
    # TODO (Student): COLLISIONS AND PERFORMANCE
    # ==============================
    # A collision occurs if two different keys map to the same hash bucket.
    # Python dictionaries handle collisions internally; their lookup,
    # insertion, and removal are O(1) on average, but can slow with many
    # collisions and may require resizing as the dictionary grows.
    print("\n=== COLLISION EXAMPLE ===")
    bucket_count = 5
    ticket_a, ticket_b = 101, 106
    print(f"Ticket {ticket_a} sample bucket: {ticket_a % bucket_count}")
    print(f"Ticket {ticket_b} sample bucket: {ticket_b % bucket_count}")
    print("Both map to the same bucket in this simple demonstration.")
    # The modulo example is illustrative; it is not Python's actual
    # dictionary hashing algorithm or collision resolution mechanism.


if __name__ == "__main__":
    main()
