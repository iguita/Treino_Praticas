using System;

class Program
{
    public static void Main(string[] args)
    {
        double H, M, HE, ME, HS, MS, PH, MG, PAG;

        Console.Write("Horario de entrada do estacionamento?: ");
        HE = double.Parse(Console.ReadLine());

        Console.Write("Minutos de entrada?: ");
        ME = double.Parse(Console.ReadLine());

        Console.Write("Horario de saida?: ");
        HS = double.Parse(Console.ReadLine());

        Console.Write("Minutos de saida?: ");
        MS = double.Parse(Console.ReadLine());

        H = HS - HE;
        M = MS - ME;
        PH = H * 4;
        MG = M / 15;
        PAG = PH + MG;

        Console.Write("O valor  a ser pago na saída é de: {0}", PAG);

    }
}