using System;

class Program
{
    static void Main()
    {
        Console.Write("Введите значение a: ");
        double a = Convert.ToDouble(Console.ReadLine());
        
        double y = 3 * a * a + 5 * a - 21;
        
        Console.WriteLine($"При a = {a}, значение функции y = {y}");
    }
}