from PIL import Image
import os

def convert_webp_to_png(input_folder,  output_folder):
    #Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)
    #List all files in the input folder
    files = os.listdir(input_folder)

    for filename in files:
        if filename.endswith('.webp'):
            #Construct the input and output file paths
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.png')

            #Open Webp Image and Save as PNG
            img = Image.open(input_path)
            img.save(output_path, 'PNG')

if __name__ == "__main__":
    input_folder = 'C:/Codex/ImageFolder/DallE' # Replace with your input folder 
    output_folder = 'C:/Codex/ImageFolder/DallE_png' #Replace with your output folder

convert_webp_to_png(input_folder, output_folder)
