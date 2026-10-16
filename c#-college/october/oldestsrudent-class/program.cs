using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
public class StudentHelper
{
    public static string OldestStudent()
    {
        Dictionary<string, int> dih = new Dictionary<string, int>();

        Console.WriteLine("Enter count of names: ");
        int count = Convert.ToInt32(Console.ReadLine());

        for (int i = 0; i < count; i++)
        {
            Console.WriteLine($"Enter name {i + 1}: ");
            string name = Console.ReadLine();

            Console.WriteLine("Enter age: ");
            int age = Convert.ToInt32(Console.ReadLine());

            dih[name] = age;
        }

        int oldest = Math.Max(dih.Values.Min(), dih.Values.Max());

        string[] names = dih.Keys.ToArray();

        string oldestName = "";

        for (int i = 0; i < names.Length; i++)
        {
            if (dih[names[i]] == oldest)
            {
                oldestName = names[i];
                break;
            }
        }

        return $"The oldest student: {oldestName}, his age: {oldest}";
    }
}