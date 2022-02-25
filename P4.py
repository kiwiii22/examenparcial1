import psycopg2

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
    print ("\n1.Número primo o compuesto")
    print ("2.Historial")

    opcion = input("\nEscoge la opción deseada: ")

    if opcion == "1":

        num=int(input("Ingrese un número: "))
        cursor = conexion.cursor()

        if num <= 0:
            print("El número debe ser mayor que cero")
        else:
            divisores = 0
            i = 1
            while (i <= num):
                if num % i == 0:
                    divisores+=1
                i+=1
            if divisores==2:
                print("Número primo")
                res = "Número primo"
                cursor.execute("insert into programa4(numero, resultado) values(%s, %s);",(num, res))
                conexion.commit()
            else:
                print("Número compuesto")
                res = "Número compuesto"
                cursor.execute("insert into programa4(numero, resultado) values(%s, %s);",(num, res))
                conexion.commit()
                cursor.close()
                conexion.close()

    if opcion == "2":

        cursor = conexion.cursor()
        SQL = 'select * from programa4;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
main()