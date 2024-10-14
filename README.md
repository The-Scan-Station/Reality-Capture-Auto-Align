# Reality Capture Auto Align

This is a python script for aligning and saving multiple projects at once.

## Step 1: Make sure you have python installed on your machine:
To check if Python is installed, open a terminal and run:

```sh
python --version
```

If Python is installed, you will see a version number. If not, you can download and install Python from the [official website](https://www.python.org/downloads/).

## Step 2: Set the up the images directory
This step assumes that you have a directory with the following structure:
- directory:
  |_sub-directory:
    |_img1.jpg
    |_img2.jpg
    |_...
    |_imgN.jpg

Where there can be an N amount of subdirectories. 

In the `rc_auto_align.ipynb` set the variable:
`images_dir = r"*THE_LOCATION_OF_YOUR_DIRECTORY*"`

## Step 3: Point at the location of the Reality Capture Folder
This is where you look at the path of the Reality Capture.exe executable.

Set the following variable:
`RealityCapture = r"*THE_PATH_TO_RC.exe"`

## Step 4: Set up the folder for saving the data:
`save_dir = r"*WHERE_YOU_WOULD_LIKE_TO_SAVE_THE_RCPROJ_FILES"`

## Step 5: Running the script on Windows
When you run the script, you should see multiple instances of Reality Capture spin up and start to align the images. Each instance will complete the alignment and then save the files in the corresponding folder.

To run the Python script on a Windows machine, follow these steps:

1. Open Command Prompt. You can do this by pressing `Win + R`, typing `cmd`, and hitting Enter.
2. Navigate to the directory where your Python script is located. You can use the `cd` command to change directories. For example:
   
   ```sh
   cd C:\path\to\your\script
   ```

3. Once you are in the correct directory, run the script by typing:

   ```sh
   python rc_auto_align.py
   ```

Make sure to replace `rc_auto_align.py` with the actual name of your Python script if it is different.


### Happy Coding! Albert Fit