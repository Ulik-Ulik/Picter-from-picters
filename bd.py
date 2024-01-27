import os

content = os.listdir(r".\pct")

for cnt, name in enumerate(content):
    os.rename(os.path.join(r".\pct", name), os.path.join(r".\pct", 'r' + str(cnt) + '.jpg'))

