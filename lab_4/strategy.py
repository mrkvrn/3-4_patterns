print("Strategy Pattern")

class SortStrategy:
    def sort(self, data):
        pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        print("Bubble sorting:", data)
        return sorted(data)

class QuickSort(SortStrategy):
    def sort(self, data):
        print("Quick sorting:", data)
        return sorted(data, reverse=True)

class Sorter:
    def __init__(self, strategy=None):
        self.strategy = strategy
    
    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def sort_data(self, data):
        return self.strategy.sort(data)

numbers = [5, 3, 8, 4, 2]
sorter = Sorter()

sorter.set_strategy(BubbleSort())
result = sorter.sort_data(numbers)
print("Result:", result)

sorter.set_strategy(QuickSort())
result = sorter.sort_data(numbers)
print("Result:", result)
