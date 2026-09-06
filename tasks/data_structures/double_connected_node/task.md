## Описание задачи
Реализуйте функцию, которая разворачивает двусвязный список (меняет порядок элементов на обратный) и возвращает голову развёрнутого списка.

## Требования
- Необходимо написать только функцию разворота списка
- Функция принимает на вход голову двусвязного списка
- Функция должна вернуть голову развёрнутого списка
- Все связи в списке должны быть корректно обновлены

## Ограничения
- Длина списка не превышает 1000 элементов
- Список всегда содержит хотя бы один элемент

## Формат ввода
- Параметр функции:
  - node: голова двусвязного списка

## Формат вывода
- Функция должна вернуть голову развёрнутого списка

## Тесты
- Опишите от 5 тест кейсов, проверяющих корректность и алгоритмическую сложность предложенного решения

```python
class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def solution(node: DoubleConnectedNode) -> DoubleConnectedNode:
    ...

# пример теста
def test():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2

    new_head = solution(node0)
    assert new_head is node3
    assert node3.next is node2
    assert node2.next is node1
    assert node2.prev is node3
    assert node1.next is node0
    assert node1.prev is node2
    assert node0.prev is node1
    # result is node3 -> node2 -> node1 -> node0
```
