try
  
pkg load database
conn = pq_connect (setdbopts ("dbname", "postgres", "host", "localhost", "port", "5432", "user", "postgres", "password", "2807289050109"))

disp("1. N�mero primo o no xd")
disp("2. Historial")
main=input("Opci�n: ");

switch main
  
 case 1
 num=input('Introduce un n�mero: ');
 a=1:n;
 tot = 0;
 if nnz(rem(num,a)==0)==2
     disp('N�mero primo');
     tot = ('Numero primo');
 pq_exec_params(conn, "insert into programa4 values ($1,$2);",{num,tot});
 else
     disp('N�mero compuesto');
     tot = ('Numero Compuesto');
 pq_exec_params(conn, "insert into programa4 values ($1,$2);",{num,tot});
 end
 case 2
 pq_exec_params(conn, 'select * from programa4;')
 otherwise
 disp("Escoge una opci�n v�lida")
end

catch
 disp('Algo sali� mal');
 tot = ('Algo sali� mal');
end_try_catch