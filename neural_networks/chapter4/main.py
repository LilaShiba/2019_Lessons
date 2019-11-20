import pandas as pd
from matplotlib import pyplot as plt
import os, random

def preview_images(animal):
    path = '../../../../kaggle_data/cats_dogs/PetImages/'+animal+'/'
    print('loading data')
    _,_,animal_images = next(os.walk(path))
    # prepare images
    fig, ax = plt.subplots(3,3,figsize=(20,10))
    # randomly plot
    for idx, img in enumerate(random.sample(animal_images, 9)):
        img_read = plt.imread(path+img)
        ax[int(idx/3), idx%3].imshow(img_read)
        ax[int(idx/3), idx%3].axis('off')
        ax[int(idx/3), idx%3].set_title(animal+'/'+img)
    plt.show()

preview_images('Dog')