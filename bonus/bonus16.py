import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to complress: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="files")

label2 = sg.Text("Selec destination folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="Output", text_color="green")

window = sg.Window("Compressor", layout=[[label1, input1, choose_button1],
                                         [label2, input2, choose_button2],
                                         [compress_button]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive((filepaths, folder))
    window["output"].update(value="Compression Completed")

window.close()