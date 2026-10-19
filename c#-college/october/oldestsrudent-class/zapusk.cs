using System;
namespace MyNamespace
{
    class zapusk
    {
        static void Main()
        {
            StudentGroup group = new StudentGroup(3);
            string result = group.OldestStudent();
            Console.WriteLine(result);
        }
    }
}