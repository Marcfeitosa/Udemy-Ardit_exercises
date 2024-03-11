import PySimpleGUI as sg

sg.theme("DarkBlack")

label1 = sg.Text("Enter feet: ")
input1 = sg.Input()

label2 = sg.Text("Enter inches: ")
input2 = sg.Input()

convert_button = sg.Button("Convert")

output_label = sg.Text(key="output", text_color="white")

exit_button = sg.Button("Exit")

col1 = sg.Column([[label1], [label2]])
col2 = sg.Column([[input1], [input2]])

window = sg.Window("Convertor", layout=[[col1, col2],
                                             [convert_button, exit_button],
                                             [output_label]])

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    # Check if both input fields are empty
    if not values[0] and not values[1]:
        sg.popup_error("Please provide at least one variable.")
        continue

    feet = int(values[0]) if values[0] else 0
    inches = int(values[1]) if values[1] else 0

    meters = feet * 0.3048 + inches * 0.0254

    window["output"].update(value=f"{meters:.2f} meters")

window.close()
