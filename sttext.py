
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

list=[]

import speech_recognition as sr

r = sr.Recognizer()

my_mic = sr.Microphone(device_index=1)

for i in range(1,5):
    with my_mic as source:
        print("Say now!!!!i")
        audio = r.listen(source)
        
        list.append(r.recognize_google(audio))
    
