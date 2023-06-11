import os
import subprocess

input_dir = 'input'
output_dir = 'output'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for file in os.listdir(input_dir):
    if file.endswith('.png'):
        input_file = os.path.join(input_dir, file)
        output_file = os.path.join(output_dir, file)
        command = f'ffmpeg -i "{input_file}" -filter_complex "[0:v] palettegen [palette],[0:v][palette] paletteuse" "{output_file}"'
        subprocess.run(command, shell=True)