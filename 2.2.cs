using System;

class Program
{
    static void Main()
    {
        Console.Write("Введите значение a: ");
        double a = Convert.ToDouble(Console.ReadLine());
        
        double numerator = a * a + 10;
        
        double denominator = Math.Sqrt(a * a + 1);
        
        double y = numerator / denominator;
        
        Console.WriteLine($"При a = {a}, значение функции y = {y:F4}");
    }
}