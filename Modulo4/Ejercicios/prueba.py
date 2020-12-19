import re

maxrep = 0
count = 0
fin = 0

texto = "ABCXXXXXXXXABCABCABCXXXXXXXXXABCABCABCABCABCABC"

while True:
    encontrado = re.search('ABC', texto)
    if encontrado:
        inicio = encontrado.start()
        end = encontrado.end()
        if fin == 0:
            count = 1
            fin = end
            texto = texto.replace("ABC", "abc", 1) #hacer un replace
        else:
            if inicio == fin:
                texto = texto.replace("ABC", "abc", 1) #hacer un replace
                count = count + 1
                fin = end
            else:
                #Se reinicia el conteo para los patrones restantes
                fin = 0
                if count > maxrep:
                    maxrep = count
                count = 0
    else:
        if count > maxrep:
            maxrep = count
        break


print(f"La cadena ABC más larga es de {maxrep}")
print(texto)