# TODO

## 2024-03-21
- [x] Установлен pydantic для типизации классов 
- [x] Создан файл itypes/tcolor.py с классом TColor
- [x] Добавлены импорты в itypes/tbuffer.py 
- [x] Создан класс TBuffer для работы с текстовым буфером
  - Поля: buffer (List[str]), cursor (int), selection (Optional[Tuple[int, int]]) 
- [x] Исправлена обработка клавиш управления курсором (добавлен keypad) 