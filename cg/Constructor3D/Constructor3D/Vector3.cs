using System;
using System.Collections.Generic;
using System.Text;

namespace Constructor3D
{
    class Vector3
    {
        public double x;
        public double y;
        public double z;

        // Constructor
        public Vector3()
        {
            this.x = 0;
            this.y = 0;
            this.z = 0;
        }
        public Vector3(Vector3 vec)
        {
            this.x = vec.x;
            this.y = vec.y;
            this.z = vec.z;
        }
        public Vector3(double x, double y, double z)
        {
            this.x = x;
            this.y = y;
            this.z = z;
        }

        //Operation
        public static Vector3 operator +(Vector3 v1, Vector3 v2)
        {
            return new Vector3 { x = v1.x + v2.x, y = v1.y + v2.y, z = v1.z + v2.z };
        }
        public static Vector3 operator /(Vector3 v1, double k)
        {
            return new Vector3 { x = v1.x / k, y = v1.y / k, z = v1.z / k };
        }

        public static Vector3 operator -(Vector3 v1, Vector3 v2)
        {
            return new Vector3 { x = v1.x - v2.x, y = v1.y - v2.y, z = v1.z - v2.z };
        }
        public static Vector3 operator -(Vector3 v)
        {
            return new Vector3 { x = -v.x, y = -v.y, z = -v.z };
        }

        public static Vector3 operator *(Vector3 v, double k)
        {
            return new Vector3 { x = v.x * k, y = v.y * k, z = v.z * k };
        }
        public static Vector3 operator *(double k, Vector3 v)
        {
            return new Vector3 { x = v.x * k, y = v.y * k, z = v.z * k };
        }

        public static double ScalarMultiplication(Vector3 a, Vector3 b)
        {
            return a.x * b.x + a.y * b.y + a.z * b.z;
        }

        public static double Length(Vector3 vec)
        {
            return Math.Sqrt(Vector3.ScalarMultiplication(vec, vec));
        }

        public Vector3 Normalize()
        {
            double length_vec = Math.Sqrt(this.x * this.x + this.y * this.y + this.z * this.z);
            return new Vector3(this.x / length_vec, this.y / length_vec, this.z / length_vec);
        }

        public static Vector3 operator *(Vector3 v, double[,] mtr)
        {
            double[] tmp = new double[4] { v.x, v.y, v.z, 1 };
            double[] result = new double[4] { 0, 0, 0, 0 };

            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    result[i] += tmp[j] * mtr[i, j];
                }
            }
            return new Vector3 { x = result[0], y = result[1], z = result[2] };
        }
    }
}
