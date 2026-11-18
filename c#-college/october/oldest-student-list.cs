class Program
{
    static void Main()
    {
        Console.Write("Enter count of names: ");
        int count = Convert.ToInt32(Console.ReadLine());

        List<string> names = new List<string>();
        List<int> ages = new List<int>();

        for (int i = 0; i < count; i++)
        {
            Console.Write($"Enter name {i + 1}: ");
            string name = Console.ReadLine();
            names.Add(name);

            Console.Write("Enter age: ");
            int age = Convert.ToInt32(Console.ReadLine());
            ages.Add(age);
        }

        if (ages.Count > 0)
        {
            // Находим максимальный возраст напрямую
            int oldest = ages.Max();
            int indx = ages.IndexOf(oldest);
            
            Console.WriteLine($"The oldest student: {names[indx]}");
        }
    }
}