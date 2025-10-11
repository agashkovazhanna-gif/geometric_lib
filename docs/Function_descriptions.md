# <span style="color:#FFA500;">Описание функций

### <span style="color: #FF4500;"> Функции для фигуры круг используемые в circle.py

### <span style="color:#FFA500;"> **area(r)**
Вычисляет площадь круга.

**Параметры:**
- `r` (float): Радиус круга

**Возвращает:**
- (float): Площадь круга

**Пример использования функции:**
```python
# Импорт функций
from geometric_lib import circle

# Вычисление площади круга с радиусом 5
result = area(5)
print(result)  # 78.53981633974483
```

### <span style="color:#FFA500;">**perimeter(r)**
Вычисляет длину окружности.

**Параметры:**
- `r` (float): Радиус окружности

**Возвращает:**
- (float): Длина окружности

**Пример использования функции:**
```python
# Импорт функций
from geometric_lib import circle

# Вычисление длины окружности с радиусом 5
result = circle.perimeter(5)
print(result)  # 31.41592653589793
```

### <span style="color: #FF4500;"> Функции для фигуры квадрат используемые в square.py

### <span style="color:#FFA500;"> **area(a)**
Вычисляет площадь квадрата.

**Параметры:**
- `a` (float): Длина стороны квадрата

**Возвращает:**
- (float): Площадь квадрата

**Пример использования функции:**
```python
# Импорт функций
from geometric_lib import square

# Вычисление площади квадрата со стороной 5
result = square.area(5)
print(result)  # 25.0
```

### <span style="color:#FFA500;"> **perimeter(a)**
Вычисляет периметр квадрата.

**Параметры:**
- `a` (float): Длина стороны квадрата

**Возвращает:**
- (float): Периметр квадрата

**Пример использования функции:**
```python
# Импорт функций
from geometric_lib import square

# Вычисление периметра квадрата со стороной 5
result = square.perimeter(5)
print(result)  # 20.0
```