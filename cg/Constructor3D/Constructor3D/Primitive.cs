using System;
using System.Collections.Generic;
using System.Text;

namespace Constructor3D
{
    abstract class Primitive : BaseObject
    {
        public Vector3 color = new Vector3(0, 0, 0);
        public double specular = 0;
        public double reflective = 0;
    }

}
