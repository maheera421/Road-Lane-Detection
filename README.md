# Road-Lane-Detection

🚀 **Code Description:**
This code is a Road Lane Detection system using Digital Image Processing techniques. It processes video frames to detect and highlight lane lines on roads. Here's how it works:

1. **Initialization:**
   - Imports necessary packages such as OpenCV, NumPy, Matplotlib, MoviePy, and others.
2. **Image Processing Functions:**
   - Contains several functions to process images and detect lane lines, including color selection, grayscale conversion, Gaussian smoothing, Canny edge detection, region selection, Hough Transform, and line drawing.
3. **Video Processing:**
   - Uses MoviePy to process video frames and apply the lane detection pipeline to each frame.
4. **User Interface:**
   - Provides a simple graphical interface to select and process videos using Tkinter.

🔍 **Code Breakdown:**

### Image Processing (imgfunc.py)

1. **list_images(images, cols=2, rows=5, cmap=None, title=None):**
   - Displays a list of images in a single figure using Matplotlib.
2. **RGB_color_selection(image):**
   - Applies color selection to RGB images to keep only white and yellow lane lines.
3. **convert_hsv(image):**
   - Converts RGB images to HSV color space.
4. **HSV_color_selection(image):**
   - Applies color selection to HSV images to keep only white and yellow lane lines.
5. **convert_hsl(image):**
   - Converts RGB images to HSL color space.
6. **HSL_color_selection(image):**
   - Applies color selection to HSL images to keep only white and yellow lane lines.
7. **gray_scale(image):**
   - Converts images to grayscale.
8. **gaussian_smoothing(image, kernel_size=13):**
   - Applies Gaussian Blur to the input image for smoothing.
9. **canny_detector(image, low_threshold=50, high_threshold=150):**
   - Applies Canny Edge Detection to the input image.
10. **region_selection(image):**
    - Defines and applies a mask to keep the region of interest in the image.
11. **hough_transform(image):**
    - Applies Hough Transform to detect lines in the masked image.
12. **draw_lines(image, lines, color=[255, 0, 0], thickness=2):**
    - Draws detected lines onto the image.
13. **lane_lines(image, lines):**
    - Creates full-length lane lines from detected line segments.
14. **draw_lane_lines(image, lines, color=[255, 0, 0], thickness=12):**
    - Draws lane lines onto the input image.

### Video Processing and GUI (vid.py)

1. **frame_processor(image):**
   - Processes each video frame to detect and highlight lane lines.
2. **display_images():**
   - Displays processed images from the 'output_images' folder.
3. **select_video(root):**
   - Allows the user to select a video file for processing.
4. **process_video(video_path):**
   - Processes the selected video and saves the output with detected lane lines.
5. **main():**
   - Initializes the Tkinter GUI, sets up the interface, and runs the application.

**🔐 Code Specifications:**
- **Dependencies:**
  - The code uses several external modules including OpenCV, NumPy, Matplotlib, MoviePy, Tkinter, and PIL. Ensure these are installed in your environment.

- **Customization:**
  - Users can adjust parameters such as color thresholds, Gaussian kernel size, Canny edge detection thresholds, and Hough Transform parameters for optimal lane detection performance.

- **Folder Structure:**
  - Ensure the project contains `test_images`, `test_videos`, `output_images`, and `output_videos` folders. The `myenv` and `__pycache__` folders are created during environment setup and can be ignored.

- **Execution:**
  - Run the `vid.py` script to launch the GUI and select a video for lane detection.
