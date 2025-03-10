import PySimpleGUI as sg
import Encoder
import Decoder

layout = [
    [sg.Text('Select image to encode message into:', expand_x=True,  size=(30, 1)),
     sg.InputText(key="-IMAGE_PATH-", expand_x=True, size=(40, 1)), sg.FileBrowse()],

    [sg.Text('Select where to save the image:',expand_x=True, size=(30, 1)),
     sg.InputText(key="-SAVE_PATH-",expand_x=True, size=(40, 1)), sg.SaveAs()],

    [sg.Text("Content of your message:", expand_x=True,size=(30, 1))],
    [sg.Multiline(key="-MESSAGE-", size=(60, 5))],

    [sg.Button('Encode', size=(12, 1))],

    [sg.HorizontalSeparator()],

    [sg.Text('Select path of image with encoded message:', expand_x=True,size=(30, 1)),
     sg.InputText(key="-ENCODED_IMAGE-", size=(40, 1)), sg.FileBrowse()],

    [sg.Button('Decode', size=(12, 1))],

    [sg.Output(size=(60, 5))],

    [sg.HorizontalSeparator()],

    [sg.Button('Close', size=(12, 1))]
]



window = sg.Window("Steganography Encoder", layout, element_justification='c', font=("Consolas", 12),size=(900, 400))

encoder = Encoder.Encoder()
decoder = Decoder.Decoder()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == 'Encode':
        encoder.set_image_path(values["-IMAGE_PATH-"])
        encoder.set_output_path(values["-SAVE_PATH-"])
        encoder.encode(values["-MESSAGE-"])
    elif event == 'Decode':
        decoder.set_image_path(values["-ENCODED_IMAGE-"])
        out = decoder.decode()
        print(out)


window.close()