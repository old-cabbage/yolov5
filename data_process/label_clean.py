import os
folder_path = r'C:\Users\OldCabbage\projects\YOLO\yolov5\data\data_animal_set\test\labels'
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'w') as file:
            file.truncate()