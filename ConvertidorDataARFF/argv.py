import argparse
import sys
#
# Funcion que recibe los argumentos de la linea de comandos
#
def argumentos():
    '''
    Argumentos() recibe de la linea de comandos
    -h, --help ayuda de los comandos
    -f, --files nombre de alrchivos o PATH .data .names
    --version  version del programa
    Retorna los argumentos recibidos
    '''
    parser = argparse.ArgumentParser(description='Convertidor de .data a .arff')

    parser.add_argument('-f','--files', 
                    action='store',
                    default=None,
                    nargs=2,
                    dest='archivosDataName',
                    help='Recibe Archivos o un PATH de archivos .data y .names para convertir')

    parser.add_argument('--version', action='version',
                    version='%(prog)s 1.4')
    

    #Lee los argumentos de la linea de comandos
    args = parser.parse_args()
    #Reviza si recibio los archivos
    if args.archivosDataName == None:
        sys.exit("No a ingresado ningun archivo\nUtilice [-h] para ayuda")

    return args.archivosDataName

if __name__ == '__main__':
    sys.exit("Error, ejequte primero Convertidor.py -h")