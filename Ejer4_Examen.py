def acl(semilla, multiplicador, incremento, modulo, n):
    numeros = []
    x = semilla
    for _ in range(n):
        x = (multiplicador * x + incremento) % modulo
        x_str = f"{x:04d}"[:4]
        x_int = int(x_str)
        numero_pseudoaleatorio = x_int / 10000 
        numeros.append((x, x_str, numero_pseudoaleatorio))
    return numeros

def concatenar_array(arr):
    return int(''.join(map(str, arr)))

arrays = []
for i, nombre in enumerate(["semilla", "multiplicador", "incremento", "módulo"]):
    while True:
        entrada = input(f"Ingrese el array para {nombre} (números de 2 dígitos separados por espacios): ")
        arr = [int(x) for x in entrada.split()]
        if all(10 <= x <= 99 for x in arr):
            arrays.append(arr)
            break
        print("Todos los números deben ser de 2 dígitos. Hazlo de nuevo.")

semilla = concatenar_array(arrays[0])
multiplicador = concatenar_array(arrays[1])
incremento = concatenar_array(arrays[2])
modulo = concatenar_array(arrays[3])

resultado = acl(semilla, multiplicador, incremento, modulo, 5)

print(f"Semilla: {semilla}")
print(f"Multiplicador: {multiplicador}")
print(f"Incremento: {incremento}")
print(f"Módulo: {modulo}")
print("Números pseudoaleatorios generados:")
for numero_completo, numero_formateado, pseudo in resultado:
    print(f"{numero_completo} -> {numero_formateado} -> {pseudo:.4f}")