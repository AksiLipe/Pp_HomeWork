name = input("Введите ваше имя: ")
last_name = input("Введите вашу фамилию: ")
age = int(input("Введите ваш возраст: "))

print(f"\nПривет, {name} {last_name}, рад тебя здесь видеть!")
if age >= 18:
    print(f"{name} {last_name}, а ты уже взрослый, тебе целых {age} лет.")
if age < 18:
    print(f"{name} {last_name}, а ты у нас малютка, тебе всего лишь {age} лет.")

