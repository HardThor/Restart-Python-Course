Конспект

Що таке Markdown (.md) і як його використовувати

Markdown (.md) — це легка мова розмітки для форматування тексту. Використовується у README-файлах GitHub, документації, нотатках.

Основні можливості:

# Заголовок — заголовки різного рівня (один # — найбільший, ## менший і так далі).

**Жирний текст** або __Жирний текст__

*Курсив* або _Курсив_

`Код` — виділення коду в рядку.



print("Привіт, світ!")
``` — блок коду.

- або 1. — списки.

# Основи Python

1. Змінні та типи даних

int, float, str, bool, None

type() — визначає тип змінної

str() int() float() — перетворення типів

2. Оператори

Арифметичні: +, -, *, /, //, %, **

Логічні: and, or, not

Порівняння: ==, !=, >, <, >=, <=

3. Умови (if-elif-else)

if умова:
    # Код виконається, якщо умова істинна
elif інша_умова:
    # Альтернативна умова
else:
    # Код виконається, якщо попередні умови хибні

4. Цикли (for, while)

for використовується для перебору послідовностей.

while виконується, поки умова істинна.

break — зупиняє цикл.

continue — пропускає ітерацію та починає наступну.

5. Функція range()

Генерує послідовність чисел.

for i in range(5):
    print(i)  # Виведе числа 0-4

6. Функція enumerate()

Додає індекси при ітерації.

for index, value in enumerate(["a", "b", "c"]):
    print(index, value)

7. Обробка винятків (try-except-finally)

try:
    x = int(input("Введіть число: "))
except ValueError:
    print("Помилка: потрібно ввести число!")
finally:
    print("Ця частина виконається завжди.")

8. Скорочені операції

+=, -=, *=, /=, %= — скорочені форми операцій.

x = 5
x += 2  # Те саме, що x = x + 2


Цей конспект містить ключові поняття. Для прикладів та практики використовуй .py файли в репозиторії.