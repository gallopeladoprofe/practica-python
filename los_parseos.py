nombre = "Abigail"
apellido = "Perez"
edad = 73
peso = 85.6

print(type(nombre))
print(type(edad))
print(type(peso))

# intentar el parsing
edad_en_string = str(edad)
print(f"""La edad anterior era {type(edad)},
      la edad parseada es de tipo 
      {type(edad_en_string)}""")
