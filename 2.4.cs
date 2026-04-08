using System;

class Program
{
    static void Main()
    {
        Console.Write("Введите длину стороны квадрата: ");
        double side = Convert.ToDouble(Console.ReadLine());
        
        if (side < 0)
        {
            Console.WriteLine("Ошибка: длина стороны не может быть отрицательной!");
            return;
        }
        
        double perimeter = 4 * side;
        Console.WriteLine($"Периметр квадрата со стороной {side} равен {perimeter}");
    }
}