using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace Constructor3D
{
    class Parser
    {
        [JsonProperty("camera")]
        private Camera camera;

        [JsonProperty("spheres")]
        private Sphere[] spheres;

        [JsonProperty("cylinders")]
        private Cylinder[] cylinders;

        [JsonProperty("Pyramids")]
        private Pyramid[] pyramids;

        [JsonProperty("parallelepipeds")]
        private Parallelepiped[] parallelepipeds;

        [JsonProperty("lights")]
        private LightSource[] lights;



        public void SceneObjectToJson(Scene scene)
        {
            this.camera = scene.camera;

            List<Sphere> spheres = new List<Sphere>();
            List<Cylinder> cylinders = new List<Cylinder>();
            List<Pyramid> pyramids = new List<Pyramid>();
            List<Parallelepiped> parallelepipeds = new List<Parallelepiped>();

            for (int i = 0; i < scene.primitives.Count; i++)
            {
                if (scene.primitives[i] is Sphere)
                    spheres.Add((Sphere)scene.primitives[i]);
                if (scene.primitives[i] is Cylinder)
                    cylinders.Add((Cylinder)scene.primitives[i]);
                if (scene.primitives[i] is Parallelepiped)
                    parallelepipeds.Add((Parallelepiped)scene.primitives[i]);
                if (scene.primitives[i] is Pyramid)
                    pyramids.Add((Pyramid)scene.primitives[i]);
            }

            this.spheres = spheres.ToArray();
            this.cylinders = cylinders.ToArray();
            this.pyramids = pyramids.ToArray();
            this.parallelepipeds = parallelepipeds.ToArray();

            this.lights = scene.light_sources.ToArray();

        }
        public void JsonToSceneObject(ref Scene scene)
        {
            scene.camera = this.camera;

            scene.primitives.Clear();

            for (int i = 0; i < this.spheres.Length; i++)
                scene.primitives.Add(this.spheres[i]);
            for (int i = 0; i < this.cylinders.Length; i++)
                scene.primitives.Add(this.cylinders[i]);
            for (int i = 0; i < this.pyramids.Length; i++)
                scene.primitives.Add(this.pyramids[i]);
            for (int i = 0; i < this.parallelepipeds.Length; i++)
                scene.primitives.Add(this.parallelepipeds[i]);

            scene.light_sources.Clear();

            for (int i = 0; i < this.lights.Length; i++)
                scene.light_sources.Add(this.lights[i]);

        }

    }
}
