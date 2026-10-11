import unittest
from unit2_discussion import Stack, Queue


class DataStructureTests(unittest.TestCase):
    def test_stack_order_and_peek(self):
        stack = Stack()
        for i in range(4):
            stack.push(i)
        self.assertEqual(stack.peek(), 3)
        self.assertEqual([stack.pop() for _ in range(4)], [3, 2, 1, 0])
        self.assertTrue(stack.is_empty())

    def test_queue_order_and_front(self):
        queue = Queue()
        for i in range(4):
            queue.enqueue(i)
        self.assertEqual(queue.front(), 0)
        self.assertEqual([queue.dequeue() for _ in range(4)], [0, 1, 2, 3])
        self.assertTrue(queue.is_empty())

    def test_empty_operations(self):
        stack, queue = Stack(), Queue()
        for operation in (stack.pop, stack.peek, queue.dequeue, queue.front):
            with self.assertRaises(IndexError):
                operation()

    def test_single_item(self):
        stack, queue = Stack(), Queue()
        stack.push('x')
        queue.enqueue('x')
        self.assertEqual(stack.pop(), 'x')
        self.assertEqual(queue.dequeue(), 'x')
        self.assertTrue(stack.is_empty())
        self.assertTrue(queue.is_empty())


if __name__ == '__main__':
    unittest.main()
