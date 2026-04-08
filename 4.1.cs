Console.Write("Введите первое число: ");
double num1 = double.Parse(Console.ReadLine());
Console.Write("Введите второе число: ");
double num2 = double.Parse(Console.ReadLine());

if (num1 > num2)
{
    Console.WriteLine($"Большее: {num1}");
    Console.WriteLine($"Меньшее: {num2}");
}
else
{
    Console.WriteLine($"Большее: {num2}");
    Console.WriteLine($"Меньшее: {num1}");
}