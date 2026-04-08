using System;

class Program
{
    static void Main()
    {
        Console.Write("Введите значение x: ");
        double x = Convert.ToDouble(Console.ReadLine());
        
        double y = 17 * x * x + 6 * x + 13;
        
        Console.WriteLine($"При x = {x}, значение функции y = {y}");
    }
}