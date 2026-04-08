using System;

class Program
{
    static void Main()
    {
        Console.Write("Введите радиус окружности: ");
        double radius = Convert.ToDouble(Console.ReadLine());
        
        if (radius < 0)
        {
            Console.WriteLine("Ошибка: радиус не может быть отрицательным!");
            return;
        }
        
        double diameter = 2 * radius;
        Console.WriteLine($"Диаметр окружности с радиусом {radius} равен {diameter}");
    }
}