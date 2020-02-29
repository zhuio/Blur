# Blur Detection
Blur Detection works using the total variance of the laplacian of an
image, this provides a quick and accurate method for scoring how blurry
an image is.

This package only depends on numpy and opencv, to install them run, 

```
pip install -U -r requirements.txt
```

```bash
# save this information to json
python main.py -i input_directory/ -s results.json

