try
  
pkg load database
conn = pq_connect(setdbopts('dbname','postgres','host','localhost','port','5432','user','postgres','password','2807289050109'))

disp("1. C�lculo de iva")
disp("2. Historial")
main=input("Opci�n: ");
switch main
 case 1
 precio=input("Precio: ");
 noiva = (precio/1.12) ;
 iva = precio - noiva;
 disp("Precio sin iva: ")
 disp(noiva)
 disp("Precio del iva: ")
 disp(iva)
 pq_exec_params(conn, 'insert into programa3 values ($1,$2,$3);',{precio,noiva,iva});
 case 2
 pq_exec_params (conn, "select * from programa3;")
 otherwise
 disp("Escoge una opci�n v�lida")
end
catch
 disp("Algo sali� mal")
end_try_catch