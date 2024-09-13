class Program
{
    public static void Main(string[] args)
    {

        double c, l, P;

        Console.Write("Digite o Comprimento: ");
        c = double.Parse(Console.ReadLine());

        Console.Write("Digite Largura: ");
        l = double.Parse(Console.ReadLine());

        P = c * 2 + l * 2;

        Console.Write("O perimetro da Sala é: {0}", P);



    }
}