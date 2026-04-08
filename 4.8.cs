Console.Write("Введите x: ");
double x8 = double.Parse(Console.ReadLine());
double k8;

if (Math.Sin(x8) >= 0) 
    k8 = Math.Pow(x8, 2);
else 
    k8 = Math.Abs(x8);

double f8 = (x8 < k8) ? Math.Abs(x8) : k8 * x8;

Console.WriteLine($"Результат f = {f8}");