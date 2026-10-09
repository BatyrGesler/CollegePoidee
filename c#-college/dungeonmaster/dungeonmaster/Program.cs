namespace dungeonmaster
{
    public class Program
    {
        
        public static void Main(string[] args)
        {
            Character zhangir = new Character(4, 7, 13, 6, 8, 9, 100);
            Character iskander = new Character(5, 14, 15, 7, 16, 6, 100);
            Character kapsatar = new Character(7, 12, 11, 7, 16, 6, 100);
            
            Console.WriteLine("zhangir vs iskander");
            
            string stat = "str";
            string stat1 = "str";
            string stat2 = "hp";

            double bonus2 = iskander.SkillCheck(stat);
            double bonus1 = zhangir.SkillCheck2(stat);

            double hp_zhangir = zhangir.abilities[stat2];
            double str_zhangir = zhangir.abilities[stat1];
            
            double hp_iskander = iskander.abilities[stat2];
            double str_iskander = iskander.abilities[stat1];
            
            double str_kapsatar = kapsatar.abilities[stat1];
            
            Console.WriteLine($"stregnth of zhangir: {str_zhangir}");
            Console.WriteLine($"stregnth of iskander: {str_iskander}");
            Console.WriteLine($"stregnth of kapsatar: {str_kapsatar}");
            double minn = Math.Min(str_kapsatar, str_zhangir, str_iskander);
            
            Console.WriteLine(bonus1 + " bonussssss");
            Console.WriteLine(bonus2 + " bonussssss2222");
            
            
            Console.WriteLine($"hp zhangir -  {hp_zhangir}");
            Console.WriteLine($"strength zhangir -  {str_zhangir}");
            
            Console.WriteLine($"hp iskander -  {hp_iskander}");
            Console.WriteLine($"strength iskander -  {str_iskander}");

            while (hp_zhangir >= 0 || hp_iskander >= 0)
            {
                hp_zhangir = hp_zhangir - (str_iskander + bonus2);
                Console.WriteLine($"hp zhangir: {hp_zhangir}");
                if (hp_zhangir <= 0 ) {
                    Console.WriteLine("Zhangir died");
                    break;
                }
                hp_iskander = hp_iskander - (str_zhangir + bonus1);
                Console.WriteLine($"hp iskander: {hp_iskander}");
                if (hp_iskander <= 0)
                {
                    Console.WriteLine("Iskander died");
                    break;
                }
            }
        }
    }
}