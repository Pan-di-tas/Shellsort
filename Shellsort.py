class Tortuga:
    def shell_sort(self, arr):
        n = len(arr)
        gap = n // 2 
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                print("\nPosición inicial:")
                print(f"Elemento actual: arr[{i}] = {arr[i]}")
                while j >= gap and arr[j - gap] > temp:
                    print(f"\nCambio de posición:")
                    print(f"arr[{j}] = arr[{j - gap}] -> {arr[j - gap]} reemplaza {arr[j]}")
                    
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            print(f"\nReducción del intervalo a la mitad: {gap} -> {gap // 2}")
            gap //= 2
            
    def Arreglo(self):
        arr = []
        Limite = int(input("\nDame el tamaño del arreglo: "))
        for _ in range(Limite):
            Num = int(input("Ingresa un número: "))
            arr.append(Num)
        return arr

# Ejecución
key = Tortuga()
arr = key.Arreglo() 
key.shell_sort(arr)
print("\nArreglo ordenado:", arr)
