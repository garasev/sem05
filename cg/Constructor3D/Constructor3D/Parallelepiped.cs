using System;
using System.Collections.Generic;
using System.Text;

namespace Constructor3D
{
    class Parallelepiped: Primitive
    {
        public double height;
        public double width;
        public double length;

        public Vector3 start;
        public Vector3 end;

        public Parallelepiped(Vector3 position, Vector3 color, double height, double width, double length, double specular, double reflective)
        {
            this.position = position;
            this.color = color;
            this.height = height;
            this.width = width;
            this.length = length;
            this.specular = specular;
            this.reflective = reflective;

            this.start = position - new Vector3(height / 2, width / 2, length / 2);
            this.end = position + new Vector3(height / 2, width / 2, length / 2);
        }
    }
}
