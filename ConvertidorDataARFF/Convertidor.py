import argv
import sys
# 
# Main
#
def main():
    #Recibe los argumentos de la ninea de comandos
    nombresArchivos = argv.argumentos()

    #Convierte los archivos a strings
    nombreArchivoData = "" + nombresArchivos[0]
    nombreArchivoName = "" + nombresArchivos[1]

    #Busca la existencia de archivos .data y .name
    if nombreArchivoData.find(".data") == -1 or nombreArchivoName.find(".names") == -1:
       sys.exit("No ingreso un archivo valido")

    #Intenta Abrir los archivos
    try:
        archivoData = open(nombreArchivoData,"r")
        archivoName = open(nombreArchivoName,"r")
    except:
        sys.exit("Error al abrir los archivos "+nombreArchivoData+nombreArchivoName) 

    #Crea un archivo extension .arff con el nombre del archivo .data
    archivoARFF = open(nombreArchivoData.replace(".data", ".arff"),"w")

    #Crea la cabezera @relacion tabla y escribe en archivo.arff
    archivoARFF.write("@relation "+nombreArchivoData.replace(".data", "")+"\n\n")

    lineas = archivoData.readlines()

    #Busca la cantidad de atributos que existen
    i = 0
    j = -1
    for linea in lineas:
        for campo in linea:
            if j != i and campo.find(",") != -1 :
                archivoARFF.write("@attribute A"+str(i+1)+"\n")
                i += 1
        j = i
    archivoARFF.write("@attribute A"+str(i+1)+"\n")

    #Escribe todos los datos en el archivo
    archivoARFF.write("\n@data\n")
    for linea in lineas:
        archivoARFF.write(""+linea)
 
    archivoData.close()
    archivoARFF.close()

if __name__ == '__main__':
    main()