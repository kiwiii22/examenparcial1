import numpy
import psycopg2
import statistics as stat


try: 
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "2807289050109",
        dbname = "postgres"
    )
    print("Conexión exitosa")
except psycopg2.Error as e:
    print("Ocurrió un error en la conexión")
    print("Verifique los parámetros")

def main():

    print ("\nMenú ")
    print ("\n1.Calificaciones")
    print ("2.Historial")

    opcion = input("\nEscoge la opción deseada: ")
    cursor = conexion.cursor()

    if opcion == "1":

        n1=int(input("1ra nota: "))
        n2=int(input("2da nota: "))
        n3=int(input("3ra nota: "))
        n4=int(input("4ta nota: "))
        n5=int(input("5ta nota: "))
        arreglo=[n1,n2,n3,n4,n5]
        media=numpy.mean(arreglo)
        print("La media es: ",media)
        mediana=numpy.median(arreglo)
        print("La media es: ",mediana)    
        moda=stat.mode(arreglo)
        print("La moda es: ",moda)
        maximo=max(arreglo)
        minimo=min(arreglo)
        rango=maximo-minimo
        print("El rango es: ",rango)
        desvest=numpy.std(arreglo)
        print("La desviación estándar es: ",desvest)
        varianza=numpy.var(arreglo)
        print("La varianza es: ",varianza)
        cursor.execute("insert into programa2(media, mediana, moda, rango, desviacion, varianza) values(%s, %s,%s, %s,%s, %s);",(media,mediana,moda,rango,desvest,varianza))
        conexion.commit()
        cursor.close()
        conexion.close()

    if opcion == "2":

        cursor = conexion.cursor()
        SQL = 'select * from programa2;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
main()