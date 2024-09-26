# punto 1
name = "Tatiana"
age = 25
favouriteFood = "pizza"

presentation = f"Hola, me llamo {name}, tengo {age} años y mi comida favorita es {favouriteFood}."
print(presentation)

# Se solicita al usuario el nombre
full_name = input("Introduce tu nombre completo: ")

# se inprime el mensaje
print(f"Hola, {full_name}. Tu nombre tiene {len(full_name.replace(' ', ''))} letras.")

#punto2
# Solicitar los datos al usuario
increaseSalesPercent = float(input("Ingrese el porcentaje de aumento de las ventas: "))
revenueGrowthPercent = float(input("Ingrese el porcentaje de crecimiento de ingresos: "))

# Crear la cadena usando f-string con un formato específico
message = f"El porcentaje de aumento de las ventas es {increaseSalesPercent:0.2f}% y el crecimiento de ingresos es {revenueGrowthPercent:0.2f}%."

# Imprimir el mensaje
print(message)


def decode_message(encoded_message, target):
    trimmed_message = encoded_message[3:]

    decoded_message = []

    target_index = 0

    for char in trimmed_message:
        if target_index < len(target):
            if char == target[target_index]:
                decoded_message.append(char)
                target_index += 1
    return ''.join(decoded_message)


encoded_message = "aS!Ir waQm VL!eDafrcnXi n=gS .P,yytahgoln.!"
target = "I am Learning Python"
decoded_message = decode_message(encoded_message, target)

print(decoded_message)




# Solicitar al usuario que ingrese una frase
text = input('Por favor, ingrese una frase: ')

# Contar el número de palabras usando split()
word_count = len(text.split())

# Mostrar el número de palabras
print(f'El número de palabras en la frase es: {word_count}')

# Solicitar al usuario que ingrese una cadena
word = input('Por favor, ingrese una cadena para cambiar la letra A por la letra E: ')

# Reemplazar 'a' con 'e'
modified_word = word.replace('a', 'e').replace('A', 'E')  # También reemplaza 'A' en mayúscula

# Mostrar el resultado
print(f'Cadena original: {word}')
print(f'Cadena modificada: {modified_word}')


# Solicitar al usuario que ingrese una frase
sentence = input('Por favor, ingrese una frase para intercanviar el orden: ')

# Invertir el orden de las palabras
reversed_sentence = ' '.join(sentence.split()[::-1])

# Mostrar la frase invertida
print(f'Frase original: {sentence}')
print(f'Frase invertida: {reversed_sentence}')

