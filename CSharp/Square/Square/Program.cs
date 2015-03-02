using System;
using System.IO;

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
                    if (lineOfText != null)
                    {
                        Console.WriteLine(a.isSquare(lineOfText));
                    
                    }
                }
            }
            catch (System.IndexOutOfRangeException)
            {
                Console.WriteLine("Input filename...");
            }
                }
    }
class Square
    {
    int[] coordinate;
    Point P0, P1, P2, P3;

        int [] GetCoordinate(string line)
        {
            string[] split = line.Split(new Char[] { ',', '(', ')', ' ' }, StringSplitOptions.RemoveEmptyEntries);
            int[] coordinat = new int[split.Length];
            //Console.WriteLine("Numbers of length: " + split.Length);
            for (int i = 0; i < split.Length; i++)
            {
                try
                {
                    coordinat[i] = int.Parse(split[i]);
                    // Console.WriteLine(split[i]);
                }
                catch (System.FormatException)
                {
                    Console.WriteLine("Check imput data...");
                    break;
                }
            }
            return coordinat;
        }

       public bool isSquare(string String)
       {
          
           coordinate = GetCoordinate(String);
           
           P0 = new Point(coordinate[0], coordinate[1]);
           P1 = new Point(coordinate[2], coordinate[3]);
           P2 = new Point(coordinate[4], coordinate[5]);
           P3 = new Point(coordinate[6], coordinate[7]);

           double dist1, dist2, dist3;
           dist1 = GetDistance(P0, P1);
           dist2 = GetDistance(P0, P2);
           dist3 = GetDistance(P0, P3);

           if (((dist1>dist2 && dist2 == dist3)||(dist1<dist2 && dist1 == dist3)||(dist1==dist2 && dist3>dist1))&&
               (GetDistance(P1, P0) > GetDistance(P1, P2) && GetDistance(P1, P2)==GetDistance(P1,P3))||
               (GetDistance(P1,P0)<GetDistance(P1,P2) && GetDistance(P1,P0)==GetDistance(P1,P3))||
               (GetDistance(P1,P0)==GetDistance(P1,P2)&&GetDistance(P1,P3)>GetDistance(P1,P0)))
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