using System;
 
public class Test
{
public static void Main()
{
System.Console.WriteLine("Podaj liczbe...");
int n = int.Parse(Console.ReadLine());
if( n % 2 == 0 ) System.Console.WriteLine("Podana liczba jest parzysta.");
else System.Console.WriteLine("Podana liczba nie jest parzysta.");
}
}