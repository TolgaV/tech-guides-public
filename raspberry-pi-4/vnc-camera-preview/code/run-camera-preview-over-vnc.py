from picamera2 import Picamera2
import cv2
import time

# Initialize the camera
picam2 = Picamera2()
# Keep the size small in case network is busy or slow
preview_config = picam2.create_preview_configuration(main={"size": (640, 480)})
picam2.configure(preview_config)
picam2.start()

# Allow time for the camera to warm up
time.sleep(2)

try:
    while True:
        # Capture a frame
        frame = picam2.capture_array()

        # Convert from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the frame
        cv2.imshow("Camera Preview", frame)

        # Check for 'q' key to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Clean up
    cv2.destroyAllWindows()
    picam2.stop()
