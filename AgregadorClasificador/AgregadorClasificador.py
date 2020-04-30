import argparse
import sys
import textwrap
import math
import numpy as np
from scipy.spatial import distance
#
# Constantes
#

#
# Funcion que recibe los argumentos de la linea de comandos
#
def argumentos():
    '''
    Argumentos() recibe de la linea de comandos
    -h, --help ayuda de los comandos
    -f, --files nombre de alrchivo
    --version  version del programa
    Retorna los argumentos recibidos
    '''
    parser = argparse.ArgumentParser(description='AgreadorClasificador',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''\
                Por defauld la distancia tomada sera la de euclides si no se especifica
                Ejemplo:
                    python AgregadorClasificador.py -f BD.arff clusters.dat -d m

                Formato de cluster.dat:
                ===========================================
                Nombreatributo,valorglobal,closter1,closter2,....
                Nombreatributo,valorglobal,closter1,closter2,....
                Nombreatributo,valorglobal,closter1,closter2,....
            '''))

    # Argumento de paso de Archivos
    parser.add_argument('-f','--files', 
                    action='store',
                    default=None,
                    nargs=2,
                    required=True,
                    dest='archivo',
                    help='-f <DB.arff> <clusters.dat>')
    
    # Argumento de distancia
    parser.add_argument('-d','--distancia', 
                    action='store',
                    default="e",
                    nargs=1,
                    required=False,
                    choices=['e', 'm', 'c','o','s'],
                    dest='funcionDistancia',
                    help=textwrap.dedent('''\
                        Donde:\n
                        e = euclidiada
                        m = Manhattan
                        c = Chebychev
                        o = coseno
                        s = Mahalanobis
                    '''))

    args = parser.parse_args()

    return args.archivo, args.funcionDistancia[0]

#
# Funcion que lee los archivos BD.arff y cluster.dat 
#
def leeArchivos( listaArchivos ):
    '''
        Abre el archivo recivido del argumento -f, --file
        lo abre y lee todas las lineas y las retorna
        en una lista de listas de strings
    '''
    # Se guardan los nombres de los archivos
    archivoNameDB= listaArchivos[0]
    archivoNameCluster = listaArchivos[1]

    # Checa que las extensiones sean las correctas
    if archivoNameDB.find(".arff") == -1:
        sys.exit("Error al abrir la Base de datos")
    elif archivoNameCluster.find(".dat") == -1:
        sys.exit("Error al abrir el archivo de closters, use la extension .dat")

    # Intenta Abrir los archivos
    try:
        archivoBD = open(archivoNameDB,"r")
        archivoCluster = open(archivoNameCluster,"r")
    except:
        sys.exit("Error al abrir los archivos")
    
    #Procesar el archivo
    lineasArchivos = []
    # Lee la base de datos
    lineasArchivos.append( archivoBD.readlines() )

    # Lee los clusters
    lineasArchivos.append( archivoCluster.readlines() )

    # Cierra los Archivos
    archivoBD.close()
    archivoCluster.close()

    return lineasArchivos

#
# Funcion que procesa arff
#
def procesaArff( archivoLeido ):
    cabecera = []
    cuerpoString = []
    i = 0
    # Mientras no encuentre los datos
    while archivoLeido[i].find("@data") == -1:
        cabecera.append(archivoLeido[i])
        i += 1
    # Lo encuentra sale y agrega el @data y deja el apuntador
    # en los datos
    cabecera.append(archivoLeido[i])
    i += 1

    # El resto del archivo leido son datos
    cuerpoString = archivoLeido[i:]

    # Se eliminan las comas y se dejan los datos separados 
    cuerpo = []
    for linea in cuerpoString:
        aux = []
        linea = linea.replace("\n", "")
        aux = linea.split(",")
        cuerpo.append( aux )
    
    #Retorna la cabecera antes de los datos y los datos en forma de lista de listas
    return cabecera, cuerpo

#
# Funcion que procesa el archivo leida
# cluster.dat
#
def procesaClusterDat( archivoLeido ):
    clusters = []
    #Procesa los closters y elimina
    #las palabras siguiendo el formato
    for lista in archivoLeido:
        aux = []
        lista = lista.replace("\n", "")
        aux = lista.split(",")
        clusters.append( aux[2:] )

    aux = np.array(clusters)
    clusterTranspuesto = aux.T

    return clusterTranspuesto

#
# Distancia euclidiana con numpy
#
def distanciaEuclidiana(p1,p2):
       return np.linalg.norm(np.array(p1)-np.array(p2))

#
# Funcion que calcula distancias
#
def caculoDistancias(baseDatos, clusters, tipoDistancia):
    # Para cada vector de datos se compara 
    # la distancia con cada Cluster
    # Se calcula el minimo 
    for vectorv in baseDatos:
        distancias = []
        i = 1
        for vectoru in clusters:
            distancias = [i, distance.euclidean(vectorv,vectoru)]
            print(distancias)
            i += 1

# 
# Main
# Agregador de clase clasificador
#
def main():
    '''
        Lee los archivos pasador por linea de comandos
        guarda los archivos leidos en archivosLeidos
        donde 
        archivosLeidos[0] es el archivo leido BD.arff
        archivosLeidos[1] es el archivo leido cluster.dat
    '''
    nombreArchivos, funcionDistancia = argumentos()
    print("La funcion de distancia es: "+funcionDistancia)

    archivosLeidos = leeArchivos( nombreArchivos )
    print("Se han leido todos los archivos correctamente")

    #Procesa la informacion de BD.arff
    cabecera,cuerpo = procesaArff( archivosLeidos[0])

    #Procesa la informacion de cluster.dat
    clusters = procesaClusterDat( archivosLeidos[1])
    print("Existen un total de "+str(len(clusters))+" Clusters")
    
    caculoDistancias(np.asfarray(cuerpo,float), np.asfarray(clusters,float), funcionDistancia)

if __name__ == '__main__':
    main()