Console.Write("Расстояние в км: ");
double km = double.Parse(Console.ReadLine());

Console.Write("Расстояние в футах: ");
double ft = double.Parse(Console.ReadLine());

double ftInMeters = ft * 0.3048;
double kmInMeters = km * 1000;

if (kmInMeters < ftInMeters)
    Console.WriteLine("Меньше расстояние в километрах");
else if (ftInMeters < kmInMeters)
    Console.WriteLine("Меньше расстояние в футах");
else
    Console.WriteLine("Расстояния равны");