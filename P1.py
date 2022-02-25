import random
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
    print ("\n1.Jugar")
    print ("2.Historial")

    opcion = input("\nEscoge la opción deseada: ")
    cursor = conexion.cursor()

    if opcion == "1":

        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        print('El valor del dado 1 es: ',dado1)
        print('El valor del dado 2 es: ',dado2)

        suma = dado1 + dado2
        print("La suma de los dados es: ", suma)

        if suma == 7 :
            print("Perdiste :/")
            res = "Perdiste"
            cursor.execute("insert into programa1(dado1, dado2, suma, resultado) values(%s, %s,%s,%s);",(dado1,dado2,suma,res))
            conexion.commit()
            cursor.close()
            conexion.close()

        elif suma == 8 :
            print("Ganaste :D")
            res= "Ganaste"
            cursor.execute("insert into programa1(dado1, dado2, suma, resultado) values(%s, %s,%s,%s);",(dado1,dado2,suma,res))
            conexion.commit()
            cursor.close()
            conexion.close()
        
        else:
            print("Juega de nuevo")
            res = "Juega de nuevo"
            cursor.execute("insert into programa1(dado1, dado2, suma, resultado) values(%s, %s,%s,%s);",(dado1,dado2,suma,res))
            conexion.commit()
            cursor.close()
            conexion.close()

    if opcion == "2":

        cursor = conexion.cursor()
        SQL = 'select * from programa1;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)

main()
    