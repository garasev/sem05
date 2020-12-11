using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Constructor3D
{
    class AddObject: Command
    {
        private int type_obj;

        public AddObject(int type_obj)
        {
            this.type_obj = type_obj;
        }
        override public void execute(Controller controller)
        {
            controller.add_obj(this.type_obj);
        }
    }
}
