using System;
using System.Collections.Generic;
using System.Text;

namespace Conveyor
{
    class ConvA
    {
        public Queue<Element> q_in = new Queue<Element>();
        public Queue<Element> q_out = new Queue<Element>();

        public int repeat;
        public int pass_cnt;

        public ConvA(ref Queue<Element> q_in, ref Queue<Element> q_out, int repeat)
        {
            this.q_in = q_in;
            this.q_out = q_out;

            this.repeat = repeat;
            this.pass_cnt = 0;
        }
        public void run()
        {
            int t1 = DateTime.Now.Minute;
            int t2 = DateTime.Now.Second;
            int t3 = DateTime.Now.Millisecond / 10;
            Element a = q_in.Dequeue();
            this.pass_cnt += 1;
            for (int repeat = 1; repeat <= this.repeat; repeat++)
            {
                a.positive = 0;
                for (int i = 0; i < a.array.Length; i++)
                {
                    if (a.array[i] > 0)
                    {
                        a.positive += 1;
                    }
                }
            }
            Console.WriteLine("[{0:00}:{1:00}.{2:00} - {3:00}:{4:00}.{5:00}] Conv #1: element #{6:00} count {7} pos number",
                t1, t2, t3,
                DateTime.Now.Minute, DateTime.Now.Second, DateTime.Now.Millisecond / 10, this.pass_cnt, a.positive);
            q_out.Enqueue(a);
        }
    }

    class ConvB
    {
        public Queue<Element> q_in = new Queue<Element>();
        public Queue<Element> q_out = new Queue<Element>();

        public int repeat;
        public int pass_cnt;

        public ConvB(ref Queue<Element> q_in, ref Queue<Element> q_out, int repeat)
        {
            this.q_in = q_in;
            this.q_out = q_out;

            this.repeat = repeat;
            this.pass_cnt = 0;
        }
        public void run()
        {
            int t1 = DateTime.Now.Minute;
            int t2 = DateTime.Now.Second;
            int t3 = DateTime.Now.Millisecond / 10;
            Element a = q_in.Dequeue();
            this.pass_cnt += 1;
            for (int repeat = 1; repeat <= this.repeat; repeat++)
            {
                a.negative = 0;
                for (int i = 0; i < a.array.Length; i++)
                {
                    if (a.array[i] < 0)
                    {
                        a.negative += 1;
                    }
                }
            }
            Console.WriteLine("[{0:00}:{1:00}.{2:00} - {3:00}:{4:00}.{5:00}] Conv #2: element #{6:00} count {7} neg number",
                t1, t2, t3,
                DateTime.Now.Minute, DateTime.Now.Second, DateTime.Now.Millisecond / 10, this.pass_cnt, a.negative);
            q_out.Enqueue(a);
        }
    }

    class ConvC
    {
        public Queue<Element> q_in = new Queue<Element>();
        public Queue<Element> q_out = new Queue<Element>();

        public int repeat;
        public int pass_cnt;

        public ConvC(ref Queue<Element> q_in, ref Queue<Element> q_out, int repeat)
        {
            this.q_in = q_in;
            this.q_out = q_out;

            this.repeat = repeat;
            this.pass_cnt = 0;
        }

        public void run()
        {
            int t1 = DateTime.Now.Minute;
            int t2 = DateTime.Now.Second;
            int t3 = DateTime.Now.Millisecond / 10;
            Element a = q_in.Dequeue();
            this.pass_cnt += 1;
            for (int repeat = 1; repeat <= this.repeat; repeat++)
            {
                a.zero = 0;
                for (int i = 0; i < a.array.Length; i++)
                {
                    if (a.array[i] == 0)
                    {
                        a.zero += 1;
                    }
                }
            }
            bool tmp = (a.zero == (a.array.Length - a.positive - a.negative));
            Console.WriteLine("[{0:00}:{1:00}.{2:00} - {3:00}:{4:00}.{5:00}] Conv #3: element #{6:00} count {7} zero number. It's {8}",
                t1, t2, t3,
                DateTime.Now.Minute, DateTime.Now.Second, DateTime.Now.Millisecond / 10, this.pass_cnt, a.zero, tmp);
            q_out.Enqueue(a);
        }
    }
}
