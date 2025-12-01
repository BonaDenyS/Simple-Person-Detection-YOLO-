import cv2
from ultralytics import YOLO

MODEL_WEIGHTS = "yolo11l.pt"
VIDEO_SOURCE = 0  # 0 = webcam
CONFIDENCE_THRESHOLD = 0.1

OBJECT_CLASS_ID = 0  # Class ID for 'person' in COCO dataset

def video_yolo_detection():
    print("Starting YOLO Person Detection...")
    model = YOLO(MODEL_WEIGHTS)
    cap = cv2.VideoCapture(VIDEO_SOURCE)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video stream or cannot read the frame.")
            break

        results = model(
            frame,
            conf=CONFIDENCE_THRESHOLD,
            classes=[OBJECT_CLASS_ID],
            show=False,
            verbose=False
        )

        for r in results:
            # Count objects (persons)
            object_count = 0
            if r.boxes is not None:
                object_count = len(r.boxes)

            # Annotated frame
            annotated = r.plot()

            # Draw object count on the frame
            cv2.putText(
                annotated,
                f"{object_count} Persons Detected",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            # Optional: print count to console
            print("Detected:", object_count)

            cv2.imshow('Persons Detection', annotated)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == 27:  # q or ESC
            break
    
    cap.release()
    cv2.destroyAllWindows()
    print("Video Detection Ended.")


if __name__ == "__main__":
    video_yolo_detection()