using System;
namespace MyNamespace
{
    class zapusk
    {
        static void Main()
        {
            StudentGroup group = new StudentGroup(3, "", 0);
            string result = group.getoldest();
            Console.WriteLine(result);
        }
    }
}