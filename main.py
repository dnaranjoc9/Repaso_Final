#Proyecto de repaso Final Programación Python
import csv
import pandas as pd
def menu():
    while True:
        try:
           print("\nMenú de opciones:")
           print("1. Registrar ventas")
           print("2. Guardar cambios CSV")
           print("3. Consultar ventas")
           print("4. Salir")
           opcion = int(input("Seleccione una opción (1-4): "))

           if opcion == 1:
               registrar_ventas()
           elif opcion == 2:
                print("Funcionalidad para guardar cambios CSV aún no implementada.")
           elif opcion == 3:
                print("Funcionalidad para consultar ventas aún no implementada.")
           elif opcion == 4:
               print("Saliendo del Programa. ¡Hasta luego!")
               break
           else:
                 print("Opción inválida. Por favor, ingrese un número entre 1 y 4.")
                 
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entre 1 y 4.")


def registrar_ventas(ventas: list): # Función para registrar ventas
    while True:
        try:
            #Logica para registrar ventas
            producto = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad vendida: "))
            precio = float(input("Ingrese el precio por unidad: "))
            fecha = input("Ingrese la fecha de la venta (DD/MM/AAAA): ")
            cliente = input("Ingrese el nombre del cliente: ")
            
            if cantidad <= 0 or precio <= 0:
                print("La cantidad y el precio deben ser mayores que cero. Por favor, intente de nuevo.")
                continue

            venta = {
                "producto": producto,
                "cantidad": cantidad,
                "precio": precio,
                "fecha": fecha,
                "cliente": cliente
            }
        
            ventas.append(venta)
        
            continuar = input("¿Desea registrar otra venta? (s/n): ").lower()
            if continuar != 's':
                break
        
        except ValueError:
            print("Entrada inválida. Por favor, intente de nuevo.")
            continue
        
      
def guardar_ventas(ventas:list):
    try:
        if not ventas:
            print("No hay ventas para guardar.")
        pass
        with open('ventas.csv', mode='w', newline='') as archivo:
            guardado = csv.Dicwriter(archivo, fieldnames=["producto", "cantidad", "precio", "fecha", "cliente"]
            guardado.writeheader()
            guardado.writerows(ventas)
        print("Ventas guardadas exitosamente en ventas.csv")
    except Exception as e:
        print(f"\nError al guardar las ventas: {e}")


def consultar_ventas():
    try:
        df=pd.read_csv('ventas.csv')
        if df.empty:
            print("No hay ventas registradas.")
        else:
            print("\nVentas registradas:")
            df["Subtotal"] = df["cantidad"] * df["precio"]
            Total = df["Subtotal"].sum()
            print(f"Total de ventas: {Total:,.2f}")
        
        # Analísis de tendencias        You, now * Uncommitted changes
        producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()
        print(f"Producto más vendido: {producto_mas_vendido}")
        
        tendencia_clientes = df["cliente"].value_counts().idxmax()
        print(f"Cliente con más compras: {tendencia_clientes}")
        except FileNotFoundError:
            print("El archivo 'ventas.csv' no fue encontrado.")
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
        pass
    except FileExistsError

#Programa principal para gestionar ventas
if __name__ == "__main__": # Verificar si el script se está ejecutando directamente
    print("Bienvenido al sistema de gestión de Ventas")
menu()  # Llamar a la función menú para mostrar las opciones
    