# Turtle Detector

## Instalation

Install the packages

```
    pip install -r requirements.txt
```

## Slicer usage

|Arg|Purpose|Default|
|---|-------|-------|
|-p| Input path| testImages|
|-d| Output directory| |
|-c| Collums| 8|
|-r| Rows| 6|

example:

```
python slicer.py -p folderWithImages
```

## Ripper

library based on [image-slicer](https://github.com/samdobson/image_slicer), [numpy](https://numpy.org) and [opencv](https://opencv.org) to slice images