using System;

class Program
{
    static void Main()
    {
        Console.Write("Введите значение x: ");
        double x = Convert.ToDouble(Console.ReadLine());
        
        if (x == 0)
        {
            Console.WriteLine("Ошибка: x не может быть равен 0 (деление на ноль)");
            return;
        }
        
        if (1 + x < 0)
        {
            Console.WriteLine("Ошибка: под корнем отрицательное число");
            return;
        }
        
        double numerator = Math.Sin(3.2) + Math.Sqrt(1 + x);
        double denominator = Math.Abs(5 * x);
        double y = numerator / denominator;
        
        Console.WriteLine($"При x = {x}, y = {y:F4}");
    }
}