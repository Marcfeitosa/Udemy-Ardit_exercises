import PySimpleGUI as sg

sg.theme("DarkGrey1")

label1 = sg.Text("Enter feet: ")
input1 = sg.Input()

label2 = sg.Text("Enter inches: ")
input2 = sg.Input()

convert_button = sg.Button("Convert")

output_label = sg.Text(key="output", text_color="white")

window = sg.Window("Convertor", layout=[[label1, input1],
                                             [label2, input2],
                                             [convert_button],
                                             [output_label]])

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    feet = int(values[0]) if values[0] else 0
    inches = int(values[1]) if values[1] else 0

    meters = feet * 0.3048 + inches * 0.0254

    window["output"].update(value=f"{meters:.2f} meters")

window.close()
