import argparse
import sys
# 
# Main
#
def main():
    args = argumentos()
    if args.archivo_data == None:
        sys.exit("No a ingresado ningun archivo\nUtilice [-h] para ayuda")
    
    nombreArchivo = ""+args.archivo_data

    if nombreArchivo.find(".data") == -1 :
       sys.exit("No ingreso un archivo .data") 

    try:
        archivoData = open(nombreArchivo,"r")
    except:
        sys.exit("No existe el archivo "+nombreArchivo) 
    
    nombreArchivoARFF = nombreArchivo.replace(".data", ".arff")
    archivoARFF = open(nombreArchivoARFF,"w")

    archivoARFF.write("@relation "+nombreArchivo.replace(".data", "")+"\n\n")

    lineas = archivoData.readlines()


    i = 0
    j = -1
    for linea in lineas:
        for campo in linea:
            if j != i and campo.find(",") != -1 :
                archivoARFF.write("@attribute A"+str(i+1)+"\n")
                i += 1
        j = i
    archivoARFF.write("@attribute A"+str(i+1)+"\n")
    archivoARFF.write("\n@data\n")

    for linea in lineas:
        archivoARFF.write(""+linea)
 
    archivoData.close()
    archivoARFF.close()

    print("Archivo "+nombreArchivoARFF+" Convertido\n")
    

def argumentos():
    '''
    Argumentos() recibe de la linea de comandos
    -h, --help ayuda de los comandos
    -f, --file nombre de alrchivo o PATH .data
    --version  version del programa
    Retorna los argumentos recibidos
    '''
    parser = argparse.ArgumentParser(description='Convertidor de .data a .arff')

    parser.add_argument('-f','--file', 
                    action='store',
                    default=None,
                    dest='archivo_data',
                    help='Recibe un Archivo o un PATH de archivos .data para convertir')

    parser.add_argument('--version', action='version',
                    version='%(prog)s 1.0')
    
    return parser.parse_args()

if __name__ == '__main__':
    main()