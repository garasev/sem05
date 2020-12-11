using System;
using System.Collections.Generic;
using System.Text;

namespace Constructor3D
{
    class Camera: BaseObject
    {
        public Vector3 direction;
        public double[,] rotation;
        public Camera(Vector3 pos, Vector3 dir)
        {
            position = pos;
            direction = dir;
        }

        public void calc_rotation()
        {
            double[,] x, y, z;
            x = new double[4, 4] { { 1, 0, 0, 0 },
                                   { 0, Math.Cos(direction.x * Math.PI / 180), -Math.Sin(direction.x * Math.PI / 180), 0 },
                                   { 0, Math.Sin(direction.x * Math.PI / 180), Math.Cos(direction.x * Math.PI / 180), 0 },
                                   { 0, 0, 0, 1 } };
            y = new double[4, 4] { { Math.Cos(direction.y * Math.PI / 180), 0, -Math.Sin(direction.y * Math.PI / 180), 0 },
                                   { 0, 1, 0, 0 },
                                   { Math.Sin(direction.y * Math.PI / 180), 0, Math.Cos(direction.y * Math.PI / 180), 0 },
                                   { 0, 0, 0, 1 } };
            z = new double[4, 4] { { Math.Cos(direction.z * Math.PI / 180), -Math.Sin(direction.z * Math.PI / 180), 0, 0 },
                                   { Math.Sin(direction.z * Math.PI / 180), Math.Cos(direction.z * Math.PI / 180), 0, 0 },
                                   { 0, 0, 1, 0 },
                                   { 0, 0, 0, 1 } };
            rotation = multMatrix(x, y);
            rotation = multMatrix(rotation, z);
        }

        private double[,] multMatrix(double[,] A, double[,] B)
        {
            double[,] result = new double[4, 4] { { 0, 0, 0, 0 }, { 0, 0, 0, 0 }, { 0, 0, 0, 0 }, { 0, 0, 0, 0 } };
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    for (int k = 0; k < 4; k++)
                        result[i, j] += A[i, k] * B[k, j];
                }

            }
            return result;
        }
    }
}
