class Program
{
    static void Main()
    {
        // PP= precoProduto, dsc= desconto, VD= valorDesconto, VP= valorPago;

        double PP, dsc, VD, VP;

        Console.Write("Digite o preço do produto: ");
        PP = Convert.ToDouble(Console.ReadLine());

        Console.Write("Digite o desconto (em porcentagem): ");
        dsc = Convert.ToDouble(Console.ReadLine());

        VD = (dsc / 100) * PP;
        VP = PP - VD;

        Console.WriteLine($"O valor a ser pago pelo produto é: R$ {VP:F2}");
    }
}