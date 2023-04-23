import PySimpleGUI as sg
from edot import edot

TITLE = "Even Doubler Odd Tripler (EDOT)"

sg.theme('DarkTeal10')


layout = [
    [sg.Text('', size=(20,1)), sg.Text(TITLE, font=('Any 20'), auto_size_text=True, justification='center'), sg.Text('', size=(20,1))],
    [sg.Text('File name to open: ')],
    [sg.Input(), sg.FileBrowse()],
    [sg.Button('Upload'), sg.Button('Quit')]
]

window = sg.Window(TITLE, layout, element_justification='center')

while True:
    event, values = window.read()

    if(event == sg.WIN_CLOSED or event == 'Quit'):
        break

    if(event == 'Upload'):
        try:
            edot(values[0])
            sg.popup_quick_message('New files successfully created within this directory')

        except:
            sg.popup_error('No such file found')

window.close()