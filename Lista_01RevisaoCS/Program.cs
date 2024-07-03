// See https://aka.ms/new-console-template for more information
// Console.WriteLine("Hello, World!");

Circulo c = new Circulo();

Console.WriteLine("Informe o valor do raio");
c.setRaio(double.Parse(Console.ReadLine()));
Console.WriteLine(c.getRaio());
Console.WriteLine(c.calcArea());
Console.WriteLine(c.calcCircunferencia());