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
|-c| Collums| 8|
|-r| Rows| 6|

example:

```
python slicer.py -p folderWithFoldersWithImages
```

## Ripper

library based on [image-slicer](https://github.com/samdobson/image_slicer), [numpy](https://numpy.org) and [opencv](https://opencv.org) to slice images