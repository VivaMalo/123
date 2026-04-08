Console.Write("Введите x: ");
double x3 = double.Parse(Console.ReadLine());
double y3;

if (x3 > 0)
{
    y3 = Math.Pow(Math.Sin(x3), 2);
}
else
{
    y3 = 1 + 2 * Math.Pow(Math.Sin(x3), 2);
}

Console.WriteLine($"y = {y3}");