using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace Threads
{
    class MatrixMult
    {
        public int[][] Mult(int[][] ma1, int[][] ma2, int thread_count)
        {
            int n1 = ma1.Length;
            int n2 = ma2.Length;

            if (n1 == 0 || n2 == 0)
                return null;

            int m1 = ma1[0].Length;
            int m2 = ma2[0].Length;

            if (m1 != n2)
                return null;

            int[][] res = new int[n1][];
            for (int i = 0; i < n1; i++)
                res[i] = new int[m2];

            for (int i = 0; i < n1; i++)
                for (int j = 0; j < m2; j++)
                    for (int k = 0; k < m1; k++)
                        res[i][j] += ma1[i][k] * ma2[k][j];

            return res;
        }

        public void MultNline(object obj)
        {
            Params p = (Params)obj;

            for (int i = p.str; i < p.end; i++)
                for (int j = 0; j < p.matr2[0].Length; j++)
                    for (int k = 0; k < p.matr1[0].Length; k++)
                        p.res[i][j] += p.matr1[i][k] * p.matr2[k][j];
        }

        public int[][] MultParal1(int[][] ma1, int[][] ma2, int thread_cnt)
        {
            int n1 = ma1.Length;
            int n2 = ma2.Length;

            if (n1 == 0 || n2 == 0)
                return null;

            int m1 = ma1[0].Length;
            int m2 = ma2[0].Length;

            if (m1 != n2)
                return null;

            int[][] res = new int[n1][];
            for (int i = 0; i < n1; i++)
                res[i] = new int[m2];

            Thread[] t = new Thread[thread_cnt];

            int thread_rows = n1 / thread_cnt;
            int str = 0;

            for (int i = 0; i < thread_cnt; i++)
            {
                int end = str + thread_rows;
                if (i == thread_cnt - 1)
                    end = n1;

                Params p = new Params(res, ma1, ma2, str, end);

                t[i] = new Thread(MultNline);
                t[i].Start(p);

                str = end;
            }

            foreach (Thread thread in t)
            {
                thread.Join();
            }
            return res;
        }

        public void MultLine(object obj)
        {
            Params p = (Params)obj;

            for (int j = 0; j < p.matr2[0].Length; j++)
                for (int k = 0; k < p.matr1[0].Length; k++)
                    p.res[p.str][j] += p.matr1[p.str][k] * p.matr2[k][j];
        }

        public int[][] MultParal2(int[][] ma1, int[][] ma2, int thread_cnt)
        {
            int n1 = ma1.Length;
            int n2 = ma2.Length;

            if (n1 == 0 || n2 == 0)
                return null;

            int m1 = ma1[0].Length;
            int m2 = ma2[0].Length;

            if (m1 != n2)
                return null;

            int[][] res = new int[n1][];
            for (int i = 0; i < n1; i++)
                res[i] = new int[m2];

            Thread[] t = new Thread[thread_cnt];

            for (int i = 0; i < thread_cnt; i++)
            {
                Params p = new Params(res, ma1, ma2, i);
                t[i] = new Thread(MultLine);
                t[i].Start(p);
            }

            for (int i = thread_cnt; i < n1; i++)
            {
                Params p = new Params(res, ma1, ma2, i);

                t[i % thread_cnt].Join();
                t[i % thread_cnt] = new Thread(MultLine);
                t[i % thread_cnt].Start(p);
            }

            foreach (Thread thread in t)
            {
                thread.Join();
            }
            return res;
        }
    }

    class Params
    {
        public int[][] res;
        public int[][] matr1, matr2;
        public int str, end;

        public Params(int[][] res, int[][] matr1, int[][] matr2, int str, int end)
        {
            this.res = res;

            this.matr1 = matr1;
            this.matr2 = matr2;

            this.str = str;
            this.end = end;
        }

        public Params(int[][] res, int[][] matr1, int[][] matr2, int str)
        {
            this.res = res;

            this.matr1 = matr1;
            this.matr2 = matr2;

            this.str = str;
        }
    }
}
