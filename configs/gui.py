import PySimpleGUI as sg
import wikipedia

def main():
  layout = [
    [sg.Text('Please enter something for search document on the Wikipedia')],
    [sg.Text('Search', size =(15, 1)), sg.InputText()],
    [sg.Submit()]
 ]

  window = sg.Window("WikiSearch Assistant", layout)
  while True:
    event, values = window.read()
    if values[0]:
     doc = wikipedia.page(values[0])
     return doc.content

    if event == "OK" or event == sg.WIN_CLOSED:
      break

  window.close()