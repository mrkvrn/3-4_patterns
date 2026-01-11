print("Iterator Pattern")

class ItemCollection:
    def __init__(self):
        self._items = []
    
    def add_item(self, item):
        self._items.append(item)
    
    def __iter__(self):
        self._current_position = 0
        return self
    
    def __next__(self):
        if self._current_position < len(self._items):
            item = self._items[self._current_position]
            self._current_position += 1
            return item
        raise StopIteration
