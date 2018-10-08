import sys 
sys.path.insert(0, '/home/inmio/technotrack/backend/FS-11_backend/app') 

import DoublyLinkedList

import unittest


class TestPush(unittest.TestCase):
    def test_push(self):
        test_list=DoublyLinkedList.DoubleLinkedList()
        test_list.push(1)
        self.assertEqual(test_list.tail.elem,1)
        test_list.push(2)
        self.assertEqual(test_list.tail.elem,2)

class TestPop(unittest.TestCase):
    def test_pop(self):
        test_list=DoublyLinkedList.DoubleLinkedList()
        test_list.push(1)
        test_list.push(2)
        self.assertEqual(test_list.pop(),2)
        self.assertEqual(test_list.pop(),1)
    def test_pop_empty(self):
        test_list=DoublyLinkedList.DoubleLinkedList()
        self.assertEqual(test_list.pop(),None)

class TestUnshift(unittest.TestCase):
    def test_unshift(self):
        test_list=DoublyLinkedList.DoubleLinkedList()
        test_list.unshift(1)
        self.assertEqual(test_list.head.elem,1)
        test_list.unshift(2)
        self.assertEqual(test_list.head.elem,2)

class TestShift(unittest.TestCase):
    def test_shift(self):
        test_list=DoublyLinkedList.DoubleLinkedList()
        test_list.unshift(1)
        test_list.unshift(2)
        self.assertEqual(test_list.shift(),2)
        self.assertEqual(test_list.shift(),1)
    def test_shift_empty(self):
        test_list=DoublyLinkedList.DoubleLinkedList()
        self.assertEqual(test_list.shift(),None)

class TestLen(unittest.TestCase):
    def test_len(self):
        test_list=DoublyLinkedList.DoubleLinkedList()
        test_list.unshift(1)
        self.assertEqual(test_list.len(),1)
        test_list.unshift(2)
        self.assertEqual(test_list.head.elem,2)
    def test_len_empty(self):
        test_list=DoublyLinkedList.DoubleLinkedList()
        self.assertEqual(test_list.len(),0)

class TestDelete(unittest.TestCase):
    def test_delete_first(self):
        test_list=DoublyLinkedList.DoubleLinkedList()
        test_list.unshift(1)
        self.assertTrue(test_list.delete(1))
    def test_len_delete(self):
        test_list=DoublyLinkedList.DoubleLinkedList()
        test_list.unshift(3)
        test_list.unshift(1)
        test_list.unshift(2)
        self.assertTrue(test_list.delete(1))
    def test_len_delete_last(self):
        test_list=DoublyLinkedList.DoubleLinkedList()
        test_list.unshift(1)
        test_list.unshift(2)
        self.assertTrue(test_list.delete(2))

    def test_len_delete_no_elem(self):
        test_list=DoublyLinkedList.DoubleLinkedList()
        test_list.unshift(1)
        test_list.unshift(2)
        self.assertFalse(test_list.delete(3))

class TestContains(unittest.TestCase):
    def test_contains_yes(self):
        test_list=DoublyLinkedList.DoubleLinkedList()
        test_list.unshift(1)
        self.assertTrue(test_list.contains(1))
    def test_contains_no(self):
        test_list=DoublyLinkedList.DoubleLinkedList()
        test_list.unshift(1)
        self.assertFalse(test_list.contains(2))

class TestFirst(unittest.TestCase):
    def test_first(self):
        test_list=DoublyLinkedList.DoubleLinkedList()
        test_list.unshift(1)
        self.assertEqual(test_list.first(),1)
        test_list.unshift(2)
        self.assertEqual(test_list.first(),2)
    def test_first_none(self):
        test_list=DoublyLinkedList.DoubleLinkedList()
        self.assertEqual(test_list.first(),None)

class TestLast(unittest.TestCase):
    def test_Last(self):
        test_list=DoublyLinkedList.DoubleLinkedList()
        test_list.unshift(1)
        self.assertEqual(test_list.last(),1)
        test_list.unshift(2)
        self.assertEqual(test_list.last(),1)
    def test_last_none(self):
        test_list=DoublyLinkedList.DoubleLinkedList()
        self.assertEqual(test_list.last(),None)


