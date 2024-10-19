# def mult_constante(semilla, constante, n):
#     numeros = []
#     x = semilla
#     for _ in range(n):
#         producto = x * constante
#         str_producto = f"{producto:08d}" 
#         medio = str_producto[2:6] 
#         x = int(medio)
#         numero_pseudoaleatorio = x / 10000 
#         numeros.append((x, f"{x:04d}", numero_pseudoaleatorio))
#     return numeros

# entrada = input("Ingrese un array de números enteros separados por espacios: ")
# array = [int(x) for x in entrada.split()]

# minimo = min(array)
# maximo = max(array)

# resultado = mult_constante(minimo, maximo, 10)

# print(f"Semilla (valor mínimo): {minimo}")
# print(f"Constante (valor máximo): {maximo}")
# print("Números pseudoaleatorios generados:")
# for numero, numero_formateado, pseudo in resultado:
#     print(f"{numero} -> {numero_formateado} -> {pseudo:.4f}")
