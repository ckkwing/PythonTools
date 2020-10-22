import os


def get_file_extension(file_path):
    return os.path.splitext(file_path)[1]

def get_file_name_without_extension(path):
    return os.path.basename(path).split('.')[0]

def get_file_extension(path):
    return os.path.splitext(path)[1]



def get_img_file(dir):
    imagelist = list()
    for parent, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            if filename.lower().endswith(
                    ('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
                imagelist.append(os.path.join(parent, filename))
        return imagelist



