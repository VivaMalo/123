using System;

class Program
{
    static void Main()
    {
        Console.Write("Введите значение a: ");
        double a = Convert.ToDouble(Console.ReadLine());
        
        double numerator = 2 * a + Math.Sin(3 * a);
        double y = numerator / 3.56;
        
        Console.WriteLine($"При a = {a}, значение функции y = {y:F4}");
    }
}