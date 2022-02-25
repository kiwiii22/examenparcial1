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
    print ("\n1.Calcular iva")
    print ("2.Historial")

    opcion = input("\nEscoge la opción deseada: ")

    if opcion == "1":

        def calculoiva():
            precio = float(input("Precio: "))
            cursor = conexion.cursor()
            noiva = (precio/1.12)
            iva = precio-noiva
            print("Precio sin iva: ", noiva)
            print("Precio del iva: ",iva)
            cursor.execute("insert into programa3(precio,sin_iva,iva) values(%s, %s,%s);",(precio,noiva,iva))
            conexion.commit()
            cursor.close()
            conexion.close()
        calculoiva()

    if opcion == "2":

        cursor = conexion.cursor()
        SQL = 'select * from programa3;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
main()