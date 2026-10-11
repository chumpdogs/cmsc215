# Unit 2 Discussion: Stacks and Queues

## Overview

I completed the starter Python program by implementing a stack and a queue and testing both with examples related to network support. I kept the original TODO prompts in the code and added comments explaining the operations.

## What I implemented

I built `Stack` using a Python list. `push()` added changes to the end of the list, `pop()` removed the latest change, `peek()` displayed that change without removing it, and `is_empty()` checked whether anything remained. This represented undoing network configuration changes in reverse order, or last in, first out (LIFO).

I built `Queue` using `collections.deque`. `enqueue()` added tickets to the end, `dequeue()` handled the oldest ticket first, `front()` showed the next ticket, and `is_empty()` checked whether any tickets remained. This represented a basic first come, first served support queue, or first in, first out (FIFO).

## Testing and edge cases

I added four changes and four support tickets to show the order in which items were removed. I also tested removing and viewing items from empty structures. Those operations raised descriptive `IndexError` messages, which the demonstration caught so the program could keep running. I tested a single item in each structure and confirmed both became empty after removal.

## Performance and memory

Both structures stored one reference for each item, so memory usage grew proportionally to the number of stored items, or O(n). Pushing and popping at the end of a Python list were O(1) amortized and O(1), respectively. Adding and removing from opposite ends of a deque were O(1) operations. Peeking and checking for emptiness were O(1).

## Real-world use

I chose network configuration history and support tickets because both situations are familiar to IT and cybersecurity work. Undoing configuration changes is a useful example of LIFO. Processing ordinary support tickets in arrival order is a good example of FIFO, although real support systems may prioritize urgent incidents.

## Running the program

I ran the completed program with:

```bash
python unit2_discussion.py
```

The program printed each operation and the expected error handling for empty structures.

## Reflection

This assignment helped me better understand why stacks and queues use different processing orders even though both hold collections of data. The main thing I had to think through was what should happen when a user tries to remove or view an item that isn't there. I handled that with clear exceptions and caught them in the demonstration rather than letting the whole program stop. For me, the difference makes sense when comparing network changes with routine support tickets. If I need to undo several changes, I'd normally start with the most recent one, which is how a stack works. If tickets are being handled in the order they came in, a queue is more appropriate. Both approaches have their uses, and picking the wrong one could make an application behave in a way users don't expect.
