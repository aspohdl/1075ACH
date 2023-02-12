int number = Convert.ToInt32(Console.ReadLine());
if (number >= 10)
{
    if (number <= 99)
    {
        if (number % 2 == 0)
        {
            Console.WriteLine($"Число {number} чётное и двузначное");
        }
        else if (number % 2 == 1)
        {
            Console.WriteLine($"Число {number} НЕ является чётным");
        }
    }
    else if (number > 99)
    {
        Console.WriteLine($"Число {number} НЕ является двузначным");
    }
}
else if (number < 10)
{
    Console.WriteLine($"Число {number} НЕ является двузначным");
}
