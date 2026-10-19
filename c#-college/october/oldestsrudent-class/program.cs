using System;
using System.Collections.Generic;
using System.Linq;

public class StudentGroup
{
    Dictionary<string, int> dih = new Dictionary<string, int>();

    public StudentGroup(int count)
    {

        for (int i = 0; i < count; i++)
        {
            Console.WriteLine($"Enter name {i + 1}: ");
            string name = Console.ReadLine();

            Console.WriteLine("Enter age: ");
            int age = Convert.ToInt32(Console.ReadLine());

            dih[name] = age;
        }
    }

    public string OldestStudent()
    {
        int oldest = dih.Values.Max();

        string oldestName = "";

        foreach (string name in dih.Keys)
        {
            if (dih[name] == oldest)
            {
                oldestName = name;
                break;
            }
        }

        return $"The oldest student: {oldestName}, his age: {oldest}";
    }
}
