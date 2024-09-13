class Program
{
    public static void Main(string[] args)
    {

        double pr, d, pag, pgt;

        Console.Write("Digite o Preço do Produto: ");
        pr = double.Parse(Console.ReadLine());

        Console.Write("Digite o Desconto aplicado: ");
        d = double.Parse(Console.ReadLine());

        pag = pr * d / 100;

        Console.WriteLine(" O desconto foi de: {0}", pag);
        
        pgt = pr - pag;
        
        Console.Write(" O valor total pago pelo cliente é: {0}", pgt);




    }
}