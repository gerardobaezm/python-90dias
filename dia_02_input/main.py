# 📥 Ask the user for information
name = input("What is your name? ")
age = input("How old are you? ")
city = input("Where are you from? ")

# 🖨️ Show the message
print(f"Hello {name}, you are {age} years old and you're from {city}.")

# 🔁 Modificación: Convertir la edad a número para hacer cálculos
# 💡 Resultado esperado: permite sumar, restar, etc.

# 🔁 Modificación: convertir la edad a número
# 💡 Esto permite hacer operaciones con la edad
age = int(age)

# 💬 Mostrar un mensaje con edad futura
print(f"In 5 years, you will be {age + 5} years old.")


# 🆕 Pedir altura al usuario
height = float(input("What is your height in meters? "))

# 💡 Mostrar altura actual
print(f"Your height is {height} meters.")

# 🧪 Calcular altura después de crecer un poco
# 💡 Usamos round() para redondear la suma de altura a 2 decimales
# 📌 Esto evita mostrar decimales excesivos como 1.9000000000000001
print(f"If you grew 10 cm, you'd be {round(height + 0.10, 2)}m tall.")

# 🧪 Final Exercise – Day 2
# 💡 Recap: asking all info, doing calculations, and showing results


# 🆕 Name, age, city, height
name3 = input("Enter your name: ")
age3 = int(input("Enter your age: "))
city3 = input("Enter your city: ")
height3 = float(input("Enter your height in meters: "))

# 🖨️ Final message
# 📌 Note: \n adds a blank line before the message to improve visual clarity

print(f"\n Nice to meet you {name3} from {city3}!")
print(f"You're {age3} years old and {height3}m tall.")

# 🔁 Calculations
print(f"In 5 years you'll be {age3 + 5} years old.")
print(f"If you grew 10 cm, you'd be {height3 + 0.10}m tall.")

