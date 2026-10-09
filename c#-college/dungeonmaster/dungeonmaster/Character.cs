namespace dungeonmaster
{
    public class Character
    {
        public Dictionary<string, double> abilities = new Dictionary<string, double>();
        Random brbr = new Random();
        Random grgr = new Random();
        public Character(double str, double dex, double con, double wis, double intell, double chr, double hp)
        {
            abilities.Add("str", str);
            abilities.Add("dex", dex);
            abilities.Add("con", con);
            abilities.Add("wis", wis);
            abilities.Add("int", intell);
            abilities.Add("chr", chr);
            abilities.Add("hp", hp);
        }

        public double Bonus(string abilityName)
        {
            return Math.Floor((abilities[abilityName] - 10.0) / 2.0);
        }

        public double SkillCheck(string abilityName)
        {
            return brbr.Next(1, 21) + Bonus(abilityName);
        }

        public double SkillCheck2(string abilityName)
        {
            return grgr.Next(1, 21) + Bonus(abilityName);
        }
    }
}