# Video Tools

Terminal scripts to simplify videos actions as convert format, extract screenshots, etc.

## Requirements

* brew install ffmpeg
* pip install pyyaml pathlib

# List of Tools

* **avi2mp4:** transform avi to mp4.
* **mp4splitter:** Create clips from MP4 from Yaml config file.
* **mp4concat:** concat clips from Yaml config file.
* **video2gif:** transform video to gif

## avi2mp4

```bash
avi2mp4 [-d output_directory]
```

## splitter

Hay que crear un archivo `yaml` con las opciones de los extractos.
Los clips se definen en un archivo `clips.yml`

```yaml
input: movie.mp4
outputFolder: out

clips:
  - title: parte_01.mp4
    init: 00:00:56
    end: 00:01:32
    description: Presentación inicial
    tags:
      - protagonista
      - social

  - title: parte_02.mp4
    init: 00:01:32
    end: 00:03:18
    description: Primera escena
    tags:
      - social
```

```bash
python splitter.py clips.yml
```

## concatena

1.- Crear un archivo con el listado de los clip asociados a un tag.

```bash
python mp4concat.py clips.yml social
```

## video2gif

Convierte un video en gif sin perdida de calidad.

```bash
video2gif [-s start_time] [-t duration] [-S scale] input_file output_file
```

