using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Constructor3D
{
    class Cylinder: Primitive
    {

        public double radius;
        public double length;
        public Vector3 dir = new Vector3(0, 0, 1);
        public DiskPlane disk1, disk2;

        public Cylinder(Vector3 position, Vector3 color, double radius, double length, double specular, double reflective)
        {
            this.position = position;
            this.color = color;
            this.radius = radius;
            this.length = length;
            this.specular = specular;
            this.reflective = reflective;
            this.disk1 = new DiskPlane(position, color, radius, specular, reflective);
            this.disk2 = new DiskPlane(position + dir * length, color, radius, specular, reflective);
        }
    }

    class DiskPlane : Primitive
    {
        public double radius;
        public Vector3 dir = new Vector3(0, 0, 1);
        public DiskPlane(Vector3 position, Vector3 color, double radius, double specular, double reflective)
        {
            this.position = position;
            this.color = color;
            this.radius = radius;
            this.specular = specular;
            this.reflective = reflective;
        }
    }
}
