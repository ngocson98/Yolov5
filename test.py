import tkinter as tk
import customtkinter as ctk
import torch
import numpy as np
import pandas as pd
import cv2

from PIL import Image, ImageTk

app = tk.Tk()
app.geometry("720x720")
app.title("Test Yolov5")
ctk.set_appearance_mode("dark")
vidFrame = tk.Frame(app, bg='black', width=720, height=720)
vidFrame.pack(padx=20, pady=20)
vid = ctk.CTkLabel(vidFrame)
vid.pack()

model = torch.hub.load('ultralytics/yolov5', 'custom', path='module/best_all.pt', force_reload=True)

cap = cv2.VideoCapture(2, cv2.CAP_DSHOW)
def detect():
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(frame)
    img = np.squeeze(results.render())

    imgarr = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(imgarr)
    vid.imgtk = imgtk
    vid.configure(image = imgtk)
    vid.after(100, detect)

detect()
app.mainloop()
