using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Runtime.Remoting.Metadata.W3cXsd2001;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Collections;
using System.Runtime.CompilerServices;
using System.Threading;

namespace Constructor3D
{
    class RayTracer
    {
        public Bitmap bmp;
        private Scene scene;

        private int thread_count = 4;

        private int Vh = 1;
        private int Vw = 1;
        private int d = 1;

        private Color[,] buffer;

        private double[,] rotation_matr = new double[4, 4] { { 1, 0, 0, 0 }, { 0, 1, 0, 0 }, { 0, 0, 1, 0 }, { 0, 0, 0, 1 } };

        public RayTracer(Scene scene)
        {
            this.scene = scene;
            bmp = new Bitmap(scene.size.Width, scene.size.Height);
            buffer = new Color[scene.size.Width, scene.size.Height];

            render();
        }

        public Color Clamp(Vector3 color)
        {
            int color_x = Math.Min(255, Math.Max(0, (int)color.x));
            int color_y = Math.Min(255, Math.Max(0, (int)color.y));
            int color_z = Math.Min(255, Math.Max(0, (int)color.z));
            return Color.FromArgb(color_x, color_y, color_z);
        }

        public void intersect_ray_sphere(Vector3 position, Vector3 dir, Sphere sphere, ref double t1, ref double t2)
        {
            Vector3 CO = position - sphere.position;

            double a = Vector3.ScalarMultiplication(dir, dir);
            double b = 2 * Vector3.ScalarMultiplication(CO, dir);
            double c = Vector3.ScalarMultiplication(CO, CO) - sphere.radius * sphere.radius;


            double discriminant = b * b - 4 * a * c;

            if (discriminant < 0)
            {
                t1 = Double.PositiveInfinity;
                t2 = Double.PositiveInfinity;
                return;
            }

            t1 = (-b + Math.Sqrt(discriminant)) / (2 * a);
            t2 = (-b - Math.Sqrt(discriminant)) / (2 * a);
        }

        private void IntersectRayPlane(Vector3 O, Vector3 D, Vector3 C, Vector3 V, ref double t)
        {
            Vector3 CO = O - C;

            double d_v = Vector3.ScalarMultiplication(D, V);
            double co_v = Vector3.ScalarMultiplication(CO, V);

            if (d_v < 0 || d_v > 0)
            {
                t = -co_v / d_v;
                if (t < 0)
                    t = Double.PositiveInfinity;

            }
            else
            {
                t = Double.PositiveInfinity;
            }
        }

        private void IntersectRayDiskPlane(Vector3 O, Vector3 D, Vector3 C, Vector3 V, double r, ref double t)
        {
            IntersectRayPlane(O, D, C, V, ref t);

            if (t != Double.PositiveInfinity)
            {
                Vector3 P = O + D * t;
                Vector3 v = P - C;
                double d2 = Vector3.ScalarMultiplication(v, v);
                if (Math.Sqrt(d2) > r)
                    t = Double.PositiveInfinity;
            }
            else
            {
                t = Double.PositiveInfinity;
            }
        }

        private void IntersectRayParallelepiped(Vector3 O, Vector3 D, Parallelepiped parallelepiped, ref double t1ret, ref double t2ret)
        {
            double t1, t2;
            double tnear = Double.NegativeInfinity;
            double tfar = Double.PositiveInfinity;

            if (Math.Abs(D.x) < 0.001)
            {
                if (O.x < parallelepiped.start.x || O.x > parallelepiped.end.x)
                {
                    t1ret = Double.PositiveInfinity;
                    t2ret = Double.NegativeInfinity;
                    return;
                }

            }
            else
            {

                t1 = (parallelepiped.start.x - O.x) / D.x;
                t2 = (parallelepiped.end.x - O.x) / D.x;
                if (t1 > t2)
                {
                    double tmp = t1;
                    t1 = t2;
                    t2 = tmp;
                }
                if (t1 > tnear) tnear = t1;
                if (t2 < tfar) tfar = t2;
                if (tnear > tfar)
                {
                    t1ret = Double.PositiveInfinity;
                    t2ret = Double.NegativeInfinity;
                    return;
                }
                if (tfar < 0)
                {
                    t1ret = Double.PositiveInfinity;
                    t2ret = Double.NegativeInfinity;
                    return;
                }
            }

            if (Math.Abs(D.y) < 0.001)
            {
                if (O.y < parallelepiped.start.y || O.y > parallelepiped.end.y)
                {
                    t1ret = Double.PositiveInfinity;
                    t2ret = Double.NegativeInfinity;
                    return;
                }
            }
            else
            {

                t1 = (parallelepiped.start.y - O.y) / D.y;
                t2 = (parallelepiped.end.y - O.y) / D.y;
                if (t1 > t2)
                {
                    double tmp = t1;
                    t1 = t2;
                    t2 = tmp;
                }
                if (t1 > tnear) tnear = t1;
                if (t2 < tfar) tfar = t2;
                if (tnear > tfar)
                {
                    t1ret = Double.PositiveInfinity;
                    t2ret = Double.NegativeInfinity;
                    return;
                }
                if (tfar < 0)
                {
                    t1ret = Double.PositiveInfinity;
                    t2ret = Double.NegativeInfinity;
                    return;
                }
            }
            if (Math.Abs(D.z) < 0.001)
            {
                if (O.z < parallelepiped.start.z || O.z > parallelepiped.end.z)
                {
                    t1ret = Double.PositiveInfinity;
                    t2ret = Double.NegativeInfinity;
                    return;
                }
            }
            else
            {

                t1 = (parallelepiped.start.z - O.z) / D.z;
                t2 = (parallelepiped.end.z - O.z) / D.z;
                if (t1 > t2)
                {
                    double tmp = t1;
                    t1 = t2;
                    t2 = tmp;
                }
                if (t1 > tnear) tnear = t1;
                if (t2 < tfar) tfar = t2;
                if (tnear > tfar)
                {
                    t1ret = Double.PositiveInfinity;
                    t2ret = Double.NegativeInfinity;
                    return;
                }
                if (tfar < 0)
                {
                    t1ret = Double.PositiveInfinity;
                    t2ret = Double.NegativeInfinity;
                    return;
                }
            }
            t1ret = tnear;
            t2ret = tfar;
        }

        private void IntersectRayCylinder(Vector3 O, Vector3 D, Cylinder cylinder, ref double t1, ref double t2)
        {
            Vector3 CO = O - cylinder.position;

            double d_d = Vector3.ScalarMultiplication(D, D);
            double d_co = Vector3.ScalarMultiplication(D, CO);
            double co_co = Vector3.ScalarMultiplication(CO, CO);
            double d_v = Vector3.ScalarMultiplication(D, cylinder.dir);
            double co_v = Vector3.ScalarMultiplication(CO, cylinder.dir);

            double a = d_d - d_v * d_v;
            double b = 2 * (d_co - d_v * co_v);
            double c = co_co - co_v * co_v - cylinder.radius * cylinder.radius;


            double discriminant = b * b - 4 * a * c;

            if (discriminant < 0)
            {
                t1 = Double.PositiveInfinity;
                t2 = Double.PositiveInfinity;
                return;
            }

            t1 = (-b + Math.Sqrt(discriminant)) / (2 * a);
            t2 = (-b - Math.Sqrt(discriminant)) / (2 * a);


            double m1 = d_v * t1 + co_v;
            double m2 = d_v * t2 + co_v;

            if (m1 < 0 || m1 > cylinder.length)
            {
                t1 = Double.PositiveInfinity;
            }
            if (m2 < 0 || m2 > cylinder.length)
            {
                t2 = Double.PositiveInfinity;
            }
        }

        private void IntersectRayTriangle(Vector3 O, Vector3 D, Vector3 v0, Vector3 v1, Vector3 v2, ref double t1)
        {
            Vector3 e1 = v1 - v0;
            Vector3 e2 = v2 - v0;

            Vector3 pvec = new Vector3(D.y * e2.z - D.z * e2.y, D.z * e2.x - D.x * e2.z, D.x * e2.y - D.y * e2.x);
            double det = Vector3.ScalarMultiplication(e1, pvec);

            // Луч параллелен плоскости
            if (det < 1e-8 && det > -1e-8)
            {
                t1 = Double.PositiveInfinity;
                return;
            }

            double inv_det = 1 / det;
            Vector3 tvec = O - v0;
            double u = Vector3.ScalarMultiplication(tvec, pvec) * inv_det;
            if (u < 0 || u > 1)
            {
                t1 = Double.PositiveInfinity;
                return;
            }
            Vector3 qvec = new Vector3(tvec.y * e1.z - tvec.z * e1.y, tvec.z * e1.x - tvec.x * e1.z, tvec.x * e1.y - tvec.y * e1.x);

            double v = Vector3.ScalarMultiplication(D, qvec) * inv_det;

            if (v < 0 || u + v > 1)
            {
                t1 = Double.PositiveInfinity;
                return;
            }

            t1 = Vector3.ScalarMultiplication(e2, qvec) * inv_det;
        }

        public void PutPixel(int x, int y, Color color)
        {
            int x_ = scene.size.Width / 2 + x;
            int y_ = scene.size.Height / 2 - y - 1;

            if (x_ < 0 || x_ >= scene.size.Width || y_ < 0 || y_ >= scene.size.Height)
                return;

            this.buffer[x_, y_] = color;
        }

        public void render_thread(object obj)
        {
            Params p = (Params)obj;
            Vector3 dir = null;
            Vector3 color = null;

            for (int x = p.start_x; x < p.start_x + p.width; x++)
            {
                for (int y = p.start_y; y < p.start_y + p.height; y++)
                {
                    dir = CanvasToViewport(x, y) * scene.camera.rotation;
                    Transformer.MultiplyMV(rotation_matr, ref dir);
                    color = TraceRay(scene.camera.position, dir, 1, Double.PositiveInfinity, x, y);
                    PutPixel(x, y, Clamp(color));

                }
            }
        }

        public void IntersectRayPyramid(ref Primitive closest_object, ref double closest_t, Vector3 camera, Vector3 dir, double t_min, double t_max, Pyramid pyramid, ref double t1, ref double t2)
        {
            IntersectRayTriangle(camera, dir, pyramid.t1.position, pyramid.t1.A, pyramid.t1.B, ref t1);
            t2 = t1;
            if (t1 < closest_t && t_min < t1 && t1 < t_max)
            {
                closest_t = t1;
                closest_object = pyramid.t1;
            }
            if (t2 < closest_t && t_min < t2 && t2 < t_max)
            {
                closest_t = t2;
                closest_object = pyramid.t1;
            }
            IntersectRayTriangle(camera, dir, pyramid.t2.position, pyramid.t2.A, pyramid.t2.B, ref t1);
            t2 = t1;
            if (t1 < closest_t && t_min < t1 && t1 < t_max)
            {
                closest_t = t1;
                closest_object = pyramid.t2;
            }
            if (t2 < closest_t && t_min < t2 && t2 < t_max)
            {
                closest_t = t2;
                closest_object = pyramid.t2;
            }
            IntersectRayTriangle(camera, dir, pyramid.t3.position, pyramid.t3.A, pyramid.t3.B, ref t1);
            t2 = t1;
            if (t1 < closest_t && t_min < t1 && t1 < t_max)
            {
                closest_t = t1;
                closest_object = pyramid.t3;
            }
            if (t2 < closest_t && t_min < t2 && t2 < t_max)
            {
                closest_t = t2;
                closest_object = pyramid.t3;
            }
            IntersectRayTriangle(camera, dir, pyramid.t4.position, pyramid.t4.A, pyramid.t4.B, ref t1);
            t2 = t1;
            if (t1 < closest_t && t_min < t1 && t1 < t_max)
            {
                closest_t = t1;
                closest_object = pyramid.t4;
            }
            if (t2 < closest_t && t_min < t2 && t2 < t_max)
            {
                closest_t = t2;
                closest_object = pyramid.t4;
            }
            IntersectRayTriangle(camera, dir, pyramid.t5.position, pyramid.t5.A, pyramid.t5.B, ref t1);
            t2 = t1;
            if (t1 < closest_t && t_min < t1 && t1 < t_max)
            {
                closest_t = t1;
                closest_object = pyramid.t5;
            }
            if (t2 < closest_t && t_min < t2 && t2 < t_max)
            {
                closest_t = t2;
                closest_object = pyramid.t5;
            }
            IntersectRayTriangle(camera, dir, pyramid.t6.position, pyramid.t6.A, pyramid.t6.B, ref t1);
            t2 = t1;
            if (t1 < closest_t && t_min < t1 && t1 < t_max)
            {
                closest_t = t1;
                closest_object = pyramid.t6;
            }
            if (t2 < closest_t && t_min < t2 && t2 < t_max)
            {
                closest_t = t2;
                closest_object = pyramid.t6;
            }

        }

        public void ClosestIntersection(ref Primitive closest_object, ref double closest_t, Vector3 camera, Vector3 dir, double t_min, double t_max)
        {
            List<Primitive> scene_object = scene.primitives;
            double t1 = 0;
            double t2 = 0;

            for (int i = 0; i < scene_object.Count; i++)
            {
                if (scene_object[i] is Sphere)
                {
                    intersect_ray_sphere(camera, dir, (Sphere)scene_object[i], ref t1, ref t2);
                }
                else if (this.scene.primitives[i] is Parallelepiped)
                {
                    IntersectRayParallelepiped(camera, dir, (Parallelepiped)this.scene.primitives[i], ref t1, ref t2);

                }
                else if (this.scene.primitives[i] is Cylinder)
                {
                    Cylinder tmp = (Cylinder)this.scene.primitives[i];
                    IntersectRayCylinder(camera, dir, tmp, ref t1, ref t2);
                    if (t1 < closest_t && t_min < t1 && t1 < t_max)
                    {
                        closest_t = t1;
                        closest_object = scene_object[i];
                    }
                    if (t2 < closest_t && t_min < t2 && t2 < t_max)
                    {
                        closest_t = t2;
                        closest_object = scene_object[i];
                    }
                    IntersectRayDiskPlane(camera, dir, tmp.disk1.position, tmp.disk1.dir, tmp.radius, ref t1);
                    t2 = t1;
                    if (t1 < closest_t && t_min < t1 && t1 < t_max)
                    {
                        closest_t = t1;
                        closest_object = scene_object[i];
                    }
                    if (t2 < closest_t && t_min < t2 && t2 < t_max)
                    {
                        closest_t = t2;
                        closest_object = scene_object[i];
                    }
                    IntersectRayDiskPlane(camera, dir, tmp.disk2.position, tmp.disk2.dir, tmp.radius, ref t1);
                    t2 = t1;
                    if (t1 < closest_t && t_min < t1 && t1 < t_max)
                    {
                        closest_t = t1;
                        closest_object = scene_object[i];
                    }
                    if (t2 < closest_t && t_min < t2 && t2 < t_max)
                    {
                        closest_t = t2;
                        closest_object = scene_object[i];
                    }
                }
                else if (this.scene.primitives[i] is Pyramid)
                {
                    IntersectRayPyramid(ref closest_object,ref closest_t, camera, dir, t_min, t_max, (Pyramid)this.scene.primitives[i], ref t1, ref t2);
                }

                if (t1 < closest_t && t_min < t1 && t1 < t_max)
                {
                    closest_t = t1;
                    closest_object = scene_object[i];
                }
                if (t2 < closest_t && t_min < t2 && t2 < t_max)
                {
                    closest_t = t2;
                    closest_object = scene_object[i];
                }
            }
        }

        private double ComputeLighting(Vector3 P, Vector3 N, Vector3 V, double specular)
        {
            double intensity = scene.ambient_light.intensity;
            List<LightSource> sceneLight = scene.light_sources;

            for (int i = 0; i < sceneLight.Count; i++)
            {
                Vector3 L;
                L = sceneLight[i].position - P;

                double n_dot_l = Vector3.ScalarMultiplication(N, L);

                if (n_dot_l > 0)
                {
                    intensity += sceneLight[i].intensity * n_dot_l / (Vector3.Length(N) * Vector3.Length(L));
                }
            }
            return intensity;
        }

        public Vector3 TraceRay(Vector3 camera, Vector3 D, double t_min, double t_max, int x, int y)
        {
            double closest_t = Double.PositiveInfinity;
            Primitive closest_object = null;

            ClosestIntersection(ref closest_object, ref closest_t, camera, D, t_min, t_max);

            if (closest_object == null)
                return new Vector3();


            Vector3 P = camera + closest_t * D;  // вычисление пересечения
            Vector3 N;
            if (closest_object is Parallelepiped)
                N = Vec3dNormalParallelepiped(P, (Parallelepiped)closest_object);
            else if (closest_object is Cylinder)
                N = Vec3dNormalCylinder(P, closest_t, (Cylinder)closest_object, camera, D);
            else if (closest_object is DiskPlane)
            {
                DiskPlane tmp = (DiskPlane)closest_object;
                N = tmp.dir;
            }
            else if (closest_object is Triangle)
                N = Vec3dNormalTriangle((Triangle)closest_object);
            else
                N = P - closest_object.position; // вычисление нормали сферы в точке пересечения
            N = N / Vector3.Length(N);

            double intensity = ComputeLighting(P, N, -D, closest_object.specular);

            return intensity * closest_object.color;
        }

        private Vector3 Vec3dNormalParallelepiped(Vector3 P, Parallelepiped parallelepiped)
        {
            Vector3 size = parallelepiped.end - parallelepiped.start;
            Vector3 C = parallelepiped.end + parallelepiped.start;
            C = C * 0.5;


            Vector3 localPoint = P - C;
            Vector3 normal = new Vector3(1, 0, 0);

            normal.x = normal.x * Math.Sign(localPoint.x);
            double distance = Math.Abs(size.x - Math.Abs(localPoint.x));
            double min = distance;

            distance = Math.Abs(size.y - Math.Abs(localPoint.y));

            if (distance < min)
            {
                min = distance;

                normal = new Vector3(0, 1, 0);

                normal.y = normal.y * Math.Sign(localPoint.y);

            }
            distance = Math.Abs(size.z - Math.Abs(localPoint.z));
            if (distance < min)
            {
                min = distance;
                normal = new Vector3(0, 0, 1);

                normal.z = normal.z * Math.Sign(localPoint.z);
            }
            return normal;

        }

        private Vector3 Vec3dNormalCylinder(Vector3 P, double closest_t, Cylinder cylinder, Vector3 O, Vector3 D)
        {

            Vector3 CO = O - cylinder.position;


            double d_v = Vector3.ScalarMultiplication(D, new Vector3(0, 0, 1));
            double co_v = Vector3.ScalarMultiplication(CO, new Vector3(0, 0, 1));

            double m = d_v * closest_t + co_v;
            Vector3 normal = P;
            normal = normal - cylinder.position;
            normal = normal - new Vector3(0, 0, 1) * m;
            return normal;

        }

        private Vector3 Vec3dNormalTriangle(Triangle closest_object)
        {
            Vector3 e1 = closest_object.A - closest_object.position;
            Vector3 e2 = closest_object.B - closest_object.position;
            Vector3 normal = new Vector3(e1.y * e2.z - e1.z * e2.y, e1.z * e2.x - e1.x * e2.z, e1.x * e2.y - e1.y * e2.x);
            double len_n = Vector3.Length(normal);
            normal = normal / len_n;
            return normal;
        }


        public void render()
        {
            Thread[] threads = new Thread[thread_count];
            scene.camera.calc_rotation();
            buffer = new Color[scene.size.Width, scene.size.Height];
            for (int i = 0; i < thread_count; i++)
            {
                Params p = new Params(scene.size.Width / thread_count, 
                    scene.size.Height, 
                    -scene.size.Width / 2 + scene.size.Width / thread_count * i, 
                    -scene.size.Height / 2);

                threads[i] = new Thread(render_thread);
                threads[i].Start(p);
            }
            foreach (Thread thread in threads)
            {
                thread.Join();
            }

            for (int i = 0; i < scene.size.Width; i++)
                for (int j = 0; j < scene.size.Height; j++)
                    this.bmp.SetPixel(i, j, buffer[i, j]);
        }
        public Vector3 CanvasToViewport(int x, int y)
        {
            return new Vector3(x * (double)Vw / scene.size.Width, y * (double)Vh / scene.size.Height, d);
        }
    }
}
