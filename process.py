import sys
import argparse
import logging
import pathlib
import json

import cv2

from blur_detection import estimate_blur
from blur_detection import fix_image_size
from blur_detection import pretty_blur_map

def parse_args():
    parser = argparse.ArgumentParser(description='run blur detection on a single image')
    parser.add_argument('-i', '--images', type=str, nargs='+', required=True, help='directory of images')
    parser.add_argument('-s', '--save-path', type=str, default=None, help='path to save output')

    parser.add_argument('-t', '--threshold', type=float, default=100.0, help='blurry threshold')
    parser.add_argument('-f', '--variable-size', action='store_true', help='fix the image size')

    parser.add_argument('-v', '--verbose', action='store_true', help='set logging level to debug')
    parser.add_argument('-d', '--display', action='store_true', help='display images')

    return parser.parse_args()


def find_images(image_paths, img_extensions=['.jpg', '.png', '.jpeg']):
    img_extensions += [i.upper() for i in img_extensions]

    for path in image_paths:
        path = pathlib.Path(path)

        if path.is_file():
            if path.suffix not in img_extensions:
                logging.info(f'{path.suffix} is not an image extension! skipping {path}')
                continue
            else:
                yield path

        if path.is_dir():
            for img_ext in img_extensions:
                yield from path.rglob(f'*{img_ext}')

