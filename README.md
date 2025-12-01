<h1>📦 Installation</h1>
<ol>
  <li>Clone this project</li>
  <ul>
    <li>git clone https://github.com/BonaDenyS/Simple-Person-Detection-YOLO-</li>
    <li>cd Simple-Person-Detection-YOLO-</li>
  </ul>
  <li>Create & activate virtual environment/li>
  <ul>
    <li>Windows:</li>
    <ul>
      <li>python -m venv venv</li>
      <li>venv\Scripts\activate</li>
    </ul>
    <li>macOS / Linux:</li>
    <ul>
      <li>python3 -m venv venv</li>
      <li>source venv/bin/activate</li>
    </ul>
  </ul>
  <li>Install dependencies</li>
  <ul>
    <li>pip install -r requirements.txt</li>
  </ul>
</ol>

<h1>📥 Download YOLO Model Weights</h1>

Place your model (e.g., yolo11l.pt) in the project folder.

You can download models here:
https://models.ultralytics.com/

<h1>▶️ Running the Detection Script</h1>
<ol>
  <li>Webcame Mode</li>
      python main.py
  <li>Using a Video File</li>
  <ul>
    <li>Edit this line in your script:</li>
        VIDEO_SOURCE = "your_video.mp4"
    <li>Then run:</li>
        python main.py
  </ul>
</ol>

<h1>📝 Features</h1>
<ul>
  <li>Real-time YOLO object detection</li>
  <li>Counts objects per frame</li>
  <li>Shows detection results on screen</li>
  <li>Supports webcam or video file</li>
  <li>Easy to configure and extend</li>
</ul>
