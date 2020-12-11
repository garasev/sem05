using System;
using System.Collections.Generic;
using System.Text;

namespace Constructor3D
{
    class Sphere: Primitive
    {
        public double radius;

        public Sphere(Vector3 position, double radius, Vector3 color, double specular, double reflective)
        {
            this.position = position;
            this.radius = radius;
            this.color = color;
            this.specular = specular;
            this.reflective = reflective;
        }
    }
}
