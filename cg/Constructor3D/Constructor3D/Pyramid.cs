using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Constructor3D
{
    class Pyramid: Primitive
    {
        public double height;
        public double width;

        public Triangle t1, t2, t3, t4, t5, t6;

        public Pyramid(Vector3 position,Vector3 color, double height, double width, double specular, double reflective)
        {
            this.position = position;
            this.color = color;
            this.height = height;
            this.width = width;
            this.specular = specular;
            this.reflective = reflective;

            Vector3 p = position + new Vector3(0, 0, 1) * height;
            Vector3 a = position + new Vector3(-width / 2, -width / 2, 0);
            Vector3 b = position + new Vector3(-width / 2, width / 2, 0);
            Vector3 c = position + new Vector3(width / 2, width / 2, 0);
            Vector3 d = position + new Vector3(width / 2, -width / 2, 0);

            this.t1 = new Triangle(p, color, a, b, specular, reflective);
            this.t2 = new Triangle(p, color, b, c, specular, reflective);
            this.t3 = new Triangle(p, color, c, d, specular, reflective);
            this.t4 = new Triangle(p, color, d, a, specular, reflective);

            this.t5 = new Triangle(a, color, b, c, specular, reflective);
            this.t6 = new Triangle(a, color, d, c, specular, reflective);
        }
    }
    class Triangle : Primitive
    {
        public Vector3 A;
        public Vector3 B;

        public Triangle(Vector3 position, Vector3 color, Vector3 A, Vector3 B, double specular, double reflective)
        {
            this.position = position;
            this.color = color;
            this.A = A;
            this.B = B;
            this.specular = specular;
            this.reflective = reflective;
        }
    }
}
