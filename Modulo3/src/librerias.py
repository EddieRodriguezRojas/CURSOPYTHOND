# import os, sys, shutil
import os # sistema operativo
import sys # argumentos
import shutil # copiar archivos


def copiado(src,dest):
    shutil.copy(src,dest)


if __name__ == "__main__":
    
    try:
        os.chdir('../img')

        # obtengo posicion de directorio
        print(os.getcwd())

        destino = os.path.join(os.getcwd(),'hola')

        # creando ruta destino
        if os.path.isfile(destino):
            os.mkdir(destino)


        # solo copio imagenes a carpeta destino
        for file in os.listdir():
            if file.split('.')[-1] in ['PNG']:
                print('este archivo es una imagen, con nombre {file}'.format(file=file))

                src = os.path.join(os.getcwd(),file)
                # copiando archivos a destino
                copiado(src, os.path.join(destino,file))

        print('archivos copiados a {}'.format(destino))

    except Exception as e:
        print(e)
    finally:
        os.system('pause')