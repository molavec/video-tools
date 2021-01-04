import subprocess
from pathlib import Path

# Define a function `plus()`
#def getClip(starTime, endTime, input, output):
def clipMovie(input, initTime, endTime, output="cut.mp4"):
  process = subprocess.run(
          [
            'ffmpeg',
            '-y',
            '-t', endTime,
            '-i', input,
            '-ss', initTime,
            '-async', '1',
            '-c', 'copy',
            output],
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE,
          text=True
          )
  if process.returncode == 0:
    print(output + ' created')
  else:
    print("## Error")
    print(process.stderr)

  return process


def copyFile(input, output):

  # verifica si el archivo existe
  if Path(output).exists():
    print(output + ' alredy exists!')
    return

  process = subprocess.run(
          [
            'cp',
            input,
            output
          ],
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE,
          text=True
          )
  if process.returncode == 0:
    print('clips.yml example file created!')
  else:
    print("## Error")
    print(process.stderr)

  return process

def removeFile(file):

  process = subprocess.run(
          [
            'rm',
            '-f',
            file
          ],
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE,
          text=True
          )
  if process.returncode == 0:
    print('remove ' + file)
  else:
    print("## Error")
    print(process.stderr)

  return process



def concatClips(tag, output):
  process = subprocess.run(
          [
            'ffmpeg',
            '-y',
            '-f', 'concat',
            '-i', tag,
            '-vcodec', 'copy',
            '-acodec', 'copy',
            output],
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE,
          text=True
          )
  if process.returncode == 0:
    print(output + ' created')
  else:
    print("## Error")
    print(process.stderr)

  return process
