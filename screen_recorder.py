import PySimpleGUI as sg
import pyautogui
import cv2
import numpy as np
from win32api import GetSystemMetrics

start_recording_button = "Start"
stop_recording_button = "Stop"

resolution = (GetSystemMetrics(0), GetSystemMetrics(1))
codec = cv2.VideoWriter_fourcc(*"XVID")
layout = [[sg.Text("Screen Recorder")], [sg.Input('', do_not_clear=True)], [sg.Button(start_recording_button)],
          [sg.Button(stop_recording_button)]]
window = sg.Window("Demo", layout)
event, values = window.read()
if event == start_recording_button:
    # filename = '%s.avi' % str(values[0])
    filename = 'name.avi'
    fps = 30.0
    out = cv2.VideoWriter(filename, codec, fps, resolution)
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        event, values = window.read()
        if cv2.waitKey(1) == ord('q') or event == stop_recording_button or event == sg.WIN_CLOSED:
            break
    out.release()
    cv2.destroyAllWindows()
window.close()
