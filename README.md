# Blur Detection
Blur Detection works using the total variance of the laplacian of an
image, this provides a quick and accurate method for scoring how blurry
an image is.

This package only depends on numpy and opencv, to install them run, 

```
pip install -U -r requirements.txt
```

The repository has a script, `main.py` which lets us run on single images or directories of images. The blur detection method is highly dependent on the size of the image being processed. To get consistent scores we fix the image size to HD, to disable this use  `--variable-size`. The script has options to, 

```bash
# run on a single image
python main.py -i input_image.png

# run on a directory of images
python main.py -i input_directory/ 

# or both! 
python main.py -i input_directory/ other_directory/ input_image.png
```

. In addition to logging whether an image is blurry or not, we can also,

```bash
# save this information to json
python main.py -i input_directory/ -s results.json
# Blur
# Blur
