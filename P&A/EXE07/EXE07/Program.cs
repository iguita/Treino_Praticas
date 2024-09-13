class Program
{
    static void Main()
    {
        // Vol= volume , R = raio

        double R, Vol, Pi=3.14;

        Console.Write("Raio da Esfera: ");
        R = double.Parse (Console.ReadLine());

        Vol = Pi * (R * R) ;

        Console.WriteLine("O volume do raio é: {0}", Vol);
    }
}