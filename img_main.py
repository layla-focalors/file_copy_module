import shutil
import uuid
import os
file_names=os.listdir('./target')

p = 0

for i in file_names:
    file_namess=os.listdir(f'./target/{i}')
    for j in file_namess:
        splot = j.split('.')
        print(splot[1])
        print(f"processing :  {j}")
        shutil.copy(f'./target/{i}/{j}', f'C:\\Users\\user\\Desktop\\output\\{str(p) + ".png"}')
        p += 1
    