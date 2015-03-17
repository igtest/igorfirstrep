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
            
            Regex regex = new Regex(@"^[(]([0-9]),([0-9])[)],[(]([0-9]),([0-9])[)],[(]([0-9]),([0-9])[)],[(]([0-9]),([0-9])[)]");
            Regex regexWithSpace = new Regex(@"^[(]([0-9]),([0-9])[)],\s[(]([0-9]),([0-9])[)],\s[(]([0-9]),([0-9])[)],\s[(]([0-9]),([0-9])[)]");
            if (regex.IsMatch(line) || regexWithSpace.IsMatch(line))
            {
                return true;
            }
            else
            {
                Console.WriteLine("False");
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

       void SortPoint(Point[]point)
        {
           Point temp;
           for(int i = 0; i<point.Length-1; i++)
           {
              for (int j = i+1;j<point.Length;j++ )
              {
                  if(point[i]>point[j])
                  {
                      temp = new Point(point[j]);
                      point[j] = point[i];
                      point[i] = temp;
                  }
              }
           }

        }

       public bool isSquare(string String)
       {
           
           coordinate = GetCoordinate(String);
           
           for (int i = 0, y = 0; i < coordinate.Length; i++, y++ )
           {
               point[y] = new Point(coordinate[i], coordinate[++i]);
           }

           SortPoint(point);

           double SquareSide = GetDistance(point[0], point[1]);
           double SquareDiagonal = GetDistance(point[0], point[3]);

           if (SquareSide == GetDistance(point[0], point[2]) && SquareSide == GetDistance(point[2], point[3]) &&
               SquareSide == GetDistance(point[3], point[1]) && SquareDiagonal == GetDistance(point[2], point[1]))

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
           return Math.Pow(B.X - A.X, 2) + Math.Pow(B.Y - A.Y, 2);
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
    public Point(Point obj)
    {
        this.X = obj.X;
        this.Y = obj.Y;
    }
    public Point(int x, int y)
    {
        X = x;
        Y = y;
    }

    public static bool operator>(Point A, Point B)
    {
        if (A.X > B.X)
        {
            return true;
        }
        else if (A.X == B.X)
        {
            if (A.Y > B.Y)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        else
        {
            return false;
        }
    }
    public static bool operator<(Point A, Point B)
    {
        if (A.X < B.X)
        {
            return true;
        }
        else if (A.X == B.X)
        {
            if (A.Y < B.Y)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        else
        {
            return false;
        }
    }

}