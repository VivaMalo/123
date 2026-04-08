using System;

Console.Write("Введите x: ");
double x = double.Parse(Console.ReadLine());
double k;

if (Math.Sin(x) < 0) 
    k = Math.Pow(x, 2);
else 
    k = Math.Abs(x);

double f;
if (k < x) 
    f = k * x;
else 
    f = k + x;

Console.WriteLine($"Результат f = {f}");