class Tortuga:
    def shell_sort(self, arr):
        n = len(arr)
        gap = n // 2
        
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2

    def Arreglo(self):
        arr = []
        Limite = int(input("Dame el tamaño del arreglo: "))
        for _ in range(Limite):
            Num = int(input("Ingresa un número: "))
            arr.append(Num)
        return arr

# Ejecución
key = Tortuga()
arr = key.Arreglo()  # Guardamos el arreglo creado por el usuario
key.shell_sort(arr)  # Ordenamos el arreglo usando Shell Sort
print("Arreglo ordenado:", arr)
