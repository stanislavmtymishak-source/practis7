
class ArrayQueue:
    def __init__(self, capacity=13):
        """Ініціалізація черги масиву фіксованого розміру[cite: 1]."""
        self.capacity = capacity
        self.array = [None] * capacity
        self.head = 0  # Індекс початку черги[cite: 1]
        self.tail = 0  # Індекс кінця черги[cite: 1]

    def is_empty(self):
        """Черга порожня, якщо Head та Tail знаходяться в одній комірці[cite: 1]."""
        return self.head == self.tail

    def is_full(self):
        """Перевірка на переповнення масиву (кільцевий буфер)."""
        return (self.tail + 1) % self.capacity == self.head

    def size(self):
        """Повертає поточну кількість елементів у черзі[cite: 3]."""
        return (self.tail - self.head + self.capacity) % self.capacity

    def enqueue(self, item):
        """Додає новий елемент в чергу (Tail змінює значення)[cite: 2, 3]."""
        if self.is_full():
            print(f"[ArrayQueue] Помилка: Черга переповнена! Элемент {item} не додано.")
            return False

        self.array[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity  # Зміщуємо вказівник Tail[cite: 2]
        print(f"[ArrayQueue] Додано елемент: {item}")
        return True

    def dequeue(self):
        """Видаляє та повертає елемент з початку черги (Head змінює позицію) за FIFO[cite: 1, 2, 3]."""
        if self.is_empty():
            print("[ArrayQueue] Помилка: Черга порожня!")
            return None

        item = self.array[self.head]
        self.array[self.head] = None  # Очищуємо комірку
        self.head = (self.head + 1) % self.capacity  # Зміщуємо вказівник Head[cite: 2]
        print(f"[ArrayQueue] Видалено елемент: {item}")
        return item

    def display(self):
        """Виводить усі наявні елементи черги від Head до Tail[cite: 3]."""
        if self.is_empty():
            print("[ArrayQueue] Черга порожня: []")
            return

        elements = []
        curr = self.head
        while curr != self.tail:
            elements.append(str(self.array[curr]))
            curr = (curr + 1) % self.capacity
        print(f"[ArrayQueue] Елементи черги (Head -> Tail): [{', '.join(elements)}]")


# ------------------------------------------------------------------------------
# 2. Реалізація черги на основі вузлів (Nodes) та посилань[cite: 2]
# ------------------------------------------------------------------------------
class Node:
    def __init__(self, data):
        """Вузол черги: зберігає значення (data) та посилання на наступний вузол (next)[cite: 2]."""
        self.data = data
        self.next = None  # Вказівник порожній до моменту додавання наступного[cite: 3]


class LinkedQueue:
    def __init__(self):
        """Ініціалізація черги на основі вузлів[cite: 2]."""
        self.head = None  # Зберігає адресу першого вузла[cite: 2]
        self.tail = None  # Зберігає адресу останнього вузла[cite: 2]
        self._count = 0  # Лічильник кількості елементів[cite: 3]

    def is_empty(self):
        """Черга порожня, якщо head is None."""
        return self.head is None

    def size(self):
        """Повертає кількість елементів у черзі[cite: 3]."""
        return self._count

    def enqueue(self, item):
        """Додає новий елемент у кінець черги[cite: 2, 3]."""
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node  # Якщо черга порожня, head і tail вказують на новий вузол
            self.tail = new_node
        else:
            self.tail.next = new_node  # Прив'язуємо новий вузол до попереднього[cite: 2]
            self.tail = new_node  # Оновлюємо tail[cite: 2]

        self._count += 1
        print(f"[LinkedQueue] Додано елемент: {item}")

    def dequeue(self):
        """Видаляє та повертає елемент з початку черги (FIFO)[cite: 1, 2, 3]."""
        if self.is_empty():
            print("[LinkedQueue] Помилка: Черга порожня!")
            return None

        removed_data = self.head.data
        self.head = self.head.next  # Записуємо в head адресу наступної змінної[cite: 2]

        if self.head is None:
            self.tail = None  # Якщо вилучено останній вузол

        self._count -= 1
        print(f"[LinkedQueue] Видалено елемент: {removed_data}")
        return removed_data

    def display(self):
        """Виводить усі елементи черги від Head до Tail[cite: 3]."""
        if self.is_empty():
            print("[LinkedQueue] Черга порожня: []")
            return

        elements = []
        curr = self.head
        while curr is not None:
            elements.append(str(curr.data))
            curr = curr.next
        print(f"[LinkedQueue] Елементи черги (Head -> Tail): {' -> '.join(elements)}")


# ------------------------------------------------------------------------------
# Головний блок виконання (Тестування функціоналу за методичкою)[cite: 2, 3]
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 65)
    print(" 1. ТЕСТУВАННЯ ЧЕРГИ НА ОСНОВІ МАСИВУ (ArrayQueue)")
    print("=" * 65)

    q_array = ArrayQueue(capacity=13)

    # Заповнюємо масив значеннями з Рис. 2 (6, 4, 6, 2, 7)[cite: 2]
    print("--- 1. Додавання елементів (enqueue) ---")
    for value in [6, 4, 6, 2, 7]:
        q_array.enqueue(value)

    q_array.display()
    print(f"Поточна кількість елементів у черзі: {q_array.size()}\n")

    print("--- 2. Видалення елементів за правилом FIFO (dequeue) ---")
    q_array.dequeue()
    q_array.dequeue()

    q_array.display()
    print(f"Кількість елементів після видалення: {q_array.size()}\n\n")

    print("=" * 65)
    print(" 2. ТЕСТУВАННЯ ЧЕРГИ НА ОСНОВІ ВУЗЛІВ (LinkedQueue)")
    print("=" * 65)

    q_linked = LinkedQueue()

    # Додаємо елементи з Рис. 3 (12, 25, 8)[cite: 2]
    print("--- 1. Додавання елементів (enqueue) ---")
    for value in [12, 25, 8]:
        q_linked.enqueue(value)

    q_linked.display()
    print(f"Поточна кількість елементів у черзі: {q_linked.size()}\n")

    print("--- 2. Видалення елемента за правилом FIFO (dequeue) ---")
    q_linked.dequeue()

    q_linked.display()
    print(f"Кількість елементів після видалення: {q_linked.size()}")