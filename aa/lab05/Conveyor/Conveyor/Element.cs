using System;
using System.Collections.Generic;
using System.Text;

namespace Conveyor
{
    class Element
    {
        public int[] array;
        public int positive;
        public int negative;
        public int zero;

        public Element(int cnt)
        {
            array = new int[cnt];
            for (int i = 0; i < cnt; i++)
            {
                Random rnd = new Random();
                array[i] = rnd.Next(-10, 10);
            }
            this.positive = 0;
            this.negative = 0;
            this.zero = 0;
        }
    }

}
