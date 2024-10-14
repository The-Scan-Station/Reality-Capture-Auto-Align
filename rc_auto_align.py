import os

#images directory
images_dir = r"C:\Users\A\Documents\ReconstructionDataSet-master"

#RealityCapture Installation 
RealityCapture = r"C:\Program Files\Capturing Reality\RealityCapture\RealityCapture.exe"

#Save directory
save_dir = r"C:\Users\A\Documents\ReconstructionDataSet-master\Projects"

#log all the folders in images_dir
folders = [name for name in os.listdir(images_dir) if os.path.isdir(os.path.join(images_dir, name))]
for index, folder in enumerate(folders):
    print(f'The folder at index {index} is: {folder}')
    print(f'The folder path is: {os.path.join(images_dir, folder)}')
    print(f'Processing {folder}...')
    command = f'"C:\Program Files\Capturing Reality\RealityCapture\RealityCapture.exe" -addFolder "{os.path.join(images_dir, folder)}" -save "{os.path.join(save_dir, folder)}\\{folder}.rcproj" -draft -quit'
    os.popen(command)
    print(f'Processing {folder} done!')