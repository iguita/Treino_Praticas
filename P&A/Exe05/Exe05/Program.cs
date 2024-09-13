class Program
{
    static void Main()
    {
        // preço do produto R$ 250, Preço com desconto R$ 210
        // PP= precoProduto, dsc= desconto, VPD= valorDesconto, VP= valorPago;

        double PP, PD, DSC, VPD;

        Console.Write("Preço do produto: ");
        PP = double.Parse (Console.ReadLine());

        Console.Write("Preço do produto com desconto: ");
        PD = double.Parse (Console.ReadLine());

        DSC = PP - PD;
        VPD = (DSC/PP)*100;

        Console.WriteLine("O desconto aplicado é de: {0}", VPD);
    }
}