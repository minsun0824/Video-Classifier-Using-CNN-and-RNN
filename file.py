import  os
import shutil

path = 'C:/Users/vml_sub/Documents/video_extrapolation/VideoOutpainting/davis_result'

for file in os.listdir(path):
    item_path = os.path.join(path, file, "input_video")
    dst_path = f'./dataset/{file}'
    shutil.copytree(item_path, dst_path)
    print(file)