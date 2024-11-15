n = int(input("Cuantos empleados tiene la empresa:")) 
x = 1 
conta1_3_mill = 0 
conta_mas_3mill = 0 
gastos = 0 

while x <= n: 
    sueldo = float(input("Ingrese el sueldo del empleado:"))
    gastos += sueldo
    if 1000000 <= sueldo <= 3000000:
        conta1_3_mill += 1
        
    elif sueldo > 3000000:
        conta_mas_3mill += 1
    x += 1

# Informar los resultados
print(f"Empleados que cobran entre $1,000,000 y $3,000,000: {conta1_3_mill}")
print(f"Empleados que cobran más de $3,000,000: {conta_mas_3mill}")
print(f"Total que gasta la empresa en sueldos: ${gastos}")
