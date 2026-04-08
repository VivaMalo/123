Console.Write("Введите x координату точки: ");
double x5 = double.Parse(Console.ReadLine());
Console.Write("Введите y координату точки: ");
double y5 = double.Parse(Console.ReadLine());

double radiusSquared = x5 * x5 + y5 * y5;
double innerRadius = 5.0;
double outerRadius = 10.0;

if (radiusSquared < innerRadius * innerRadius)
{
    Console.WriteLine("Точка попадает в область I (внутренний круг)");
}
else if (radiusSquared > innerRadius * innerRadius && radiusSquared <= outerRadius * outerRadius)
{
    Console.WriteLine("Точка попадает в область II (кольцо)");
}
else
{
    Console.WriteLine("Точка не попадает ни в одну из областей");
}