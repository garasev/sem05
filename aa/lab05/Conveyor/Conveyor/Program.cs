using System;
using System.Collections.Generic;
using System.Threading;
using System.Diagnostics;

namespace Conveyor
{
    class Program
    {
        static void Main(string[] args)
        {
            Time(MainLoop, 10, 10000, 10000);
            Time(SimpleLoop, 10, 10000, 10000);
            Console.WriteLine("Hello World!");
        }

        static public void Time(Func<int, int, int, int> func, int elem_cnt, int elem_len, int repeat)
        {
            Stopwatch stopWatch = new Stopwatch();
            TimeSpan ts;
            stopWatch.Start();
            func(elem_cnt, elem_len, repeat);
            stopWatch.Stop();
            ts = stopWatch.Elapsed;
            string elapsedTime = String.Format("{0:00}:{1:00}.{2:00}",
                    ts.Minutes, ts.Seconds,
                    ts.Milliseconds / 10);
            Console.WriteLine("Время: " + elapsedTime);
        }

        static public int SimpleLoop(int elem_cnt, int elem_len, int repeat)
        {
            Queue<Element> q1 = new Queue<Element>();
            Queue<Element> q2 = new Queue<Element>();
            Queue<Element> q3 = new Queue<Element>();
            Queue<Element> q_finish = new Queue<Element>();

            FillQueue(ref q1, elem_cnt, elem_len);

            ConvA ca = new ConvA(ref q1, ref q2, repeat);
            ConvB cb = new ConvB(ref q2, ref q3, repeat);
            ConvC cc = new ConvC(ref q3, ref q_finish, repeat);

            while (true)
            {
                if (q1.Count != 0)
                {
                    ca.run();
                }
                else if (q2.Count != 0)
                {
                    cb.run();
                }
                else if (q3.Count != 0)
                {
                    cc.run();
                }
                else if (q_finish.Count == elem_cnt)
                    break;
            }

            return 0;
        }

        static public int MainLoop(int elem_cnt, int elem_len, int repeat)
        {
            Queue<Element> q1 = new Queue<Element>();
            Queue<Element> q2 = new Queue<Element>();
            Queue<Element> q3 = new Queue<Element>();
            Queue<Element> q_finish = new Queue<Element>();

            FillQueue(ref q1, elem_cnt, elem_len);

            ConvA ca = new ConvA(ref q1, ref q2, repeat);
            ConvB cb = new ConvB(ref q2, ref q3, repeat);
            ConvC cc = new ConvC(ref q3, ref q_finish, repeat);

            int conv_cnt = 3;

            Thread[] t = new Thread[conv_cnt];

            while (true)
            {
                if (t[0] is null)
                {
                    t[0] = new Thread(ca.run);
                    t[0].Start();
                } 
                else if (!t[0].IsAlive && q1.Count != 0)
                {
                    t[0] = new Thread(ca.run);
                    t[0].Start();
                }

                if (t[1] is null)
                {
                    if (q2.Count != 0)
                    { 
                        t[1] = new Thread(cb.run);
                        t[1].Start();
                    }
                }
                else if (!t[1].IsAlive && q2.Count != 0)
                {
                    t[1] = new Thread(cb.run);
                    t[1].Start();
                }

                if (t[2] is null)
                {
                    if (q3.Count != 0)
                    {
                        t[2] = new Thread(cc.run);
                        t[2].Start();
                    }
                }
                else if (!t[2].IsAlive && q3.Count != 0)
                {
                    t[2] = new Thread(cc.run);
                    t[2].Start();
                }
                if (q_finish.Count == elem_cnt)
                    break;
            }
            return 0;
        }

        static public void FillQueue(ref Queue<Element> queue, int cnt, int len)
        {
            for (int i = 0; i < cnt; i++)
            {
                queue.Enqueue(new Element(len));
            }
        }
    }
}
