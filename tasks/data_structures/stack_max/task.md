## Описание задачи
Реализуйте класс `StackMax`, который поддерживает операцию определения максимума среди всех элементов в стеке.

## Требования
- Класс должен поддерживать следующие операции:
  - `push(x)`: добавить целое число x в стек
  - `pop()`: удалить число с вершины стека
  - `get_max()`: вернуть максимальное число в стеке

## Ограничения
- Количество команд не превышает 10000
- Для операции push(x): число x не превышает 10^5
- При пустом стеке:
  - get_max() должен вернуть "None"
  - pop() должен вернуть "error"

## Формат ввода
- В первой строке записано количество команд n
- В следующих n строках записаны команды, каждая в своей строке:
  - push(x) - где x целое число
  - pop()
  - get_max()

## Формат вывода
- Для каждой команды get_max() напечатать результат её выполнения
- Для команды pop() при пустом стеке напечатать "error"
- Для команды get_max() при пустом стеке напечатать "None"

## Примеры

### Пример 1
```
Ввод:
8
get_max
push 7
pop
push -2
push -1
pop
get_max
get_max

Вывод:
None
-2
-2
```

### Пример 2
```
Ввод:
7
get_max
pop
pop
pop
push 10
get_max
push -9

Вывод:
None
error
error
error
10
```

## Тесты
- Опишите от 5 тест кейсов, проверяющих корректность и алгоритмическую сложность предложенного решения

```python
class StackMax:
    def __init__(self):
        ...

    def push(self, x: int) -> None:
        ...

    def pop(self) -> str | None:
        ...

    def get_max(self) -> int | str | None:
        ...

# пример теста
def test():
    stack = StackMax()
    assert stack.get_max() == "None"
    assert stack.pop() == "error"

    stack.push(7)
    assert stack.get_max() == 7

    stack.push(1)
    stack.push(3)
    assert stack.get_max() == 7

    stack.pop()
    stack.pop()
    assert stack.get_max() == 7

    stack.pop()
    assert stack.get_max() == "None"
```
