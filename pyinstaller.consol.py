# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 21:22:12 2023

@author: V5
"""

# pyinstaller --name=your_executable_name --add-data="sound.mp3;." --onefile your_script.py


# пока самый рабочий вариант
pyinstaller --name=VIJU_INTEL --add-data="alarm_1.mp3;." --add-data="alarm_on.png;." --add-data="alarm_off.png;." --add-data="ocon_1.png;." -F --noconsole test_6.py






pyinstaller test_6.spec


pyi-makespec --onefile test_6.py




pyinstaller --name=VIJU_INTE --add-data="alarm_1.mp3:." --console=False --onefile test_6.py

Music


pyi-makespec --onefile --add-data="alarm_1.mp3:." test_6.py








Например, если все дополнительные файлы лежат в папке models:
pyinstaller -F --add-data coco-dataset.labels;models --add-data yolov3-tiny.cfg;models --add-data yolov3-tiny.weights;models pine.py