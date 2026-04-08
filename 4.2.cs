Console.Write("Введите x: ");
double x2 = double.Parse(Console.ReadLine());
double y2;

if (x2 > 0)
{
    y2 = Math.Pow(Math.Sin(x2), 2);
}
else
{
    y2 = 1 - 2 * Math.Pow(Math.Sin(x2), 2);
}

Console.WriteLine($"y = {y2}");