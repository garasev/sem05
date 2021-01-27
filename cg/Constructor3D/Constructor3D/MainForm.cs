using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Constructor3D
{
    public partial class MainForm : Form
    {
        
        private FacadeViewer facade_viewer;
        private int selected_add = 0;
        private int[] obj_count = new int[5] { 0, 0, 0, 0, 0};
        private int[] last_obj = new int[5] { 0, 0, 0, 0, 0 };

        private string[] cam_tab = new string[6] { "x", "y", "z", "OX", "OY", "OZ"};
        private string[] sphere_tab = new string[9] {"x", "y", "z", "радиус", "гладкость", "отполированность (0-1)", "цвет R", "цвет G", "цвет B" };
        private string[] par_tab = new string[11] { "x", "y", "z", "длина", "ширина", "высота", "гладкость", "отполированность (0-1)", "цвет R", "цвет G", "цвет B" };
        private string[] cyl_tab = new string[10] { "x", "y", "z", "радиус", "высота", "гладкость", "отполированность (0-1)", "цвет R", "цвет G", "цвет B" };
        private string[] pyr_tab = new string[10] { "x", "y", "z", "высота", "ширина", "гладкость", "отполированность (0-1)", "цвет R", "цвет G", "цвет B" };
        private string[] light_tab = new string[4] { "x", "y", "z", "интенсивность"};

        public MainForm()
        {
            InitializeComponent();
            facade_viewer = new FacadeViewer(pictureBox2.Size);
            pictureBox2.Image = facade_viewer.controller.trace_manager.ray_tracer.bmp;

            combobox_obj.Items.Add("Камера");

            del_btn.Visible = false;

            dgv.Visible = false;
            dgv.RowHeadersVisible = false;

            openFileDialog1.Filter = "Text files(*.scene)|*.scene";
            saveFileDialog1.Filter = "Text files(*.scene)|*.scene";
        }

        private void update_image()
        {
            facade_viewer.controller.trace_manager.ray_tracer.render();
            pictureBox2.Image = facade_viewer.controller.trace_manager.ray_tracer.bmp;
        }

        private void combobox_obj_SelectedIndexChanged(object sender, EventArgs e)
        {
            dgv.Columns.Clear();
            dgv.Rows.Clear();

            var column1 = new DataGridViewColumn();
            column1.HeaderText = "Атрибут";
            column1.Width = 180;
            column1.ReadOnly = true;
            column1.Name = "attr";
            column1.CellTemplate = new DataGridViewTextBoxCell();

            var column2 = new DataGridViewColumn();
            column2.HeaderText = "Значение";
            column2.Width = 133;
            column2.Name = "value";
            column2.CellTemplate = new DataGridViewTextBoxCell();

            dgv.Columns.Add(column1);
            dgv.Columns.Add(column2);
            dgv.AllowUserToAddRows = false;

            dgv.AllowUserToResizeColumns = false;
            dgv.AllowUserToResizeRows = false;

            int tmp = combobox_obj.SelectedIndex;

            if (tmp == 0)
            {
                Camera cam = facade_viewer.controller.scene.camera;
                for (int i = 0; i < cam_tab.Length; i++)
                {
                    dgv.Rows.Add();
                    dgv["attr", dgv.Rows.Count - 1].Value = cam_tab[i];
                }

                dgv["value", 0].Value = cam.position.x;
                dgv["value", 1].Value = cam.position.y;
                dgv["value", 2].Value = cam.position.z;
                dgv["value", 3].Value = cam.direction.x;
                dgv["value", 4].Value = cam.direction.y;
                dgv["value", 5].Value = cam.direction.z;

                del_btn.Visible = false;
            }
            else if (tmp > 0 && tmp <= obj_count[4])
            {
                LightSource prim = facade_viewer.controller.scene.light_sources[tmp - 1];
                for (int i = 0; i < light_tab.Length; i++)
                {
                    dgv.Rows.Add();
                    dgv["attr", dgv.Rows.Count - 1].Value = light_tab[i];
                }
                dgv["value", 0].Value = prim.position.x;
                dgv["value", 1].Value = prim.position.y;
                dgv["value", 2].Value = prim.position.z;
                dgv["value", 3].Value = prim.intensity;

                del_btn.Visible = true;
            }
            else
            {
                Primitive prim = facade_viewer.controller.scene.primitives[tmp - obj_count[4] - 1];
                if (prim is Sphere)
                {
                    Sphere tmp_prim = (Sphere)prim;
                    for (int i = 0; i < sphere_tab.Length; i++)
                    {
                        dgv.Rows.Add();
                        dgv["attr", dgv.Rows.Count - 1].Value = sphere_tab[i];
                    }
                    dgv["value", 0].Value = tmp_prim.position.x;
                    dgv["value", 1].Value = tmp_prim.position.y;
                    dgv["value", 2].Value = tmp_prim.position.z;
                    dgv["value", 3].Value = tmp_prim.radius;
                    dgv["value", 4].Value = tmp_prim.specular;
                    dgv["value", 5].Value = tmp_prim.reflective;
                    dgv["value", 6].Value = tmp_prim.color.x;
                    dgv["value", 7].Value = tmp_prim.color.y;
                    dgv["value", 8].Value = tmp_prim.color.z;
                }
                else if (prim is Parallelepiped)
                {
                    Parallelepiped tmp_prim = (Parallelepiped)prim;
                    for (int i = 0; i < par_tab.Length; i++)
                    {
                        dgv.Rows.Add();
                        dgv["attr", dgv.Rows.Count - 1].Value = par_tab[i];
                    }
                    dgv["value", 0].Value = tmp_prim.position.x;
                    dgv["value", 1].Value = tmp_prim.position.y;
                    dgv["value", 2].Value = tmp_prim.position.z;
                    dgv["value", 3].Value = tmp_prim.width;
                    dgv["value", 4].Value = tmp_prim.height;
                    dgv["value", 5].Value = tmp_prim.length;
                    dgv["value", 6].Value = tmp_prim.specular;
                    dgv["value", 7].Value = tmp_prim.reflective;
                    dgv["value", 8].Value = tmp_prim.color.x;
                    dgv["value", 9].Value = tmp_prim.color.y;
                    dgv["value", 10].Value = tmp_prim.color.z;
                }
                else if (prim is Cylinder)
                {
                    Cylinder tmp_prim = (Cylinder)prim;
                    for (int i = 0; i < cyl_tab.Length; i++)
                    {
                        dgv.Rows.Add();
                        dgv["attr", dgv.Rows.Count - 1].Value = cyl_tab[i];
                    }
                    dgv["value", 0].Value = tmp_prim.position.x;
                    dgv["value", 1].Value = tmp_prim.position.y;
                    dgv["value", 2].Value = tmp_prim.position.z;
                    dgv["value", 3].Value = tmp_prim.radius;
                    dgv["value", 4].Value = tmp_prim.length;
                    dgv["value", 5].Value = tmp_prim.specular;
                    dgv["value", 6].Value = tmp_prim.reflective;
                    dgv["value", 7].Value = tmp_prim.color.x;
                    dgv["value", 8].Value = tmp_prim.color.y;
                    dgv["value", 9].Value = tmp_prim.color.z;
                }
                else if (prim is Pyramid)
                {
                    Pyramid tmp_prim = (Pyramid)prim;
                    for (int i = 0; i < pyr_tab.Length; i++)
                    {
                        dgv.Rows.Add();
                        dgv["attr", dgv.Rows.Count - 1].Value = pyr_tab[i];
                    }
                    dgv["value", 0].Value = tmp_prim.position.x;
                    dgv["value", 1].Value = tmp_prim.position.y;
                    dgv["value", 2].Value = tmp_prim.position.z;
                    dgv["value", 3].Value = tmp_prim.height;
                    dgv["value", 4].Value = tmp_prim.width;
                    dgv["value", 5].Value = tmp_prim.specular;
                    dgv["value", 6].Value = tmp_prim.reflective;
                    dgv["value", 7].Value = tmp_prim.color.x;
                    dgv["value", 8].Value = tmp_prim.color.y;
                    dgv["value", 9].Value = tmp_prim.color.z;
                }

                del_btn.Visible = true;
            }
            dgv.Height = 36 + (dgv.Rows.Count) * 22;
            dgv.Visible = true;
        }

        private void button_add_Click(object sender, EventArgs e)
        {
            obj_count[selected_add] += 1;
            last_obj[selected_add] += 1;

            Command add_object = new AddObject(this.selected_add);
            facade_viewer.executeCommand(add_object);
            update_image();

            string name = primitive_to_str(selected_add);
            int tmp = last_obj[selected_add];
            name = string.Concat(name, tmp.ToString());
            if (selected_add == 4)
            {
                combobox_obj.Items.Insert(obj_count[4], name);
            }
            else
                combobox_obj.Items.Add(name);
        }

        private void combobox_add_SelectedIndexChanged(object sender, EventArgs e)
        {
            string tmp = combobox_add.SelectedItem.ToString();
            if (tmp == "Сфера")
            {
                this.selected_add = 0;
            }
            else if (tmp == "Параллелепипед") 
            {
                this.selected_add = 1;
            }
            else if (tmp == "Цилиндр")
            {
                this.selected_add = 2;
            }
            else if (tmp == "Пирамида")
            {
                this.selected_add = 3;
            }
            else if (tmp == "Источник света")
            {
                this.selected_add = 4;
            }
        }

        private void button_mod_raytrace_Click(object sender, EventArgs e)
        {
            upd();
            facade_viewer.controller.trace_manager.ray_tracer_mod.render();
            pictureBox2.Image = facade_viewer.controller.trace_manager.ray_tracer_mod.bmp;
        }

        private void upd()
        {
            if (dgv.Visible)
            {

                int tmp = combobox_obj.SelectedIndex;

                if (tmp == 0)
                {
                    try 
                    {
                        double x, y, z;

                        x = Convert.ToDouble(dgv.Rows[0].Cells[1].Value);
                        y = Convert.ToDouble(dgv.Rows[1].Cells[1].Value);
                        z = Convert.ToDouble(dgv.Rows[2].Cells[1].Value);

                        Vector3 pos = new Vector3(x, y, z);

                        x = Convert.ToDouble(dgv.Rows[3].Cells[1].Value);
                        y = Convert.ToDouble(dgv.Rows[4].Cells[1].Value);
                        z = Convert.ToDouble(dgv.Rows[5].Cells[1].Value);

                        Vector3 dir = new Vector3(x, y, z);

                        facade_viewer.controller.scene.camera = new Camera(pos, dir);
                    }
                    catch
                    {
                        MessageBox.Show("Ошибка при изменении атрибутов камеры");
                    }
                }
                else if (tmp > 0 && tmp <= obj_count[4])
                {
                    LightSource prim = facade_viewer.controller.scene.light_sources[tmp - 1];
                    try
                    {
                        double x, y, z;
                        double intensity;

                        x = Convert.ToDouble(dgv.Rows[0].Cells[1].Value);
                        y = Convert.ToDouble(dgv.Rows[1].Cells[1].Value);
                        z = Convert.ToDouble(dgv.Rows[2].Cells[1].Value);

                        intensity = Convert.ToDouble(dgv.Rows[3].Cells[1].Value);

                        intensity = (intensity < 0) ? 0 : intensity;
                        intensity = (intensity > 1) ? 1 : intensity;


                        Vector3 pos = new Vector3(x, y, z);

                        LightSource tmp_light = new LightSource(pos, intensity);
                        facade_viewer.controller.scene.light_sources[tmp - 1] = tmp_light;
                    }
                    catch
                    {
                        MessageBox.Show("Ошибка при изменении атрибутов объекта");
                    }
                }
                else
                {
                    try
                    {
                        Primitive prim = facade_viewer.controller.scene.primitives[tmp - obj_count[4] - 1];
                        if (prim is Sphere)
                        {
                            try
                            {
                                double x, y, z;
                                double r, g, b;
                                double radius, specular, reflective;

                                x = Convert.ToDouble(dgv.Rows[0].Cells[1].Value);
                                y = Convert.ToDouble(dgv.Rows[1].Cells[1].Value);
                                z = Convert.ToDouble(dgv.Rows[2].Cells[1].Value);

                                r = Convert.ToInt16(dgv.Rows[6].Cells[1].Value);
                                g = Convert.ToInt16(dgv.Rows[7].Cells[1].Value);
                                b = Convert.ToInt16(dgv.Rows[8].Cells[1].Value);

                                r = (r < 0) ? 0 : r;
                                r = (r > 255) ? 255 : r;

                                g = (g < 0) ? 0 : g;
                                g = (g > 255) ? 255 : g;

                                b = (b < 0) ? 0 : b;
                                b = (b > 255) ? 255 : b;

                                radius = Convert.ToDouble(dgv.Rows[3].Cells[1].Value);
                                specular = Convert.ToDouble(dgv.Rows[4].Cells[1].Value);
                                reflective = Convert.ToDouble(dgv.Rows[5].Cells[1].Value);

                                specular = (specular < 0) ? 0 : specular;
                                specular = (specular > 1000) ? 1000 : specular;

                                reflective = (reflective < 0) ? 0 : reflective;
                                reflective = (reflective > 1) ? 1 : reflective;

                                Vector3 pos = new Vector3(x, y, z);

                                Vector3 color = new Vector3(r, g, b);

                                Sphere tmp_sphere = new Sphere(pos, radius, color, specular, reflective);
                                facade_viewer.controller.scene.primitives[tmp - obj_count[4] - 1] = tmp_sphere;
                            }
                            catch
                            {
                                MessageBox.Show("Ошибка при изменении атрибутов объекта");
                            }
                        }
                        else if (prim is Parallelepiped)
                        {
                            try
                            {
                                double x, y, z;
                                double r, g, b;
                                double width, height, length;
                                double specular, reflective;

                                x = Convert.ToDouble(dgv.Rows[0].Cells[1].Value);
                                y = Convert.ToDouble(dgv.Rows[1].Cells[1].Value);
                                z = Convert.ToDouble(dgv.Rows[2].Cells[1].Value);

                                r = Convert.ToInt16(dgv.Rows[8].Cells[1].Value);
                                g = Convert.ToInt16(dgv.Rows[9].Cells[1].Value);
                                b = Convert.ToInt16(dgv.Rows[10].Cells[1].Value);

                                r = (r < 0) ? 0 : r;
                                r = (r > 255) ? 255 : r;

                                g = (g < 0) ? 0 : g;
                                g = (g > 255) ? 255 : g;

                                b = (b < 0) ? 0 : b;
                                b = (b > 255) ? 255 : b;

                                width = Convert.ToDouble(dgv.Rows[3].Cells[1].Value);
                                height = Convert.ToDouble(dgv.Rows[4].Cells[1].Value);
                                length = Convert.ToDouble(dgv.Rows[5].Cells[1].Value);

                                specular = Convert.ToDouble(dgv.Rows[6].Cells[1].Value);
                                reflective = Convert.ToDouble(dgv.Rows[7].Cells[1].Value);

                                specular = (specular < 0) ? 0 : specular;
                                specular = (specular > 1000) ? 1000 : specular;

                                reflective = (reflective < 0) ? 0 : reflective;
                                reflective = (reflective > 1) ? 1 : reflective;

                                Vector3 pos = new Vector3(x, y, z);

                                Vector3 color = new Vector3(r, g, b);

                                Parallelepiped tmp_prim = new Parallelepiped(pos, color, height, width, length, specular, reflective);
                                facade_viewer.controller.scene.primitives[tmp - obj_count[4] - 1] = tmp_prim;
                            }
                            catch
                            {
                                MessageBox.Show("Ошибка при изменении атрибутов объекта");
                            }
                        }
                        else if (prim is Cylinder)
                        {
                            try
                            {
                                double x, y, z;
                                double r, g, b;
                                double radius, length;
                                double specular, reflective;

                                x = Convert.ToDouble(dgv.Rows[0].Cells[1].Value);
                                y = Convert.ToDouble(dgv.Rows[1].Cells[1].Value);
                                z = Convert.ToDouble(dgv.Rows[2].Cells[1].Value);

                                r = Convert.ToInt16(dgv.Rows[7].Cells[1].Value);
                                g = Convert.ToInt16(dgv.Rows[8].Cells[1].Value);
                                b = Convert.ToInt16(dgv.Rows[9].Cells[1].Value);

                                r = (r < 0) ? 0 : r;
                                r = (r > 255) ? 255 : r;

                                g = (g < 0) ? 0 : g;
                                g = (g > 255) ? 255 : g;

                                b = (b < 0) ? 0 : b;
                                b = (b > 255) ? 255 : b;

                                radius = Convert.ToDouble(dgv.Rows[3].Cells[1].Value);
                                length = Convert.ToDouble(dgv.Rows[4].Cells[1].Value);

                                specular = Convert.ToDouble(dgv.Rows[5].Cells[1].Value);
                                reflective = Convert.ToDouble(dgv.Rows[6].Cells[1].Value);

                                specular = (specular < 0) ? 0 : specular;
                                specular = (specular > 1000) ? 1000 : specular;

                                reflective = (reflective < 0) ? 0 : reflective;
                                reflective = (reflective > 1) ? 1 : reflective;

                                Vector3 pos = new Vector3(x, y, z);

                                Vector3 color = new Vector3(r, g, b);

                                Cylinder tmp_prim = new Cylinder(pos, color, radius, length, specular, reflective);
                                facade_viewer.controller.scene.primitives[tmp - obj_count[4] - 1] = tmp_prim;
                            }
                            catch
                            {
                                MessageBox.Show("Ошибка при изменении атрибутов объекта");
                            }
                        }
                        else if (prim is Pyramid)
                        {
                            try
                            {
                                double x, y, z;
                                double r, g, b;
                                double height, width;
                                double specular, reflective;

                                x = Convert.ToDouble(dgv.Rows[0].Cells[1].Value);
                                y = Convert.ToDouble(dgv.Rows[1].Cells[1].Value);
                                z = Convert.ToDouble(dgv.Rows[2].Cells[1].Value);

                                r = Convert.ToInt16(dgv.Rows[7].Cells[1].Value);
                                g = Convert.ToInt16(dgv.Rows[8].Cells[1].Value);
                                b = Convert.ToInt16(dgv.Rows[9].Cells[1].Value);

                                r = (r < 0) ? 0 : r;
                                r = (r > 255) ? 255 : r;

                                g = (g < 0) ? 0 : g;
                                g = (g > 255) ? 255 : g;

                                b = (b < 0) ? 0 : b;
                                b = (b > 255) ? 255 : b;

                                height = Convert.ToDouble(dgv.Rows[3].Cells[1].Value);
                                width = Convert.ToDouble(dgv.Rows[4].Cells[1].Value);

                                specular = Convert.ToDouble(dgv.Rows[5].Cells[1].Value);
                                reflective = Convert.ToDouble(dgv.Rows[6].Cells[1].Value);

                                specular = (specular < 0) ? 0 : specular;
                                specular = (specular > 1000) ? 1000 : specular;

                                reflective = (reflective < 0) ? 0 : reflective;
                                reflective = (reflective > 1) ? 1 : reflective;

                                Vector3 pos = new Vector3(x, y, z);

                                Vector3 color = new Vector3(r, g, b);

                                Pyramid tmp_prim = new Pyramid(pos, color, height, width, specular, reflective);
                                facade_viewer.controller.scene.primitives[tmp - obj_count[4] - 1] = tmp_prim;
                            }
                            catch
                            {
                                MessageBox.Show("Ошибка при изменении атрибутов объекта");
                            }
                        }
                    }
                    catch
                    {
                    }
                }
            }
        }
        private void button_raytrace_Click(object sender, EventArgs e)
        {
            upd();

            update_image();
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private string primitive_to_str(int select)
        {
            switch (select)
            {
                case 0:
                    return "Сфера";
                case 1:
                    return "Параллелепипед";
                case 2:
                    return "Цилиндр";
                case 3:
                    return "Пирамида";
                default:
                    return "Источник света";
            }
        }

        private void dgv_CellValueChanged(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int tmp = combobox_obj.SelectedIndex;

            if (tmp <= obj_count[4])
            {
                obj_count[4] -= 1;
                facade_viewer.controller.scene.light_sources.RemoveRange(tmp - 1, 1);
            }
            else
                facade_viewer.controller.scene.primitives.RemoveRange(tmp - obj_count[4] - 1, 1);

            combobox_obj.Items.RemoveAt(tmp);
            dgv.Visible = false;
            del_btn.Visible = false;

            update_image();
        }

        private void сохранитьСценуToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (saveFileDialog1.ShowDialog() == DialogResult.Cancel)
                return;

            string filename = saveFileDialog1.FileName;
            Scene scene = facade_viewer.controller.scene;
            facade_viewer.controller.file_manager.savingScene(filename, scene);

            MessageBox.Show("Сцена сохранилась успешно");

        }

        private void загрузитьСценуToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.Cancel)
                return;

            string filename = openFileDialog1.FileName;
            Scene scene = facade_viewer.controller.scene;
            facade_viewer.controller.file_manager.loadingScene(filename, ref scene);
            facade_viewer.controller.scene = scene;
            upd();

            update_image();

            MessageBox.Show("Сцена загрузилась успешно");
            upd_combobox();
        }

        private void upd_combobox()
        {
            combobox_obj.Items.Clear();
            combobox_obj.Items.Add("Камера");

            string name;
            int tmp;
            obj_count = new int[5] { 0, 0, 0, 0, 0 };
            last_obj = new int[5] { 0, 0, 0, 0, 0 };

            List<LightSource> l = facade_viewer.controller.scene.light_sources;
            for (int i = 0; i < l.Count; i++)
            {
                obj_count[4] += 1;
                last_obj[4] += 1;
                name = primitive_to_str(4);
                tmp = last_obj[4];
                name = string.Concat(name, tmp.ToString());
                combobox_obj.Items.Insert(obj_count[4], name);
            }

            List <Primitive> prims = facade_viewer.controller.scene.primitives;
            for (int i = 0; i < prims.Count; i++)
            {
                if (prims[i] is Sphere)
                {
                    selected_add = 0;
                }
                if (prims[i] is Parallelepiped)
                {
                    selected_add = 1;
                }
                if (prims[i] is Cylinder)
                {
                    selected_add = 2;
                }
                if (prims[i] is Pyramid)
                {
                    selected_add = 3;
                }
                obj_count[selected_add] += 1;
                last_obj[selected_add] += 1;
                name = primitive_to_str(selected_add);
                tmp = last_obj[selected_add];
                name = string.Concat(name, tmp.ToString());
                combobox_obj.Items.Add(name);
            }
            
        }

        private void openFileDialog1_FileOk(object sender, CancelEventArgs e)
        {

        }

        private void saveFileDialog1_FileOk(object sender, CancelEventArgs e)
        {

        }
    }
}
