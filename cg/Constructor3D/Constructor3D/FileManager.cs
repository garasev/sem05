using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace Constructor3D
{
    class FileManager
    {


        public FileManager()
        {
            
        }

        public void savingScene(string filename, Scene scene)
        {
            Parser parser = new Parser();
            parser.SceneObjectToJson(scene);
            string output = JsonConvert.SerializeObject(parser);
            System.IO.File.WriteAllText(filename, output);
        }

        public void loadingScene(string filename, ref Scene scene)
        {
            string input = System.IO.File.ReadAllText(filename);
            Parser parser = JsonConvert.DeserializeObject<Parser>(input);
            parser.JsonToSceneObject(ref scene);
        }
    }
}
