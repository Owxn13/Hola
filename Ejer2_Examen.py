def product_medios(semilla1, semilla2, n):
    numeros = []
    for _ in range(n):
        producto = semilla1 * semilla2
        str_producto = f"{producto:08d}"
        medio = str_producto[2:6] 
        nuevo_numero = int(medio)
        numero_pseudoaleatorio = nuevo_numero / 10000 
        numeros.append((nuevo_numero, f"{nuevo_numero:04d}", numero_pseudoaleatorio))
        semilla1, semilla2 = semilla2, nuevo_numero
    return numeros

while True:
    entrada = input("Ingrese un array de números enteros de longitud par, separados por espacios: ")
    array = [int(x) for x in entrada.split()]
    if len(array) % 2 == 0:
        break
    print("La longitud del array debe ser par. Intente de nuevo.")

resultados = []
for i in range(0, len(array), 2):
    semilla1 = array[i]
    semilla2 = array[i+1]
    semilla = semilla1 * semilla2
    numeros = product_medios(semilla1, semilla2, 5)
    resultados.append((semilla, numeros))

for i, (semilla, numeros) in enumerate(resultados):
    print(f"\nPar {i+1}:")
    print(f"Semilla: {semilla} (producto de {array[i*2]} y {array[i*2+1]})")
    print("Números pseudoaleatorios generados:")
    for numero, numero_formateado, pseudo in numeros:
        print(f"{numero} -> {numero_formateado} -> {pseudo:.4f}")