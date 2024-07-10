namespace Aula_11CS;

class Program
{
    static void Main(string[] args)
    {
        Retangulo r = new Retangulo();

        r.SetAltura(double.Parse(Console.ReadLine()));
        r.SetBase(double.Parse(Console.ReadLine()));

        Console.WriteLine(r);
        Console.WriteLine(r.CalcArea());
        Console.WriteLine(r.CalcDiagonal());
    }
}
