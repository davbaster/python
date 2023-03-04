from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget
import openpyxl


class Formulario(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crea los widgets de entrada de texto y las etiquetas
        self.octane_url_label = QLabel("Octane Url:")
        self.octane_url_text_field = QLineEdit()
        self.shared_space_label = QLabel("Shared Space:")
        self.shared_space_text_field = QLineEdit()
        self.udf_field_label = QLabel("UDF Field:")
        self.udf_field_text_field = QLineEdit()
        self.value_id_label = QLabel("Value Id:")
        self.value_id_text_field = QLineEdit()

        # Crea el botón "Exportar"
        self.exportar_button = QPushButton("Exportar")
        self.exportar_button.clicked.connect(self.exportar_datos)

        # Agrega los widgets de entrada de texto y las etiquetas a un layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.octane_url_label)
        layout.addWidget(self.octane_url_text_field)
        layout.addWidget(self.shared_space_label)
        layout.addWidget(self.shared_space_text_field)
        layout.addWidget(self.udf_field_label)
        layout.addWidget(self.udf_field_text_field)
        layout.addWidget(self.value_id_label)
        layout.addWidget(self.value_id_text_field)

        # Agrega el botón "Exportar" al layout
        layout.addWidget(self.exportar_button)
        

        # Crea un widget central que contenga el layout vertical
        widget = QWidget()
        widget.setLayout(layout)

        # Establece el widget central de la ventana como el widget que acabamos de crear
        self.setCentralWidget(widget)

    def exportar_datos(self):
        # Obtener los valores de entrada de texto
        octane_url = self.octane_url_text_field.text()
        shared_space = self.shared_space_text_field.text()
        udf_field = self.udf_field_text_field.text()
        value_id = self.value_id_text_field.text()
        entity = "work_items"

        # Abre el archivo Excel
        workbook = openpyxl.load_workbook('WORKSPACES.xlsx')

        # Selecciona la hoja del archivo
        worksheet = workbook['WORKSPACES']

        # Lee los datos de la columna A y B y los almacena en una lista
        data = []
        for row in worksheet.iter_rows(min_row=2, values_only=True):
            wsid = row[0]
            #name = row[1]
            #status = row[2]

            #concatenated_string = f"{column_a_value} {column_b_value}"
            APIcall = octane_url + "/api/shared_spaces/" + str(shared_space) + "/workspaces/" + str(wsid) + "/" + entity + "?fields=id,name," + udf_field + "&query=\"" + udf_field + "={id+IN+'" + str(value_id) + "'}\""
            print(APIcall)
        
        data.append(APIcall)

        # Crear un nuevo libro de Excel
        new_workbook = openpyxl.Workbook()

        # Crear una nueva hoja de trabajo en el libro de Excel
        new_worksheet = new_workbook.active
        new_worksheet.title = 'workitems'

        # Escribir los datos de la estructura de datos junto con los valores de entrada de texto en el archivo de Excel
        for row in self.data:
            #for column in row:
                #new_worksheet.cell(row=row.index(column) + 1, column=1, value=str(column))
            new_worksheet.cell(row.index(row), 1, row)

        # Guardar el libro de Excel
        new_workbook.save("resultados.xlsx")

if __name__ == '__main__':
   
    app = QApplication([])
    ventana = Formulario()
    ventana.show()
    app.exec_()
