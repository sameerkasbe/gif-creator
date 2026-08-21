import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os


import cv2
from PIL import Image, ImageTk


class GIFMaker:
    def __init__(self, root):
        self.root = root
        self.root.title("GIF Maker")
        self.root.geometry("500x450")

        self.video_path = None
        self.frames = []

        # UI
        self.label = ttk.Label(root, text="No video selected")
        self.label.pack(pady=10)

        ttk.Button(root, text="Select Video", command=self.select_video).pack(pady=5)
        ttk.Button(root, text="Convert to GIF", command=self.start_conversion).pack(pady=5)

        ttk.Label(root, text="FPS:").pack()
        self.fps_entry = ttk.Entry(root)
        self.fps_entry.insert(0, "10")
        self.fps_entry.pack()

        self.canvas = tk.Canvas(root, width=400, height=300, bg="black")
        self.canvas.pack(pady=10)

    # 🎬 SELECT VIDEO + PREVIEW FIRST FRAME
    def select_video(self):
        path = filedialog.askopenfilename(
            filetypes=[("Video Files", "*.mp4 *.avi *.mov")]
        )

        if path:
            self.video_path = path
            self.label.config(text=os.path.basename(path))

            cap = cv2.VideoCapture(path)
            ret, frame = cap.read()

            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (400, 300))

                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)

                self.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
                self.canvas.image = imgtk

            cap.release()
            

    # 🚀 THREAD START
    def start_conversion(self):
        thread = threading.Thread(target=self.convert_to_gif)
        thread.start()

    # 🔁 CONVERT VIDEO → GIF
    def convert_to_gif(self):
        if not self.video_path:
            messagebox.showerror("Error", "Select a video first!")
            return

        save_path = filedialog.asksaveasfilename(
            defaultextension=".gif",
            filetypes=[("GIF files", "*.gif")]
        )

        if not save_path:
            return

        # 🔒 Force .gif extension
        if not save_path.lower().endswith(".gif"):
            save_path += ".gif"

        try:
            fps = int(self.fps_entry.get())
        except:
            messagebox.showerror("Error", "Invalid FPS")
            return

        cap = cv2.VideoCapture(self.video_path)
        self.frames = []

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (400, 300))

            img = Image.fromarray(frame)
            self.frames.append(img)

            # 🔥 Live preview during conversion
            imgtk = ImageTk.PhotoImage(image=img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
            self.canvas.image = imgtk

        cap.release()

        if self.frames:
            self.frames[0].save(
                save_path,
                save_all=True,
                append_images=self.frames[1:],
                duration=int(1000 / fps),
                loop=0
            )
            messagebox.showinfo("Success", "GIF Created Successfully!")


# ▶️ RUN APP
root = tk.Tk()
app = GIFMaker(root)
root.mainloop()