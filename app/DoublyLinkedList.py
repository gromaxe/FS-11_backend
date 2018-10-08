
# coding: utf-8

# Необходимо реализовать двусвязный список на python и протестировать его.
# 
# Код оформить в виде класса DoubleLinkedList со следующими методами:
# 
#     push(elem) добавляет элемент в конец списка
#     pop() убирает элемент из конца списка
#     unshift(elem) добавляет элемент в начало списка
#     shift() убирает элемент из начала списка
#     len() возвращает длину списка
#     delete(elem) удаляет элемент из списка
#     contains(elem) проверяет, входит ли элемент в список
#     first() возвращает первый Item в списке
#     last() возвращает последний Item в списке
# 
# Отдельный элемент списка нужно хранить внутри класса Item со следующими свойствами:
# 
#     next__item следующий Item
#     prev__item предыдущий Item
#     elem элемент текущего Item
# 
# Внимание (!) выше указаны не сигнатуры методов, а только общее описание. Тесты должны проверять работу всех указанных методов и особенно в граничных случаях, например пустой список или список из одного элемента.



class Item:
    
    def __init__(self, elem, next_item = None, prev_item = None):
        self.elem     = elem
        self.next_item = next_item
        self.prev_item = prev_item
        
    
    def next_item (self):
        return self.next_item
    def prev_item (self):
        return self.prev_item
    def elem (self):
        return self.elem

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

        if self.tail == None:
            self.head = elem
            self.tail = elem
        else:
            self.tail.next_item = elem
            elem.prev_item = self.tail
            self.tail = elem
            
    def pop(self, ):
        # убирает элемент из конца списка
        if self.tail == None:
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

        if self.head == None:
            self.head = elem
            self.tail = elem
        else:
            self.head.prev_item = elem
            elem.next_item = self.head
            self.head = elem
        
    def shift(self):
        # убирает элемент из начала списка
        if self.head == None:
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
        if(self.head == None):
            return 0
        
        count = 1
        iter_item = self.head
        while(iter_item.next_item != None):
            count =+ 1
            iter_item = iter_item.next_item
        return count
    
    def delete(self, elem):
        # удаляет первое вхождение элемента из списка. При отсутствии эл-та в списке возвращает False
        iter_item = self.head
        if iter_item.elem == elem:
            self.head = iter_item.next_item
            return True
        
        while(iter_item.next_item != None):
            if (iter_item.elem == elem):
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
        while(iter_item.next_item != None):
            iter_item = iter_item.next_item
            if(iter_item.elem == elem):
                return True
        
    def first(self):
        # возвращает первый Item в списке
        if(self.head != None):
            return self.head.elem
        else:
            return None
    def last(self):
        # возвращает последний Item в списке
        if(self.tail != None):
            return self.tail.elem
        else:
            return None
    def __str__(self):
        if(self.head == None):
            return 'List is empty!'
            
        out_str = ""
        iter_item = self.head
        out_str += str(iter_item.elem) 
        while(iter_item.next_item != None):
            iter_item = iter_item.next_item
            out_str += '\n' + str(iter_item.elem)
        return out_str


