# Задание 2. Алгоритмы и структуры данных

Курс «Программная инженерия», Политех, осень 2026.

## Что нужно сделать

Решить минимум:

- **3 задачи** из `tasks/data_structures/`
- **2 задачи** из `tasks/sorts/`
- **1 задачу** из `tasks/recursion/`

Для каждой выбранной задачи:

1. Прочитать `task.md` в её папке — там описание, ограничения, формат ввода/вывода
   и сигнатура функции или класса, которую нужно реализовать.
2. Создать рядом файл `solution.py` и реализовать решение с той сигнатурой,
   что указана в `task.md`.
3. Типизировать код (проходит `mypy`) и добавить короткие докстринги
   к публичным функциям и методам.
4. Написать минимум **5 своих тестов** на задачу в `tests/<раздел>/<задача>/test_solution.py`
   (см. [tests/README.md](tests/README.md)).

Список задач:

| Раздел | Задача |
|---|---|
| data_structures | [bracket_sequence](tasks/data_structures/bracket_sequence/task.md) |
| data_structures | [double_connected_node](tasks/data_structures/double_connected_node/task.md) |
| data_structures | [stack_max](tasks/data_structures/stack_max/task.md) |
| data_structures | [tasks_list](tasks/data_structures/tasks_list/task.md) |
| data_structures | [update_list](tasks/data_structures/update_list/task.md) |
| sorts | [bubble_sort](tasks/sorts/bubble_sort/task.md) |
| sorts | [insertion_sort](tasks/sorts/insertion_sort/task.md) |
| sorts | [merge_sort](tasks/sorts/merge_sort/task.md) |
| sorts | [quick_sort](tasks/sorts/quick_sort/task.md) |
| recursion | [binary_search](tasks/recursion/binary_search/task.md) |

Решать можно больше минимума — лишние решённые задачи не мешают, CI проверяет
только то, что вы реализовали.

## Установка

Нужен **uv** — менеджер зависимостей и окружений Python.

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Дальше в корне репозитория:

```bash
make install   # uv sync — ставит зависимости и виртуальное окружение
make hooks     # ставит pre-commit хуки (автопроверка перед каждым коммитом)
```

## Как проверить себя локально до пуша

```bash
make check
```

Это ровно то, что запускает CI: `ruff check`, `ruff format --check`, `mypy`,
затем ваши тесты из `tests/` и эталонные тесты преподавателя из `tests_reference/`.
Если задача не решена — её эталонные тесты помечаются `SKIPPED`, это нормально.

Проверить набранный минимальный объём:

```bash
make check-volume
```

Другие полезные команды — `make lint`, `make format`, `make test` (только свои тесты).

## Как сдавать

1. Создайте ветку `develop` и работайте в ней.
2. Когда готовы сдавать — откройте Pull Request `develop → main`.
3. Запросите ревью у преподавателя.
4. Напишите в общий чат курса, что отправили задание на проверку.
5. **PR с непройденными проверками не смотрится** — сначала добейтесь зелёных
   чеков `lint` и `tests` в самом PR.
6. После approve задание считается принятым.

## Что проверяет CI, а что — преподаватель

CI (обязательно, автоматически, при каждом PR):

- линтер и форматтер (`ruff`);
- типизация (`mypy`);
- ваши тесты из `tests/`;
- эталонные тесты преподавателя из `tests_reference/` — они всегда подтягиваются
  из этого же шаблона по фиксированному тегу, а не берутся из вашей копии, так
  что подправить их под своё решение не получится.

Преподаватель смотрит глазами (после зелёного CI):

- набран ли минимальный объём (3 + 2 + 1);
- читаемость и типизация кода, докстринги;
- что ваши тесты в `tests/` не пустые и реально проверяют граничные случаи;
- нет ли изменений в `tests_reference/` или `.github/workflows/`.
