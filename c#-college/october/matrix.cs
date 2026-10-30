namespace MyNamespace;

public class mrt
{
    public static void Main(string[] args)
    {
        string[,] chess =
        {
            { "L", "K", "S", "F", "T", "S", "K", "L" },
            { "0", "0", "0", "0", "0", "0", "0", "0" },
            { "-", "-", "-", "-", "-", "-", "-", "-" },
            { "-", "-", "-", "-", "-", "-", "-", "-" },
            { "-", "-", "-", "-", "-", "-", "-", "-" },
            { "-", "-", "-", "-", "-", "-", "-", "-" },
            { "0", "0", "0", "0", "0", "0", "0", "0" },
            { "L", "K", "S", "T", "F", "S", "K", "L" }
        };

        List<string> coords = new List<string>();

        Console.Write("How many figures? ");

        int count = Convert.ToInt32(Console.ReadLine());
        for (int i = 0; i < count; i++)
        {
            Console.Write("Enter chess coords: ");
            string input = Console.ReadLine();
            coords.Add(input);
        }

        for (int i = 0; i < coords.Count - 1; i++)
        {
            for (int j = 0; j < coords.Count - 1 - i; j++)
            {
                if (GetPrice(coords[j]) > GetPrice(coords[j + 1]))
                {
                    string temp = coords[j];
                    coords[j] = coords[j + 1];
                    coords[j + 1] = temp;
                }
            }
        }

        foreach (string c in coords)
        {
            int letter = (int)char.ToUpper(c[0]) - 65;
            int num = (int)c[1] - 49;
            string figure = chess[num, letter];
            if (figure == "T")
            {
                Console.WriteLine(figure + " - Neopravdano dorogo");
            }
            else
            {
                Console.WriteLine(figure + " - " + GetPrice(c));
            }
        }

        int GetPrice(string c)
        {
            int letter = (int)char.ToUpper(c[0]) - 65;
            int num = (int)c[1] - 49;
            string figure = chess[num, letter];

            if (figure == "0") return 1;
            if (figure == "K") return 3;
            if (figure == "S") return 3;
            if (figure == "L") return 5;
            if (figure == "F") return 9;
            if (figure == "T") return 1000;
            return 0;
        }
    }
}