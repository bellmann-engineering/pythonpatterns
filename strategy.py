# Es ist einfach, zwischen verschiedenen Algorithmen zu wechseln, 
# ohne die Struktur des Kontextes zu ändern.
# Neue Suchstrategien können hinzugefügt werden, ohne den bestehenden Code zu verändern.

from abc import ABC, abstractmethod

# Strategy Interface
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

# Konkrete Strategie: BubbleSort
class BubbleSort(SortStrategy):
    def sort(self, data):
        print("Verwende BubbleSort.")
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

# Konkrete Strategie: QuickSort
class QuickSort(SortStrategy):
    def sort(self, data):
        print("Verwende QuickSort.")
        return self.quick_sort(data)

    def quick_sort(self, data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

# Kontextklasse: Sortiermaschine
class Sorter:
    def __init__(self):
        self._strategy = None

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort(self, data):
        if len(data) < 5:
            self.set_strategy(BubbleSort())
        else:
            self.set_strategy(QuickSort())
        return self._strategy.sort(data)

# Verwendung des Strategy Patterns
if __name__ == "__main__":
    # Sortiermaschine erstellen
    sorter = Sorter()

    # Kleine Liste mit weniger als 5 Elementen
    small_list = [5, 1, 4, 2]
    sorted_small_list = sorter.sort(small_list)
    print(f"Sortierte kleine Liste: {sorted_small_list}")

    # Große Liste mit mehr als 5 Elementen
    large_list = [33, 2, 52, 10, 25, 19, 27]
    sorted_large_list = sorter.sort(large_list)
    print(f"Sortierte große Liste: {sorted_large_list}")
