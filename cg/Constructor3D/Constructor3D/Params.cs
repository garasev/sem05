using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Constructor3D
{
    class Params
    {
        public int width;
        public int height;
        public int start_x;
        public int start_y;
        public Params(int width, int height, int start_x, int start_y)
        {
            this.width = width;
            this.height = height;
            this.start_x = start_x;
            this.start_y = start_y;
        }
    }
}
