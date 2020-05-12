# coding=utf-8

from test_base import BaseTestCase


class TestCase(BaseTestCase):

    def test_heap(self):
        import random

        from algorithm.tree.heap import Heap

        size = 16
        heap = Heap(Heap.MIN)

        value = [var for var in range(size)]

        for _ in range(size):
            var = random.choice(value)
            value.remove(var)
            heap.append(var)

        heap.build()
        heap.sort()
        self.assertEqual(heap, sorted(heap, reverse=True))

    def test_queue(self):
        from algorithm.tree.heap import PriorityQueue
        queue = PriorityQueue()

        for var in [1, 4, 10, 6, 23, 66, 7, 9]:
            queue.insert(var)

        self.assertEqual(queue, [66, 10, 23, 9, 6, 4, 7, 1])
        self.assertEqual(queue.extract(), 66)
        # print(queue)
        self.assertEqual(queue.extract(), 23)
        self.assertEqual(queue, [10, 9, 7, 1, 6, 4])

        queue = PriorityQueue(PriorityQueue.MIN)

        for var in [1, 4, 10, 6, 23, 66, 7, 9]:
            queue.insert(var)

        self.assertEqual(queue, [1, 4, 7, 6, 23, 66, 10, 9])
        self.assertEqual(queue.extract(), 1)
        # print(queue)
        self.assertEqual(queue.extract(), 4)
        self.assertEqual(queue, [6, 9, 7, 10, 23, 66])


if __name__ == '__main__':
    TestCase.main()
