clear all;
close all;

datos = load("dataset_RegresionLineal.txt");

x = datos(:, 1); 
y = datos(:, 2); 
m = numel(x);

a0 = 0;
a1 = 0;
beta = 0.023; 
iterMax = 600;
iter = 1; 

figure(1); 
plot(x, y, 'ok', 'MarkerFaceColor', 'y');
hold on; 

h = a0 + (a1 * x); 
plot(x, h, 'r'); 

J = (1 / (2 * m )) * sum((h - y).^2); 

while(iter < iterMax)

 a0 = a0 - (beta * ((1 / m) * sum(h - y)));
 a1 = a1 - (beta * ((1 / m) * sum((h-y).*x)));
 h = a0 + (a1 * x);
 J = (1 / (2 * m )) * sum((h - y).^2); 
 convergencia(iter) = J;
 iter = iter + 1; 
end

figure(1);
plot(x, h, 'g');

figure(2);
plot(convergencia, '*');
%prueba
datoEntrada = 9.7687; 
hDatoEntrada = a0 + (a1 * datoEntrada); 
%resultado
figure(1);
plot(datoEntrada, hDatoEntrada, 'ok', 'MarkerFaceColor','r');

