# BnumsPad

Небольшой текстовый редактор на **PySide6** для быстрых заметок.
Умеет открывать и сохранять файлы, имеет четыре темы оформления и хранит стили отдельно от логики.

## Возможности

- Открытие файлов: `.txt`, `.md`, `.ini`, `.json`, `.log`, `.csv`, `.xml`, `.yaml` и «все файлы».
- Сохранение в `.txt`: если путь ещё не выбран, открывается диалог сохранения.
- Горячие клавиши: `Ctrl+O` — открыть, `Ctrl+S` — сохранить.
- Пункт «Помощь» открывает репозиторий проекта в браузере.
- Четыре темы: простые и «красивые», светлые и тёмные.
- Стили вынесены в отдельный файл, логика окна — в другой.

## Структура проекта

```text
PythonApplication1/                 # корень репозитория
├─ README.md                        # этот файл
├─ PythonApplication1.slnx
└─ PythonApplication1/              # проект Visual Studio
   ├─ PythonApplication1.pyproj     # StartupFile: code\app.py
   ├─ code/
   │  ├─ app.py                     # точка входа: QApplication + Win
   │  ├─ logicNotebook.py           # окно, меню, открытие и сохранение файлов
   │  └─ graph.py                   # темы оформления (QSS)
   └─ env2/                         # виртуальное окружение, Python 3.14.3
```

## Запуск

### Из Visual Studio

Открой `PythonApplication1.slnx` и нажми **F5**. Используется интерпретатор `env2`.

### Из терминала

```powershell
cd C:\Users\B1n9uM\source\repos\PythonApplication1\PythonApplication1
.\env2\Scripts\python.exe code\app.py
```

**Требования:** Python 3.14.x и `PySide6`.

## Темы оформления

В `PythonApplication1/code/graph.py` определены четыре функции:

| Функция | Описание |
|---|---|
| `themeWhite()` | простая белая тема |
| `themeDark()` | простая тёмная тема, с читаемым выделением при наведении |
| `beautifulStyle_White()` | красивая светлая тема |
| `beautifilStyle_Dark()` | красивая тёмная тема |

Чтобы включить другую тему, в `PythonApplication1/logicNotebook.py` найди блок с комментарием
`БЛОК ИЗ graph.py` и замени вызов:

```python
self.setStyleSheet(themeWhite())
```

на любую функцию из таблицы выше. После изменения стиля перезапусти приложение —
импорт модуля кэшируется.

## Что дальше

- переключатель темы прямо в меню;
- панель инструментов с иконками;
- сохранение в HTML и подсветка синтаксиса.

## Ссылки

- Репозиторий: <https://github.com/B1n9uM/PythonApplication1>
