import os
from pathlib import Path

def push(message):
    pathlist = Path("./Visualisations").glob('*.png')
    with open(Path("./README.md"),"w+") as file:
        file.write("# COVID-19 dataset visualisation\n\n## All the images(Graphs) are present in Visualisations directory.\n\n### Use main.py as the starting point of the project.\n\n##### Visualisations\n\n")
        for path in pathlist:
            file.write("![image]("+str(path)+")\n\n")
        file.close()
    os.system('git add -A && git commit -m "'+message+'" && git push -u origin master')