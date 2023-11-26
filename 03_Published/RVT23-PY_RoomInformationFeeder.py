# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
clr.AddReference('RevitAPI')
from Autodesk.DesignScript.Geometry import *
from Autodesk.Revit.DB import *

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager

clr.AddReference("RevitAPIUI")
from Autodesk.Revit.UI import PreviewControl

# imports requiered for UI
import System.Drawing
import System.Windows.Forms
from System.Drawing import *
from System.Windows.Forms import *

#TODO Creamos clsae con una interfaz personalizada
class Alimentador_Parametros(Form):
    def __init__(self, parameter_names, doc, view):
        self.parameter_names = parameter_names
        self.doc = doc
        self.view = view
        self.preview = PreviewControl(self.doc, self.view.Id)
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._roomsDropDown = System.Windows.Forms.ComboBox()
        self._roomLabel = System.Windows.Forms.Label()
        self._roomName = System.Windows.Forms.Label()
        self._roomNumber = System.Windows.Forms.Label()
        self._roomParam1 = System.Windows.Forms.Label()
        self._roomParam2 = System.Windows.Forms.Label()
        self._roomParam3 = System.Windows.Forms.Label()
        self._roomParam6 = System.Windows.Forms.Label()
        self._roomParam5 = System.Windows.Forms.Label()
        self._roomParam4 = System.Windows.Forms.Label()
        self._roomNameTextBox = System.Windows.Forms.TextBox()
        self._roomNumberTextBox = System.Windows.Forms.TextBox()
        self._roomParam1TextBox = System.Windows.Forms.TextBox()
        self._roomParam2TextBox = System.Windows.Forms.TextBox()
        self._roomParam3TextBox = System.Windows.Forms.TextBox()
        self._roomParam4TextBox = System.Windows.Forms.TextBox()
        self._roomParam5TextBox = System.Windows.Forms.TextBox()
        self._roomParam6TextBox = System.Windows.Forms.TextBox()
        self._updateBtn = System.Windows.Forms.Button()
        self._panel1 = System.Windows.Forms.Panel()
        self.SuspendLayout()
        # 
        # roomsDropDown
        # 
        self._roomsDropDown.FormattingEnabled = True
        self._roomsDropDown.Location = System.Drawing.Point(28, 54)
        self._roomsDropDown.Name = "roomsDropDown"
        self._roomsDropDown.Size = System.Drawing.Size(400, 30)
        self._roomsDropDown.TabIndex = 0
        self._roomsDropDown.SelectedIndexChanged += self.RoomsDropDownSelectedIndexChanged
        # 
        # roomLabel
        # 
        self._roomLabel.Location = System.Drawing.Point(28, 19)
        self._roomLabel.Name = "roomLabel"
        self._roomLabel.Size = System.Drawing.Size(259, 34)
        self._roomLabel.TabIndex = 1
        self._roomLabel.Text = "Habitaciones"                             #!Nombre en la ventana
        # 
        # roomName
        # 
        self._roomName.Location = System.Drawing.Point(28, 113)
        self._roomName.Name = "roomName"
        self._roomName.Size = System.Drawing.Size(139, 33)
        self._roomName.TabIndex = 2
        self._roomName.Text = "Nombre de habitación"                      #!Nombre en la ventana
        # 
        # roomNumber
        # 
        self._roomNumber.Location = System.Drawing.Point(28, 158)
        self._roomNumber.Name = "roomNumber"
        self._roomNumber.Size = System.Drawing.Size(139, 33)
        self._roomNumber.TabIndex = 3
        self._roomNumber.Text = "Número de habitación"                    #!Nombre en la ventana
        # 
        # roomParam1
        # 
        self._roomParam1.Location = System.Drawing.Point(28, 203)
        self._roomParam1.Name = "roomParam1"
        self._roomParam1.Size = System.Drawing.Size(139, 33)
        self._roomParam1.TabIndex = 4
        self._roomParam1.Text = "roomParam1"
        # 
        # roomParam2
        # 
        self._roomParam2.Location = System.Drawing.Point(28, 248)
        self._roomParam2.Name = "roomParam2"
        self._roomParam2.Size = System.Drawing.Size(139, 33)
        self._roomParam2.TabIndex = 5
        self._roomParam2.Text = "roomParam2"
        # 
        # roomParam3
        # 
        self._roomParam3.Location = System.Drawing.Point(28, 293)
        self._roomParam3.Name = "roomParam3"
        self._roomParam3.Size = System.Drawing.Size(139, 33)
        self._roomParam3.TabIndex = 6
        self._roomParam3.Text = "roomParam3"
        # 
        # roomParam6
        # 
        self._roomParam6.Location = System.Drawing.Point(28, 428)
        self._roomParam6.Name = "roomParam6"
        self._roomParam6.Size = System.Drawing.Size(139, 33)
        self._roomParam6.TabIndex = 9
        self._roomParam6.Text = "roomParam6"
        # 
        # roomParam5
        # 
        self._roomParam5.Location = System.Drawing.Point(28, 383)
        self._roomParam5.Name = "roomParam5"
        self._roomParam5.Size = System.Drawing.Size(139, 33)
        self._roomParam5.TabIndex = 8
        self._roomParam5.Text = "roomParam5"
        # 
        # roomParam4
        # 
        self._roomParam4.Location = System.Drawing.Point(28, 338)
        self._roomParam4.Name = "roomParam4"
        self._roomParam4.Size = System.Drawing.Size(139, 33)
        self._roomParam4.TabIndex = 7
        self._roomParam4.Text = "roomParam4"
        # 
        # roomNameTextBox
        # 
        self._roomNameTextBox.Location = System.Drawing.Point(198, 110)
        self._roomNameTextBox.Name = "roomNameTextBox"
        self._roomNameTextBox.ReadOnly = True
        self._roomNameTextBox.Size = System.Drawing.Size(230, 29)
        self._roomNameTextBox.TabIndex = 10
        # 
        # roomNumberTextBox
        # 
        self._roomNumberTextBox.Location = System.Drawing.Point(198, 155)
        self._roomNumberTextBox.Name = "roomNumberTextBox"
        self._roomNumberTextBox.ReadOnly = True
        self._roomNumberTextBox.Size = System.Drawing.Size(230, 29)
        self._roomNumberTextBox.TabIndex = 11
        # 
        # roomParam1TextBox
        # 
        self._roomParam1TextBox.Location = System.Drawing.Point(198, 200)
        self._roomParam1TextBox.Name = "roomParam1TextBox"
        self._roomParam1TextBox.ReadOnly = True
        self._roomParam1TextBox.Size = System.Drawing.Size(230, 29)
        self._roomParam1TextBox.TabIndex = 12
        # 
        # roomParam2TextBox
        # 
        self._roomParam2TextBox.Location = System.Drawing.Point(198, 245)
        self._roomParam2TextBox.Name = "roomParam2TextBox"
        self._roomParam2TextBox.Size = System.Drawing.Size(230, 29)
        self._roomParam2TextBox.TabIndex = 13
        # 
        # roomParam3TextBox
        # 
        self._roomParam3TextBox.Location = System.Drawing.Point(198, 290)
        self._roomParam3TextBox.Name = "roomParam3TextBox"
        self._roomParam3TextBox.Size = System.Drawing.Size(230, 29)
        self._roomParam3TextBox.TabIndex = 14
        # 
        # roomParam4TextBox
        # 
        self._roomParam4TextBox.Location = System.Drawing.Point(198, 335)
        self._roomParam4TextBox.Name = "roomParam4TextBox"
        self._roomParam4TextBox.Size = System.Drawing.Size(230, 29)
        self._roomParam4TextBox.TabIndex = 15
        # 
        # roomParam5TextBox
        # 
        self._roomParam5TextBox.Location = System.Drawing.Point(198, 380)
        self._roomParam5TextBox.Name = "roomParam5TextBox"
        self._roomParam5TextBox.Size = System.Drawing.Size(230, 29)
        self._roomParam5TextBox.TabIndex = 16
        # 
        # roomParam7TextBox
        # 
        self._roomParam6TextBox.Location = System.Drawing.Point(198, 425)
        self._roomParam6TextBox.Name = "roomParam7TextBox"
        self._roomParam6TextBox.Size = System.Drawing.Size(230, 29)
        self._roomParam6TextBox.TabIndex = 17
        # 
        # updateBtn
        # 
        self._updateBtn.Cursor = System.Windows.Forms.Cursors.Hand
        self._updateBtn.Location = System.Drawing.Point(28, 480)
        self._updateBtn.Name = "updateBtn"
        self._updateBtn.Size = System.Drawing.Size(399, 33)
        self._updateBtn.TabIndex = 18
        self._updateBtn.Text = "Actualizar parámetros"                 #!Nombre del botón en la ventana
        self._updateBtn.UseVisualStyleBackColor = True
        self._updateBtn.Click += self.UpdateParameters
        #
        # preview host
        # 
        self.PreviewHost = System.Windows.Forms.Integration.ElementHost()
        self.PreviewHost.Location = System.Drawing.Point(470, 54)
        self.PreviewHost.Dock = DockStyle.Fill
        self.PreviewHost.Size = System.Drawing.Size(50, 50)
        self.PreviewHost.Child = self.preview                               # bind windows form element with revit PreviewHost
        # 
        # panel1
        # 
        self._panel1.Location = System.Drawing.Point(470, 54)
        self._panel1.Name = "panel1"
        self._panel1.Size = System.Drawing.Size(490, 459)
        self._panel1.TabIndex = 19
        self._panel1.Controls.Add(self.PreviewHost)             # add Revit PreviewHost to Form Panel
        # 
        # MyFirstForm
        # 
        self.BackColor = System.Drawing.SystemColors.InactiveBorder
        self.ClientSize = System.Drawing.Size(1000, 544)
        self.Controls.Add(self._updateBtn)
        self.Controls.Add(self._roomParam6TextBox)
        self.Controls.Add(self._roomParam5TextBox)
        self.Controls.Add(self._roomParam4TextBox)
        self.Controls.Add(self._roomParam3TextBox)
        self.Controls.Add(self._roomParam2TextBox)
        self.Controls.Add(self._roomParam1TextBox)
        self.Controls.Add(self._roomNumberTextBox)
        self.Controls.Add(self._roomNameTextBox)
        self.Controls.Add(self._roomParam6)
        self.Controls.Add(self._roomParam5)
        self.Controls.Add(self._roomParam4)
        self.Controls.Add(self._roomParam3)
        self.Controls.Add(self._roomParam2)
        self.Controls.Add(self._roomParam1)
        self.Controls.Add(self._roomNumber)
        self.Controls.Add(self._roomName)
        self.Controls.Add(self._roomLabel)
        self.Controls.Add(self._roomsDropDown)
        self.Controls.Add(self._panel1)
        self.Font = System.Drawing.Font("Roboto Light", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)   #* Añadir fuente personalizada
        self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle
        self.Name = "MyFirstForm"
        self.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
        self.Text = "Alimentador de información"                  #!Nombre en la ventana
        self._panel1.ResumeLayout(False)
        self.ResumeLayout(False)
        self.PerformLayout()
        # bind parameters
        self._bindRoomParameters(self.parameter_names)

    #TODO Función para Actualizar valores
    def UpdateParameters(self, sender, e):
        
        #* Obtener los valores de los parametros indicados como inputs
        param2 = self._roomParam4TextBox.Text
        param3 = self._roomParam4TextBox.Text
        param4 = self._roomParam4TextBox.Text
        param5 = self._roomParam5TextBox.Text
        param6 = self._roomParam6TextBox.Text
        
        #* Obtener el id de las habitacion seleccionada
        selected_room = self._roomsDropDown.SelectedItem
        room_id = selected_room.split("[")[1].split("]")[0]
        
        #* Obtener la habitación del modelo
        room = doc.GetElement(ElementId(room_id))
        
        #* Aplicar valores a los parámetros
        t = Transaction(self.doc)
        t.Start('Actualizar valores')
        room.LookupParameter(self._roomParam2.Text).Set(param2)
        room.LookupParameter(self._roomParam3.Text).Set(param3)
        room.LookupParameter(self._roomParam4.Text).Set(param4)
        room.LookupParameter(self._roomParam5.Text).Set(param5)
        room.LookupParameter(self._roomParam6.Text).Set(param6)
        t_status = t.Commit()


    #TODO Función para crear lista de habitaciones    
    def bindRoomsList(self, rooms):
        room_names = [room.LookupParameter("Nombre").AsString() for room in rooms]
        rooms_keys = [f"{room.Number} - {room_names[i]} [{room.Id}]" for i, room in enumerate(rooms)]
        self._roomsDropDown.DataSource = rooms_keys     # pass room list to DropDown Component
        
        
    #TODO función para crear lista de parámetros    
    def _bindRoomParameters(self, parameter_names):
        self._roomParam1.Text = parameter_names[0]      #! Parametro Nivel
        self._roomParam2.Text = parameter_names[1]      #! Parametro 2
        self._roomParam3.Text = parameter_names[2]      #! Parametro 3
        self._roomParam4.Text = parameter_names[3]      #! Parámetro 4
        self._roomParam5.Text = parameter_names[4]      #! Parámetro 5
        self._roomParam6.Text = parameter_names[5]      #! Parámetro 6
        
        
    #TODO Función para mostrar la jhabitación seleccionada y todos sus parametros indicados    
    def RoomsDropDownSelectedIndexChanged(self, sender, e):
        #* Obtener id de habitacion seleccionada
        selected_room = self._roomsDropDown.SelectedItem
        room_id = selected_room.split("[")[1].split("]")[0]
        
        #* obtener habitación del modelo
        room = doc.GetElement(ElementId(room_id))
        room_name = room.LookupParameter("Nombre").AsString()
        
        #* Obtener valores actuales de los parámetros de las hbaitaciones
        self._roomNameTextBox.Text = room_name
        self._roomNumberTextBox.Text = room.Number
        self._roomParam1TextBox.Text = room.Level.Name
        self._roomParam2TextBox.Text = room.LookupParameter(self._roomParam2.Text).AsString()
        self._roomParam3TextBox.Text = room.LookupParameter(self._roomParam3.Text).AsString()
        self._roomParam4TextBox.Text = room.LookupParameter(self._roomParam4.Text).AsString()
        self._roomParam5TextBox.Text = room.LookupParameter(self._roomParam5.Text).AsString()
        self._roomParam6TextBox.Text = room.LookupParameter(self._roomParam6.Text).AsString()
        
        #* Establecer caja de sección adaptandose al contorno de la habitación seleccionada extendiendo la base para que se vea el suelo
        room_b_box = room.get_BoundingBox(self.doc.ActiveView)
        extended_b_box = BoundingBoxXYZ()
        extended_b_box.Max = room_b_box.Max 
        extended_b_box.Min = XYZ(room_b_box.Min.X, room_b_box.Min.Y, room_b_box.Min.Z-1)
        
        #* comenzar transacción
        t = Transaction(doc)
        t.Start("Show Room")
        view.SetSectionBox(extended_b_box)
        t.Commit()


#TODO Funcion para obtener vista por el nombre indicado por el usuario
def getView_ByName(view_name):
    value_provider = ParameterValueProvider(ElementId(BuiltInParameter.VIEW_NAME))
    evaluator = FilterStringEquals()
    rule = FilterStringRule(value_provider, evaluator, view_name) 
    filter = ElementParameterFilter(rule)
    view = FilteredElementCollector(doc).OfClass(View3D).WherePasses(filter).ToElements()[0]
    return view


#TODO Recopilamos inputs y los guardamos en listas
rooms_list = UnwrapElement(IN[0])
parameters = IN[1]
view_name = IN[2]

doc = DocumentManager.Instance.CurrentDBDocument
view = getView_ByName(view_name)


#TODO Ejecución

ui = Alimentador_Parametros(parameters, doc, view)
ui.bindRoomsList(rooms_list)
ui.ShowDialog()

OUT = 0