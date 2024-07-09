import os
from tkinter import Tk, filedialog, messagebox, Label, Button, Canvas
from imgfunc import *
from moviepy.editor import VideoFileClip
from PIL import Image, ImageTk
import webbrowser

# Define or import the frame_processor function
def frame_processor(image):
    """
    Process the input frame to detect lane lines.
        Parameters:
            image: Single video frame.
    """
    color_select = HSL_color_selection(image)
    gray         = gray_scale(color_select)
    smooth       = gaussian_smoothing(gray)
    edges        = canny_detector(smooth)
    region       = region_selection(edges)
    hough        = hough_transform(region)
    result       = draw_lane_lines(image, lane_lines(image, hough))
    return result 

# Create a function to display the images
def display_images():
    # Iterate through all images in the 'output_images' folder
    for filename in os.listdir('output_images'):
        if filename.endswith('.jpg'):
            image_path = os.path.join('output_images', filename)
            image = Image.open(image_path)
            image.show()

# Create a function to select the video file using Tkinter
def select_video(root):
    # Prompt user to select a video file
    video_path = filedialog.askopenfilename(initialdir=os.path.join(os.getcwd(), 'test_videos'), title="Select Video File", filetypes=(("MP4 files", "*.mp4"), ("All files", "*.*")))
    if video_path:
        process_video(video_path)
    else:
        messagebox.showwarning("No file selected", "Please select a video file.")

def process_video(video_path):
    # Extract the name of the input video file
    input_video_name = os.path.splitext(os.path.basename(video_path))[0]
    output_video_name = f"{input_video_name}_output.mp4"  # Append "_output" to the input video name

    # Dummy implementation for demonstration
    input_video = VideoFileClip(video_path)
    processed = input_video.fl_image(frame_processor)
    processed.write_videofile(os.path.join('output_videos', output_video_name), audio=False)

    # Open the output video in the default web browser
    webbrowser.open(os.path.join('output_videos', output_video_name))

def main():
    root = Tk()
    root.title("Lane Detection System")   # Title of the window

    # Load the background image
    background_image = Image.open("background.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # Set the window size to match the image size
    root.geometry(f"{background_image.width}x{background_image.height}")

    canvas = Canvas(root, width=background_image.width, height=background_image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    canvas.create_text(background_image.width // 2, 200, text="Lane Detection System", font=("Helvetica", 70, "bold"), fill="white")

    # Add a button to select video
    select_button = Button(root, text="Select Video", command=lambda: select_video(root), font=("Helvetica", 20), bg="grey", fg="white", bd=0, padx=20, pady=10)
    select_button_window = canvas.create_window(background_image.width // 2, background_image.height // 2, window=select_button)

    root.mainloop()

if __name__ == "__main__":
    main()
