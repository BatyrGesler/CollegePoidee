namespace HelloWorld
{
    public class Program
    {
        public static void Main(string[] args)
        {
   //          List<int> history = new List<int>();
   //          int last_result = 0;
   //
   //          while (true) 
   //          {
   //              string input1 = Console.ReadLine();
   //              if (input1 == null || input1 == "end") 
   //              {
   //                  break;
   //              }
   //
   //              string symbol = Console.ReadLine();
   //              if (symbol == null || symbol == "end") 
   //              {
   //                  break;
   //              }
   //
   //              string input2 = Console.ReadLine();
   //              if (input2 == null || input2 == "end") 
   //              {
   //                  break;
   //              }
   //
   //              int num1;
   //              int num2;
   //
   //              if (input1 == "ans") {
   //                  num1 = last_result;
   //              } else {
   //                  num1 = Convert.ToInt32(input1);
   //              }
   //
   //              if (input2 == "ans") {
   //                  num2 = last_result;
   //              } else {
   //                  num2 = Convert.ToInt32(input2);
   //              }
   //
   //              int result = 0;
   //
   //              if (symbol == "+") {
   //                  result = num1 + num2;
   //              }
   //              else if (symbol == "-") {
   //                  result = num1 - num2;
   //              }
   //              else if (symbol == "/") {
   //                  if (num2 == 0) {
   //                      Console.WriteLine("На ноль делить нельзя");
   //                      continue; 
   //                  }
   //                  result = num1 / num2;
   //              }
   //              else if (symbol == "*") {
   //                  result = num1 * num2;
   //              }
   //
   //              // Console.WriteLine(result);
   //
   //              last_result = result;
   //              history.Add(result); 
   //          }
   //
   //          for (int i = 0; i < history.Count; i++) {
			// 	Console.WriteLine(history[i]);
			// }
        }

        public static int Calc(int num1, int num2, string symbol)
        {
            List<int> history = new List<int>();
            int last_result = 0;
            while (true) 
            {
                string input1 = Console.ReadLine();
                if (input1 == null || input1 == "end") 
                {
                    break;  
                }
                string symbol = Console.ReadLine();
                if (symbol == null || symbol == "end") 
                {
                    break;
                }
                string input2 = Console.ReadLine();
                if (input2 == null || input2 == "end") 
                {
                    break;
                }
                int num1;
                int num2;
                if (input1 == "ans") {
                    num1 = last_result;
                } else {
                    num1 = Convert.ToInt32(input1);
                }
                if (input2 == "ans") {
                    num2 = last_result;
                } else {
                    num2 = Convert.ToInt32(input2);
                }
                int result = 0;
                if (symbol == "+") {
                    result = num1 + num2;
                }
                else if (symbol == "-") {
                    result = num1 - num2;
                }
                else if (symbol == "/") {
                    if (num2 == 0) {
                        Console.WriteLine("На ноль делить нельзя");
                        continue; 
                    }
                    result = num1 / num2;
                }
                else if (symbol == "*") {
                    result = num1 * num2;
                }

                // Console.WriteLine(result);

                last_result = result;
                history.Add(result); 
            }

            for (int i = 0; i < history.Count; i++) {
                Console.WriteLine(history[i]);
            } 
        }
    }
}