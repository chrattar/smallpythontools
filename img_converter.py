from PIL import Image
import os

def convert_webp_to_png(input_folder,  output_folder):
    os.makedirs(output_folder, exist_ok=True)
    files = os.listdir(input_folder) # LIST FILES IN DIR

    for filename in files:
        if filename.endswith('.webp'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.png')
            img = Image.open(input_path)
            img.save(output_path, 'PNG') 

if __name__ == "__main__":
    input_folder = '/input_dir'
    output_folder = '/output_dir'

convert_webp_to_png(input_folder, output_folder)
