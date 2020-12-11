using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Constructor3D
{
    class Transformer
    {
        static public void RotateOX(ref Vector3 vec, ref Vector3 C, double teta)
        {

            double d = teta * Math.PI / 180;
            double tmp_y;
            tmp_y = C.y + (vec.y - C.y) * Math.Cos(d) + (vec.z - C.z) * Math.Sin(d);
            vec.z = C.z - (vec.y - C.y) * Math.Sin(d) + (vec.z - C.z) * Math.Cos(d);
            vec.y = tmp_y;
        }
        static public void RotateOY(ref Vector3 vec, ref Vector3 C, double teta)
        {

            double d = teta * Math.PI / 180;
            double tmp_x;
            tmp_x = C.x + (vec.x - C.x) * Math.Cos(d) + (vec.z - C.z) * Math.Sin(d);
            vec.z = C.z - (vec.x - C.x) * Math.Sin(d) + (vec.z - C.z) * Math.Cos(d);
            vec.x = tmp_x;
        }

        static public void RotateOZ(ref Vector3 vec, ref Vector3 C, double teta)
        {

            double d = teta * Math.PI / 180;
            double tmp_x;
            tmp_x = C.x + (vec.x - C.x) * Math.Cos(d) + (vec.y - C.y) * Math.Sin(d);
            vec.y = C.y - (vec.x - C.x) * Math.Sin(d) + (vec.y - C.y) * Math.Cos(d);
            vec.x = tmp_x;
        }

        /*static public void RotateOXCylinder(ref Cylinder cylinder, ref Vector3 C, double teta)
        {
            RotateOX(ref cylinder.C, ref C, teta);
            RotateOX(ref cylinder.V, ref C, teta);
        }

        static public void RotateOYCylinder(ref Cylinder cylinder, ref Vector3 C, double teta)
        {
            RotateOY(ref cylinder.C, ref C, teta);
            RotateOY(ref cylinder.V, ref C, teta);
        }

        static public void RotateOZCylinder(ref Cylinder cylinder, ref Vector3 C, double teta)
        {
            RotateOZ(ref cylinder.C, ref C, teta);
            RotateOZ(ref cylinder.V, ref C, teta);
        }*/

        static public double[,] MultiplyMM4(double[,] A, double[,] B)
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

        static public void MultiplyMV(double[,] matr, ref Vector3 vec)
        {
            double[] tmp = new double[4] { vec.x, vec.y, vec.z, 1 };
            double[] result = new double[4] { 0, 0, 0, 0 };

            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    result[i] += tmp[j] * matr[i, j];
                }
            }

            vec.x = result[0];
            vec.y = result[1];
            vec.z = result[2];
        }

        static public void RotationOXVector(ref Vector3 vec, double teta)
        {
            double[,] matrix = getMatrixRotationOX(teta);
            MultiplyMV(matrix, ref vec);
        }

        static public void RotationOYVector(ref Vector3 vec, double teta)
        {
            double[,] matrix = getMatrixRotationOY(teta);
            MultiplyMV(matrix, ref vec);
        }

        static public void RotationOZVector(ref Vector3 vec, double teta)
        {
            double[,] matrix = getMatrixRotationOZ(teta);
            MultiplyMV(matrix, ref vec);
        }

        static public void RotationOXMatrix(ref double[,] R, double teta)
        {
            double[,] A = getMatrixRotationOX(teta);
            R = MultiplyMM4(R, A);
        }

        static public void RotationOYMatrix(ref double[,] R, double teta)
        {
            double[,] A = getMatrixRotationOY(teta);
            R = MultiplyMM4(R, A);
        }

        static public void RotationOZMatrix(ref double[,] R, double teta)
        {
            double[,] A = getMatrixRotationOZ(teta);
            R = MultiplyMM4(R, A);
        }

        static public double[,] getMatrixRotationOX(double teta)
        {
            double d = teta * Math.PI / 180;
            double[,] matrix = new double[4, 4] { { 1, 0, 0, 0 }, { 0, Math.Cos(d), -Math.Sin(d), 0 }, { 0, Math.Sin(d), Math.Cos(d), 0 }, { 0, 0, 0, 1 } };
            return matrix;
        }

        static public double[,] getMatrixRotationOY(double teta)
        {
            double d = teta * Math.PI / 180;
            double[,] matrix = new double[4, 4] { { Math.Cos(d), 0, Math.Sin(d), 0 }, { 0, 1, 0, 0 }, { -Math.Sin(d), 0, Math.Cos(d), 0 }, { 0, 0, 0, 1 } };
            return matrix;
        }

        static public double[,] getMatrixRotationOZ(double teta)
        {
            double d = teta * Math.PI / 180;
            double[,] matrix = new double[4, 4] { { Math.Cos(d), -Math.Sin(d), 0, 0 }, { Math.Sin(d), Math.Cos(d), 0, 0 }, { 0, 0, 1, 0 }, { 0, 0, 0, 1 } };
            return matrix;
        }

        static public void MoveVector(ref Vector3 vec, double dx, double dy, double dz)
        {
            vec.x += dx;
            vec.y += dy;
            vec.z += dz;
        }

        static public double[,] getMatrixMove(double dx, double dy, double dz)
        {
            double[,] matrix = new double[4, 4] { { 1, 0, 0, 0 }, { 0, 1, 0, 0 }, { 0, 0, 1, 0 }, { dx, dy, dz, 1 } };
            return matrix;
        }

        static public void MoveMatrix(ref double[,] R, double dx, double dy, double dz)
        {
            double[,] A = getMatrixMove(dx, dy, dz);
            R = MultiplyMM4(R, A);
        }
    }
}
