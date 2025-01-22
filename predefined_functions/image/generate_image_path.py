from random import randint


def generate_image_save_path():
    imgfile = f"temp/{hex(hash(randint(1000000,9999999)))[2:]}.png"
    return imgfile
