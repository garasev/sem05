using System;
using System.Collections.Generic;
using System.Text;

namespace Constructor3D
{
    class LightSource: BaseObject
    {
        public double intensity;

        public LightSource(Vector3 position, double intensity)
        {
            this.position = position;
            this.intensity = intensity;
        }
    }
}
