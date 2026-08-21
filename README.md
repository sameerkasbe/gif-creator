# GIF Creator

A simple Python desktop application that converts video files into animated GIFs. The application provides a graphical interface for selecting videos, previewing frames, setting the GIF FPS, and saving the final GIF.

## ✨ Features

*  Select video files (`MP4`, `AVI`, `MOV`)
*  Preview the selected video's first frame
*  Convert videos into animated GIFs
*  Customize GIF FPS
*  Live frame preview during conversion
*  Choose where to save the generated GIF
*  Uses threading to keep the application responsive during conversion

## Technologies Used

* **Python**
* **Tkinter** – Desktop graphical user interface
* **OpenCV** – Video reading and frame processing
* **Pillow (PIL)** – Image processing and GIF creation
* **Threading** – Background GIF conversion

##  Project Structure

```text
gif-creator/
│
├── gif_creator.py
├── README.md
└── requirements.txt
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/gif-creator.git
cd gif-creator
```

### 2. Install the required libraries

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install opencv-python Pillow
```

##  How to Run

Run the Python file:

```bash
python gif_creator.py
```

### Steps

1. Click **Select Video**
2. Choose an `MP4`, `AVI`, or `MOV` file
3. Preview the selected video
4. Enter the desired FPS
5. Click **Convert to GIF**
6. Choose the location to save the GIF
7. Your animated GIF will be generated

How It Works

The application uses **OpenCV** to read the video frame by frame. Each frame is converted from OpenCV's BGR format to RGB and processed using **Pillow**.

The processed frames are then combined into an animated GIF. The GIF duration is calculated from the selected FPS:

```text
Frame Duration = 1000 / FPS milliseconds
```

Threading is used during conversion so that the GUI remains responsive while the video is being processed.

Future Improvements

* Add GIF resolution and quality controls
* Add video trimming (start/end time)
* Add GIF preview before saving
* Add progress bar for conversion
* Add drag-and-drop video support
* Add support for more video formats
* Package the application as a standalone `.exe`

👨‍💻 Author

**Sameer Kasbe**

Built as a Python project to explore GUI development, video processing, image manipulation, and GIF generation.
