try
  
pkg load database
conn = pq_connect(setdbopts('dbname','postgres','host','localhost','port','5432','user','postgres','password','2807289050109'))

disp("1. Calificaciones")
disp("2. Historial")
main=input("Opción: ");
switch main
 case 1
 n1=input("1ra nota: ");
 n2=input("2da nota: ");
 n3=input("3ra nota: ");
 n4=input("4ta nota: ");
 n5=input("5ta nota: ");
 arreglo=([n1 n2 n3 n4 n5]); 
 media=mean(arreglo); 
 fprintf('La media es: %d\n',media)
 mediana=median(arreglo); 
 fprintf('La mediana es: %d\n',mediana)
 moda=mode(arreglo); 
 fprintf('La moda es: %d\n',moda)
 maximo=max(arreglo); 
 minimo=min(arreglo); 
 rango=maximo-minimo;
 fprintf('El rango es: %d\n',rango)
 desvest=std(arreglo,1)
 fprintf('La desviación estándar es: %d\n',desvest)
 varianza=var(arreglo,1)
 fprintf('La varianza es: %d\n',varianza)
 pq_exec_params(conn, 'insert into programa2 values ($1,$2,$3,$4,$5,$6);',{media,mediana,moda,rango,desvest,varianza});
case 2
 pq_exec_params (conn, "select * from programa2;")
 otherwise
 disp("Escoge una opción válida")
end
catch
 disp("Algo salió mal")
end_try_catch