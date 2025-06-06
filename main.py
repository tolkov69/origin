import random

# Генеруємо випадкове число від 1 до 100
secret_number = random.randint(1, 100)
max_attempts = 7

print("Вгадай число від 1 до 100!")
print(f"У тебе є {max_attempts} спроб.")

for attempt in range(1, max_attempts + 1):
    guess_input = input(f"\nСпроба {attempt}. Введи своє число: ")

    # Перевірка, чи введено коректне число
    if not guess_input.isdigit():
        print("Введи, будь ласка, ціле число.")
        continue

    guess = int(guess_input)

    if guess < secret_number:
        print("Занадто маленьке.")
    elif guess > secret_number:
        print("Занадто велике.")
    else:
        print(f"Вітаємо, ти вгадав число {secret_number} з {attempt} спроб(и)!")
        break
else:
    print(f"\nНажаль, спроби закінчились. Загадане число було: {secret_number}")
