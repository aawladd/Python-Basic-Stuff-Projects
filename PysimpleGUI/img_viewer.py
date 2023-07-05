import PySimpleGUI as sg
import os.path

from PySimpleGUI.PySimpleGUI import Image, Window

#Window layout of two columns

file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40,20),
            key="-FILE LIST-"
        )
    ],
 ]



image_viewer_column = [
    [sg.Text("Choosen an image from the list on the left: ")],
    [sg.Text(size=(40,1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

#-----FULL layout ------

layout = [
    sg.Column(file_list_column),
    sg.VSeparator(),
    sg.Column(image_viewer_column),
]

Window = sg.Window("Image Viewer", layout)



while True:
    event, values = Window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

Window.close()