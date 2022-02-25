try
  
pkg load database
conn = pq_connect(setdbopts('dbname','postgres','host','localhost','port','5432','user','postgres','password','2807289050109'))

disp("1. Jugar")
disp("2. Historial")
main=input("Opción: ");
switch main
 case 1
 dado1=randi(6)
 dado2=randi(6)
 disp("El valor del dado 1 es: ")
 disp(dado1)
 disp("El valor del dado 2 es: ")
 disp(dado2)
 suma = dado1+dado2;
 disp("La suma de los dados es: ")
 disp(suma)
 if suma == 7
   disp("Perdiste :/")
   res = ('Perdiste'); 
   pq_exec_params(conn, 'insert into programa1 values ($1,$2,$3,$4);',{dado1,dado2,suma,res});
 elseif  suma == 8
   disp("Ganaste :D")
   res = ('Ganaste');
   pq_exec_params(conn, 'insert into programa1 values ($1,$2,$3,$4);',{dado1,dado2,suma,res});
 else
   disp("Juega de nuevo")
   res = ('Juega de nuevo');
   pq_exec_params(conn, 'insert into programa1 values ($1,$2,$3,$4);',{dado1,dado2,suma,res});
 endif
 case 2
 pq_exec_params (conn, "select * from programa1;")
 otherwise
 disp("Escoge una opción válida")
end
catch
 disp("Algo salió mal")
end_try_catch
