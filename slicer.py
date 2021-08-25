# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 11:46:08 2021

@author: jagra26
"""
from alive_progress import alive_bar
import glob
import os
import argparse
from ripper import slice, save_tiles

def get_prefix(filename, foldername):
    splitedFile = filename.split("\\")
    splitedFile = splitedFile[-1].split(".")
    splitedFolder = foldername.split("\\")
    return splitedFolder[-1] + "_" + splitedFile[0]
    

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="path to folder", default="testImages")
#parser.add_argument("-d", "--directory", help="output directory")
parser.add_argument("-c", "--collumns", type=int, help="number of collumns", default=8)
parser.add_argument("-r", "--rows", type=int, help="number of rows", default=6)
args = parser.parse_args()


for folder in glob.glob(args.path + "/*"):
    if not folder.endswith("Sliced"):
        print(folder)
        if not os.path.exists(folder + "Sliced"):
            os.mkdir( folder + "Sliced")
        directory = folder + "Sliced"

        files = glob.glob(folder+"/*")

        with alive_bar(len(files)) as bar1:
            for i in range(len(files)):
                try:
                    filename = files[i]
                    tiles = slice(filename, col=args.collumns, row=args.rows, save=False)
                    save_tiles(tiles, prefix=get_prefix(filename, folder), directory=directory)
                    bar1()
                except Exception as e: print(e)
        print("end")