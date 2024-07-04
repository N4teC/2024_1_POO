namespace Aula_10CS;

class Program
{
    static void Main(string[] args)
    {
        Circle c = new Circle();
        Console.WriteLine("Digite o valor do raio:");
        c.SetRadius(double.Parse(Console.ReadLine()));

        Console.WriteLine(c.GetRadius());
        Console.WriteLine(c.CalcArea());
        Console.WriteLine(c.CalcCircunferencia());
    }
}
