📦 Installation
1. Clone this project
git clone <your-repo-url>
cd <project-folder>

2. Create & activate virtual environment (recommended)
Windows:
python -m venv venv
venv\Scripts\activate

macOS / Linux:
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

📥 Download YOLO Model Weights

Place your model (e.g., yolo11l.pt) in the project folder.

You can download models here:
https://models.ultralytics.com/

▶️ Running the Detection Script
1. Webcam Mode
python main.py

2. Using a Video File

Edit this line in your script:

VIDEO_SOURCE = "your_video.mp4"


Then run:

python main.py

📝 Features

Real-time YOLO object detection

Counts objects per frame

Shows detection results on screen

Supports webcam or video file

Easy to configure and extend