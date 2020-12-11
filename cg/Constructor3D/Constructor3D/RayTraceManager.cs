using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Constructor3D
{
    class RayTraceManager
    {
        public RayTracer ray_tracer;
        public RayTracerMod ray_tracer_mod;

        public RayTraceManager(Scene scene)
        {
            ray_tracer = new RayTracer(scene);
            ray_tracer_mod = new RayTracerMod(scene);
        }
    }
}
