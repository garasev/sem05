using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace Constructor3D
{
    class Controller
    {
        public FileManager file_manager;
        public Scene scene;
        public RayTraceManager trace_manager;

        public Controller(Size size)
        {
            scene = new Scene(size);
            file_manager = new FileManager();
            trace_manager = new RayTraceManager(scene);
        }
        public void add_obj(int obj_type)
        {
            if (obj_type == 0)
            {
                scene.add_sphere(new Vector3(0, 0, 0), 1, new Vector3(255, 0, 0), 10, 0.2);
            }
            else if (obj_type == 1)
            {
                scene.add_par(new Vector3(0, 0, 0), new Vector3(0, 255, 0), 1, 1, 1, 10, 0.2);
            }
            else if (obj_type == 2)
            {
                scene.add_cyl(new Vector3(0, 0, 0), new Vector3(0, 0, 255), 1, 1, 10, 0.2);
            }
            else if (obj_type == 3)
            {
                scene.add_pyr(new Vector3(0, 0, 0), new Vector3(0, 0, 255), 1, 1, 10, 0.2);
            }
            else if (obj_type == 4)
            {
                scene.add_ls(new Vector3(5, 5, 5), 0.5);
            }
        }
        public void del_obj()
        {

        }
    }
}
