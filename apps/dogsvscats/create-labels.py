#!/usr/bin/python3

# ****************************************************************************
# Copyright(c) 2017 Intel Corporation. 
# License: MIT See LICENSE file in root directory.
# ****************************************************************************

# Create labels files for training & validation data 
# Usage: python create-labels.py /path/to/data/train/

import os
import sys
import glob
import ntpath

DATA_PATH = sys.argv[1]

# ---- Main function (entry point for this script ) --------------------------
def main():
    fVal = open( DATA_PATH + '/val.txt', 'w' )
    fTrain = open( DATA_PATH + '/train.txt', 'w' )

    file_list = []
    with open(os.path.join(DATA_PATH, 'annotations/list.txt')) as f:
        lines = f.readlines()
        for strline in lines:
            if '#' in strline:
                continue
            # Annotation format: image, id, SPECIES id, breed id
            # 1 -> cat, 2 -> dog
            # Abyssinian_100 1 1 1
            elems = strline.strip().split()
            image_file_name = elems[0]+'.jpg'
            class_id = elems[2]
            if class_id == '1':
                class_name = 'cat'
            else:
                class_name = 'dog'
            file_list.append((image_file_name, class_name))

    # Create a list of all files in current directory & sub-directories
    for file_index, (file_name, class_name) in enumerate( file_list ):
        if class_name == 'cat'  :
            if file_index % 6 == 0:
                fVal.write( file_name + ' 0\n' )
            else:
                fTrain.write( file_name + ' 0\n' )
        if class_name == 'dog':
            if file_index % 6 == 0:
                fVal.write( file_name + ' 1\n' )
            else:
                fTrain.write( file_name + ' 1\n' )

    fVal.close()
    fTrain.close()

# ---- Define 'main' function as the entry point for this script -------------

if __name__ == '__main__':
    main()

# ==== End of file ===========================================================
