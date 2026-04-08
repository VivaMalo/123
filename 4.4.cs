Console.Write("Введите x координату точки: ");
double x4 = double.Parse(Console.ReadLine());
Console.Write("Введите y координату точки: ");
double y4 = double.Parse(Console.ReadLine());

if (x4 > 0 && y4 > 0)
{
    Console.WriteLine("Точка попадает в область I");
}
else if (x4 < 0 && y4 > 0)
{
    Console.WriteLine("Точка попадает в область II");
}
else
{
    Console.WriteLine("Точка не попадает ни в одну из областей (или на границу)");
}