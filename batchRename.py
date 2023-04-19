import subprocess
import os
root_dir = './/files//'  # set the root directory
cover = r'.//bin//cover.jpg'
with open('.//bin//YourName.txt','r') as file:
    YourName = file.read()

# loop through all files in the root directory
for filename in os.listdir(root_dir):
    if filename.endswith('.mkv'):
        input_file = os.path.join(root_dir, filename)
        output = subprocess.run([".\\bin\\mkvmerge.exe", "-i", input_file], capture_output=True, text=True)

        video_count = output.stdout.count("video")
        audio_count = output.stdout.count("audio")
        subtitle_count = output.stdout.count("subtitle")

        print(f"Number of video tracks: {video_count}")
        print(f"Number of audio tracks: {audio_count}")
        print(f"Number of subtitle tracks: {subtitle_count}")

        i = 1
        while(i<=video_count):
            os.system(f'''.\\bin\\mkvpropedit.exe "{input_file}" --edit track:v{i} --set name="{YourName}"''')
            i=i+1

        i=1
        while(i<=audio_count):
            os.system(f'''.\\bin\\mkvpropedit.exe "{input_file}" --edit track:a{i} --set name="{YourName}"''')
            i=i+1

        i=1
        while(i<=subtitle_count):
            os.system(f'''.\\bin\\mkvpropedit.exe "{input_file}" --edit track:s{i} --set name="{YourName}"''')
            i=i+1

        os.system(f'''.\\bin\\mkvpropedit.exe "{input_file}" --edit info --set "title={YourName}"''')
        os.system(f'''.\\\bin\\mkvpropedit.exe "{input_file}" --delete-attachment mime-type:image/jpeg''')
        os.system(f'''.\\bin\\mkvpropedit.exe "{input_file}" --add-attachment "{cover}"''')