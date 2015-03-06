using System;
using System.IO;
using System.Text.RegularExpressions;

    class Program
    {
        static void Main(string[] args)
        {
            Square a = new Square();
            try {
            using (StreamReader sReader = File.OpenText(args[0]))
            
                while (!sReader.EndOfStream)
                {
                        
                    string lineOfText = sReader.ReadLine();
                    if (lineOfText != null && checkLine(lineOfText))
                    {
                        Console.WriteLine(a.isSquare(lineOfText));
                    }

                }
            }
            catch (System.IndexOutOfRangeException)
            {
                Console.WriteLine("Input file argument...");
            }
         }
        static bool checkLine(string line)
        {
            
            Regex regex = new Regex(@"^[(]([0-9]|10),([0-9]|10)[)],[(]([0-9]|10),([0-9]|10)[)],[(]([0-9]|10),([0-9]|10)[)],[(]([0-9]|10),([0-9]|10)[)]");
            Regex regexWithSpace = new Regex(@"^[(]([0-9]|10),([0-9]|10)[)],\s[(]([0-9]|10),([0-9]|10)[)],\s[(]([0-9]|10),([0-9]|10)[)],\s[(]([0-9]|10),([0-9]|10)[)]");
            if (regex.IsMatch(line) || regexWithSpace.IsMatch(line))
            {
                return true;
            }
            else
            {
                Console.WriteLine("Input data is incorrect");
                return false;
            }
           
        }
    }
class Square
    {
    int[] coordinate;
    Point[] point = new Point[4];

        int [] GetCoordinate(string line)
        {
            string[] split = line.Split(new Char[] { ',', '(', ')', ' ' }, StringSplitOptions.RemoveEmptyEntries);
            int[] coordinates = new int[split.Length];
            for (int i = 0; i < split.Length; i++)
            {
              
                coordinates[i] = int.Parse(split[i]);
              
            }
            return coordinates;
        }

       public bool isSquare(string String)
       {
          
           coordinate = GetCoordinate(String);
           
           for (int i = 0, y = 0; i < coordinate.Length; i++, y++ )
           {
               point[y] = new Point(coordinate[i], coordinate[++i]);
           }
           

           if (((GetDistance(point[0], point[1]) > GetDistance(point[0], point[2]) && GetDistance(point[0], point[2]) == GetDistance(point[0], point[3])) ||
               (GetDistance(point[0], point[1]) < GetDistance(point[0], point[2]) && GetDistance(point[0], point[1]) == GetDistance(point[0], point[3])) ||
               (GetDistance(point[0], point[1]) == GetDistance(point[0], point[2]) && GetDistance(point[0], point[3]) > GetDistance(point[0], point[1]))) &&
               (GetDistance(point[1], point[0]) > GetDistance(point[1], point[2]) && GetDistance(point[1], point[2])==GetDistance(point[1],point[3]))||
               (GetDistance(point[1],point[0])<GetDistance(point[1],point[2]) && GetDistance(point[1],point[0])==GetDistance(point[1],point[3]))||
               (GetDistance(point[1],point[0])==GetDistance(point[1],point[2])&&GetDistance(point[1],point[3])>GetDistance(point[1],point[0])))
           {
               return true;
           }
           else
           {
               return false;
           }

       }

        double GetDistance(Point A, Point B)
       {
           return Math.Pow((B.X - A.X), 2) + Math.Pow((B.Y - A.Y), 2);
       }


    }
class Point
{
    public int X;
    public int Y;
    public Point()
    {
        X = 0;
        Y = 0;
    }
    public Point(int x, int y)
    {
        X = x;
        Y = y;
    }
}