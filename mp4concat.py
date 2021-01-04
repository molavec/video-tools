#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
sys.path.append('/usr/local/lib/python3.8/site-packages')
#print(sys.version)

import getopt
from pathlib import Path
import yaml

from lib.clipMovie import concatClips, removeFile



def main(argv):

  HELP_TEXT = """
DESCRIPCION:
    Create a movie from clips.
    This action should be do after get clips with slipper app.

HOW TO USE:
    mp4concat [-h --help] [-k --keep-file] clips_yml tag_name

OPTIONS:
    -h --help punto de inicio en el vídeo
    -k keep file with list of clips will be merge
    clips_yml Yaml file with list of clips
    tag_name tag used to select clips to be merge

"""

  KeepAuxFiles = False
  tagName = ''

  try:
    opts, args = getopt.getopt(argv,"hk",["help=", "keep-file="])
  except getopt.error as error:
    print(HELP_TEXT)
    sys.exit(2)
  for opt, value in opts:
    if opt == '-h':
      print(HELP_TEXT)
      sys.exit()
    if opt == '-k':
      KeepAuxFiles = True

  # Verifica argumento con archivo configuración
  if len(args) < 1:
    print(HELP_TEXT)
    sys.exit(2)

  # Inicia variables
  tagName = args[1]


  # Lee el archivo Yaml
  with open(args[0], 'r') as stream:
    try:
      splitConfig = yaml.safe_load(stream)
      clipsFolder = splitConfig.get('outputFolder')
      clips = splitConfig.get('clips')
    except yaml.YAMLError as exc:
      print(exc)



  # Abre el archivo de tags
  filename = tagName
  f=open(filename, "a+")

  # Obtiene los clips con el tag requerido
  for clip in clips:
    tags = clip.get('tags')
    for tag in tags:
      if tag == tagName:
        outPath = clipsFolder + '/' + clip.get('title')
        f.write("file " + outPath + '\n')
  # Cierra el archivo
  f.close()


  # Crea la carpeta de salida
  outputFolder = './output'
  Path('./'+outputFolder).mkdir(parents=True, exist_ok=True)

  # Concatena clips
  outputFilename = outputFolder + '/' + tagName + '.mp4'
  concatClips(tagName, outputFilename)

  # Elimina archivo temporal
  if KeepAuxFiles == False:
    removeFile(tagName)

if __name__ == "__main__":
   main(sys.argv[1:])
