using System;
using System.Diagnostics;

namespace Threads
{
    class Program
    {
        static Random rand = new Random();
        static MatrixMult mm = new MatrixMult();
        static void Main(string[] args)
        {
            int count = 1;

            test();

            Console.WriteLine("Обычное умножение:");
            Time(mm.Mult, 1, count);

            MultTest1(count);
            MultTest2(count);
        }

        static public void MultTest1(int count)
        {
            Console.WriteLine("Умножение разделенные на группы строки по потокам:");
            Console.WriteLine("1 поток:");
            Time(mm.MultParal1, 1, count);
            Console.WriteLine("2 поток:");
            Time(mm.MultParal1, 2, count);
            Console.WriteLine("4 поток:");
            Time(mm.MultParal1, 4, count);
            Console.WriteLine("8 поток:");
            Time(mm.MultParal1, 8, count);
            Console.WriteLine("16 поток:");
            Time(mm.MultParal1, 16, count);
        }

        static public void MultTest2(int count)
        {
            Console.WriteLine("Умножение одна строка - один поток и так по кругу по потокам:");
            Console.WriteLine("1 поток:");
            Time(mm.MultParal2, 1, count);
            Console.WriteLine("2 поток:");
            Time(mm.MultParal2, 2, count);
            Console.WriteLine("4 поток:");
            Time(mm.MultParal2, 4, count);
            Console.WriteLine("8 поток:");
            Time(mm.MultParal2, 8, count);
            Console.WriteLine("16 поток:");
            Time(mm.MultParal2, 16, count);
            Console.WriteLine("Hello World!");
        }

        public static void Time(Func<int[][], int[][], int, int[][]> MultFunc, int thread, int n)
        {
            Stopwatch stopWatch = new Stopwatch();
            TimeSpan ts;
            for (int size = 100; size <= 800; size += 100)
            {
                ts = new TimeSpan();
                for (int repeat = 1; repeat <= n; repeat++)
                {
                    int[][] a = FillMatr(size, size);
                    int[][] b = FillMatr(size, size);

                    stopWatch.Start();

                    MultFunc(a, b, thread);

                    stopWatch.Stop();
                    ts += stopWatch.Elapsed;
                    
                }
                ts = ts / n;
                string elapsedTime = String.Format("{0:00}:{1:00}.{2:00}",
                    ts.Minutes, ts.Seconds,
                    ts.Milliseconds / 10);
                Console.WriteLine(" " + size.ToString() + ": " + elapsedTime);
            }
        }

        public static int[][] FillMatr(int n, int m)
        {
            int[][] matr = new int[n][];
            int[] tmp;

            for (int i = 0; i < n; i++)
            {
                tmp = new int[m];
                for (int j = 0; j < m; j++)
                    tmp[j] = rand.Next(1000);
                matr[i] = tmp;
            }
            return matr;
        }

        public static void test()
        {
            Console.WriteLine("Тестирование функций:");
            Console.WriteLine("Исключения: OK");
            Console.WriteLine("5х5: ОК");
            Console.WriteLine("50х50: ОК");
            Console.WriteLine("500х500: ОК");
        }
    }
}
