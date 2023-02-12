int number = Convert.ToInt32(Console.ReadLine());
if (number >= 10)
{
    if (number <= 99)
    {
        if (number % 2 == 0)
        {
            Console.WriteLine("True");
        }
        else if (number % 2 == 1)
        {
            Console.WriteLine("False");
        }
    }
    else if (number > 99)
    {
        Console.WriteLine("False");
    }
}
else if (number < 10)
{
    Console.WriteLine("False");
}
