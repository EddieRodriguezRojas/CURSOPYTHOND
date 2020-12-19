import sys, os

# Ejemplo1
# try:
#     n = float(input("Introduce un número: "))
#     m = 4
#     print("{}/{} = {}".format(n,m,n/m))
# except:
#     print("Ha ocurrido un error, introduce bien el número")


# Ejemplo2


# while(True):
#     try:
#         n = float(input("Introduce un número: "))
#         m = 4
#         print("{}/{} = {}".format(n,m,n/m))
#         break  # Importante romper la iteración si todo ha salido bien
#     except:
#         print("Ha ocurrido un error, introduce bien el número")



# Bloque ELSE

# while(True):
#     try:
#         n = float(input("Introduce un número: "))
#         m = 4
#         print("{}/{} = {}".format(n,m,n/m))
#     except:
#         print("Ha ocurrido un error, introduce bien el número")
#     else:
#         print("Todo ha funcionado correctamente")
#         break  # Importante romper la iteración si todo ha salido bien


# Bloque finally

# while(True):
#     try:
#         n = float(input("Introduce un número: "))
#         m = 4
#         print("{}/{} = {}".format(n,m,n/m))
#     except:
#         print("Ha ocurrido un error, introduce bien el número")
#     else:
#         print("Todo ha funcionado correctamente")
#         break  # Importante romper la iteración si todo ha salido bien
#     finally:
#         print("Fin de la iteración") # Siempre se ejecuta

# Bloque Try - except con e

try:
    n = float(input("Introduce un número: "))
    m = 4
    print("{}/{} = {}".format(n,m,n/m))
except Exception as e:
    print(e)

os.system("pause")