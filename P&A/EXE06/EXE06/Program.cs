class Program
{
    static void Main()
    {
        // AA =  Ano Atual, An = Ano Nascimento, IDA= Idade atual;

        double AA, AN, IDA;

        Console.Write("Ano Atual: ");
        AA = double.Parse (Console.ReadLine());

        Console.Write("Ano Nascimento: ");
        AN = double.Parse (Console.ReadLine());

        IDA = AA - AN;
       
        Console.WriteLine("A idade é: {0}", IDA);
    }
}