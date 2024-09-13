class Program
{
    public static void Main(string[] args)
    {

        double c, l, A;

        Console.Write("Digite o Comprimento: ");
        c = double.Parse(Console.ReadLine());

        Console.Write("Digite Largura: ");
        l = double.Parse(Console.ReadLine());

        A = c + l ;

        Console.Write("A area da Sala é: {0}", A);



    }
}