using System;

class Program
{
    static void Main()
    {
        Console.Write("Введите значение x: ");
        
        if (double.TryParse(Console.ReadLine(), out double x))
        {
            double yA = -x + 2;
            Console.WriteLine($"а) При x = {x}, значение y = {yA}");
            
            double yB;
            if (x <= 3)
            {
                yB = -x;
            }
            else
            {
                yB = -3;
            }
            Console.WriteLine($"б) При x = {x}, значение y = {yB}");
        }
        else
        {
            Console.WriteLine("Ошибка: введено не число.");
        }
    }
}