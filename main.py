import mean_var_std
from unittest import main

# Verificar si se llega a esta parte del código
print("Starting program...")

# Pedir entrada del usuario
user_input = input("Insert your 9 numbers list separated by commas (Example: 0,1,2,3,4,5,6,7,8): ")

# Verificar si el input es recibido
print(f"User input: {user_input}")

# Convertir la entrada en una lista de enteros
try:
    numbers = [int(num.strip()) for num in user_input.split(",")]
    print(f"Converted numbers: {numbers}")
except ValueError:
    print("Error: Please enter only numbers separated by commas.")
    exit()

# Llamar a la función con la lista ingresada
try:
    result = mean_var_std.calculate(numbers)
    print(f"Calculation result: {result}")
except ValueError as e:
    print(f"Error: {e}")

# Run unit tests automatically
main(module='test_module', exit=False)
