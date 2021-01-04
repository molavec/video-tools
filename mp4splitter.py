#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
sys.path.append('/usr/local/lib/python3.8/site-packages')
#print(sys.version)

import yaml
import getopt
from pathlib import Path

from lib.clipMovie import clipMovie, copyFile



def main(argv):

  HELP_TEXT = """
  DESCRIPCION:
      Create a movie from clips.
      This action should be do after get clips with slipper app.

  HOW TO USE:
      mp4splitter [-h --help] [-k --keep-file] clips_yml tag_name

  OPTIONS:
      -h --help show this help
      -g --generate-file create a clips.yml example file
      clips_yml Yaml file with list of clips
      tag_name tag used to select clips to be merge

  """

  #obtiene los argumentos
  try:
    opts, args = getopt.getopt(argv,"hg",["help=","generate-file="])
  except getopt.error as error:
    print(HELP_TEXT)
    sys.exit(2)
  for opt, value in opts:
    if opt == '-h':
      print(HELP_TEXT)
      sys.exit()
    if opt == '-g':
      copyFile('./lib/clips_copy.yml', "clips.yml") # TODO: veridicar que no este el archivo creado
      sys.exit()

  # Inicia variables
  splitConfig = ''
  inputFilename = ''
  outputFolder = 'clips'
  clips = []

  # Verifica argumento con archivo configuración
  if len(args) < 1:
    print(HELP_TEXT)
    sys.exit(2)

  # Lee el archivo Yaml
  with open(args[0], 'r') as stream:
    try:
      splitConfig = yaml.safe_load(stream)
      inputFilename = splitConfig.get('input')
      outputFolder = splitConfig.get('outputFolder')
      clips = splitConfig.get('clips')
    except yaml.YAMLError as exc:
      print(exc)

  # Crea la carpeta de salida
  Path('./'+outputFolder).mkdir(parents=True, exist_ok=True)

  # genera los clips
  for clip in clips:
    outPath = './' + outputFolder + '/' + clip.get('title')
    process = clipMovie(input=inputFilename, initTime=clip.get('init'), endTime=clip.get('end'), output=outPath)
    #print(process.returncode)

  #process = clipMovie(input='movie.mp4', initTime='00:10:08', endTime='00:10:03', output='cut.mp4')
  #print(process.returncode)


if __name__ == "__main__":
   main(sys.argv[1:])
