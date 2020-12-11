using System.Collections.Generic;
using System.Drawing;

namespace Constructor3D
{
    class Scene
    {
        public Camera camera;
        public List<Primitive> primitives;
        public List<LightSource> light_sources;
        public LightSource ambient_light;
        public Size size;

        public Scene(Size size)
        {
            this.size = size;

            camera = new Camera(new Vector3(0, 0, -10), new Vector3());
            camera.calc_rotation();
            primitives = new List<Primitive>();
            light_sources = new List<LightSource>();
            ambient_light = new LightSource(new Vector3(), 0.2); //Диффузное освещение
        }

        public void add_ls(Vector3 position, double intensity)
        {
            light_sources.Add(new LightSource(position, intensity));
        }

        public void add_sphere(Vector3 position, double radius, Vector3 color, double specular, double reflective)
        {
            primitives.Add(new Sphere(position, radius, color, specular, reflective));
        }

        public void add_par(Vector3 position, Vector3 color, double height, double width, double length, double specular, double reflective)
        {
            primitives.Add(new Parallelepiped(position, color, height, width, length, specular, reflective));
        }

        public void add_cyl(Vector3 position, Vector3 color, double radius, double length, double specular, double reflective)
        {
            primitives.Add(new Cylinder(position, color, radius, length, specular, reflective));
        }

        public void add_pyr(Vector3 position, Vector3 color, double height, double width, double specular, double reflective)
        {
            primitives.Add(new Pyramid(position, color, height, width, specular, reflective));
        }
    }
}
