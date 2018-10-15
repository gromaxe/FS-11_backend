class Item:
    def __init__(self, elem, next_item=None, prev_item=None):
        self.elem = elem
        self.next_item = next_item
        self.prev_item = prev_item

    def __str__(self):
        return str(self.elem)
class DoubleLinkedList:
    def __init__(self,):
        self.head = None
        self.tail = None
    def push(self, elem):
        # добавляет элемент в конец списка
        if not isinstance(elem, Item):
            elem = Item(elem)
        if self.tail is None:
            self.head = elem
            self.tail = elem
        else:
            self.tail.next_item = elem
            elem.prev_item = self.tail
            self.tail = elem
    def pop(self, ):
        # убирает элемент из конца списка
        if self.tail is None:
            return None
        if self.tail is self.head:
            _ = self.tail.elem
            self.tail = None
            self.head = None
            return _
        _ = self.tail.elem
        self.tail = self.tail.prev_item
        self.tail.next_item = None
        return _
    def unshift(self, elem):
        # добавляет элемент в начало списка
        if not isinstance(elem, Item):
            elem = Item(elem)
        if self.head is None:
            self.head = elem
            self.tail = elem
        else:
            self.head.prev_item = elem
            elem.next_item = self.head
            self.head = elem
    def shift(self):
        # убирает элемент из начала списка
        if self.head is None:
            return None
        if self.head is self.tail:
            _ = self.head.elem
            self.tail = None
            self.head = None
            return _
        _ = self.head.elem
        self.head = self.head.next_item
        self.head.prev_item = None
        return _
    def len(self):
        # возвращает длину списка
        if self.head is None:
            return 0
        count = 1
        iter_item = self.head
        while iter_item.next_item is not None:
            count += 1
            iter_item = iter_item.next_item
        return count
    def delete(self, elem):
        # удаляет первое вхождение элемента из списка. 
	# При отсутствии эл-та в списке возвращает False
        iter_item = self.head
        if iter_item.elem == elem:
            self.head = iter_item.next_item
            return True
        while iter_item.next_item is not None:
            if iter_item.elem == elem:
                iter_item.next_item.prev_item, iter_item.prev_item.next_item =\
		iter_item.prev_item, iter_item.next_item
                return True
            iter_item = iter_item.next_item
        if iter_item.elem == elem:
            self.tail = iter_item.prev_item
            self.tail.next_item = None
            return True
        return False
    def contains(self, elem):
        # проверяет, входит ли элемент в список
        if self.head.elem == elem:
            return True
        iter_item = self.head
        while iter_item.next_item is not None:
            iter_item = iter_item.next_item
            if iter_item.elem == elem:
                return True
    def first(self):
        # возвращает первый Item в списке
        if self.head is not None:
            return self.head.elem
        return None
    def last(self):
        # возвращает последний Item в списке
        if self.tail is not None:
            return self.tail.elem
        return None
    def __str__(self):
        if self.head is None:
            return 'List is empty!'
        out_str = ""
        iter_item = self.head
        out_str += str(iter_item.elem)
        while iter_item.next_item is not None:
            iter_item = iter_item.next_item
            out_str += '\n' + str(iter_item.elem)
        return out_str
