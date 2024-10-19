def cuadrados_medios(semilla, n):
    numeros = []
    for _ in range(n):
        cuadrado = semilla ** 2
        str_cuadrado = f"{cuadrado:08d}"
        medio = str_cuadrado[2:6] 
        semilla = int(medio)
        numero_pseudoaleatorio = semilla / 10000  
        numeros.append((semilla, f"{semilla:04d}", numero_pseudoaleatorio))
    return numeros

entrada = input("Ingrese un array de números enteros separados por espacios: ")
array = [int(x) for x in entrada.split()]

semilla = sum(array)

resultado = cuadrados_medios(semilla, 10)

print(f"Semilla: {semilla}")
print("Números pseudoaleatorios generados:")
for numero, numero_formateado, pseudo in resultado:
    print(f"{numero} -> {numero_formateado} -> {pseudo:.4f}")