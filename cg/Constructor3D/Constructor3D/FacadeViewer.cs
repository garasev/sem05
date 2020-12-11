using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace Constructor3D
{
    class FacadeViewer
    {
        public Controller controller;
        public FacadeViewer(Size size)
        {
            this.controller = new Controller(size);
        }

        public void executeCommand(Command command)
        {
            command.execute(controller);
        }
    }
}
