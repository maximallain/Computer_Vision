import os
import DL_model.data.constants as cst
import cv2
import numpy as np
from PIL import Image

path = '../data/dataset-resized/'
waste_list = ['glass', 'paper', 'cardboard', 'plastic', 'metal', 'trash']

def write_list_path(data_path = path, written_path = './lst/list_path.lst') :
    """
    Functions which write the data's path from data_path's directory in the written_path's file
    """
    with open(written_path, 'w') as file :
    # for e in os.listdir('./dataset-resized/') :
    #     file.write(e)
        for e in os.listdir(data_path):
            try :
                for f in os.listdir(data_path+e) :
                    file.write(data_path+e+"/"+f+"\n")
            except NotADirectoryError :
                pass

def get_data_number(arg_train, arg_val):
    res = []
    res.append((int(arg_train * cst.NB_GLASS), int(arg_val * cst.NB_GLASS)))
    res.append((int(arg_train * cst.NB_PAPER), int(arg_val * cst.NB_PAPER)))
    res.append((int(arg_train * cst.NB_CARDBOARD), int(arg_val * cst.NB_CARDBOARD)))
    res.append((int(arg_train * cst.NB_PLASTIC), int(arg_val * cst.NB_PLASTIC)))
    res.append((int(arg_train * cst.NB_METAL), int(arg_val * cst.NB_METAL)))
    res.append((int(arg_train * cst.NB_TRASH), int(arg_val * cst.NB_TRASH)))
    return res

def write_list_path_divided(arg_train, arg_val, arg_test) :
    """
    Functions which takes an arg (float between 0 and 1) and which divides the data-set :
    size of train's data : len(data-set) * arg
    size of test's data : len(data-set) * (1-arg)
    """
    written_path_train = '../data/lst/list_path_train.lst'
    written_path_val = '../data/lst/list_path_val.lst'
    written_path_test = '../data/lst/list_path_test.lst'
    if (arg_train+arg_val+arg_test) != 1 :
        raise ValueError
    nb = get_data_number(arg_train, arg_val)
    with open(written_path_train, 'w') as train_file :
        with open(written_path_val, 'w') as val_file :
            with open(written_path_test, 'w') as test_file :
                waste_indice = 0
                for waste in waste_list :
                    i = 0
                    borne = nb[waste_indice]
                    for f in os.listdir(path+waste) :
                        if i < borne[0] :
                            train_file.write(path + waste + "/" + f + "\n")
                        elif i < borne[0]+borne[1]:
                            val_file.write(path + waste + "/" + f + "\n")
                        else :
                            test_file.write(path + waste + "/" + f + "\n")

                        i += 1



def get_labels():
    """
    :param path: file of images' path
    Function which create a file with the labels of the path
    """
    for name in ['train', 'val', 'test']:
        file_path = '../data/lst/list_path_'+name+'.lst'
        written_path = '../data/lst/'+name+'_label.lst'

        with open(written_path, 'w') as res :
            with open(file_path, 'r') as list :
                ligns = list.readlines()
            for l in ligns :
                if 'glass' in l :
                    res.writelines(str(cst.GLASS)+"\n")
                if "paper" in l :
                    res.writelines(str(cst.PAPER)+"\n")
                if 'cardboard' in l :
                    res.writelines(str(cst.CARDBOARD)+"\n")
                if 'metal' in l:
                    res.writelines(str(cst.METAL) + "\n")
                if 'plastic' in l:
                    res.writelines(str(cst.PLASTIC) + "\n")
                if 'trash' in l:
                    res.writelines(str(cst.TRASH) + "\n")

def get_vector_labels():
    """"""
    for name in ['train', 'val', 'test']:
        file_path = '../data/lst/'+name+'_label.lst'
        written_path = '../data/lst/'+name+'_label.lab'
        with open(written_path, 'w') as res :
            with open(file_path, 'r') as list :
                ligns = list.readlines()
            for l in ligns :
                temp = [0,0,0,0,0,0]
                temp[int(l)] = 1
                str_res = ""
                for i in range(0,6):
                    str_res = str_res + str(temp[i]) + " "
                res.write(str_res + "\n")

def get_npy_labels():
    for name in ['train', 'val', 'test']:
        vector_path = '../data/lst/'+name+'_label.lab'
        written_path = '../data/numpy/'+name+'_label.npy'
        lab_train = np.loadtxt(vector_path, int)
        np.save(written_path, lab_train)



def obtainFilePath(path_images_filename = "./list_path.lst"):
    # read list of images
    with open(path_images_filename, 'r') as path_images_file:
        path_images = [x.strip() for x in path_images_file.readlines()]
    return path_images


def meanRGB() :
    print("MeanRGB")
    path_images = obtainFilePath()
    r = 0
    g = 0
    b = 0
    j = 0
    for l in range(len(path_images)):
        imname = path_images[l]
        image_temp = cv2.imread(imname)
        i = 0
        b_temp = 0
        g_temp = 0
        r_temp = 0
        for e in image_temp :

            for e_e in e :
                b_temp += e_e[0]
                g_temp += e_e[1]
                r_temp += e_e[2]
                i += 1
        b += b_temp/i
        g += g_temp/i
        r += r_temp/i
        j += 1
    return (r/j,g/j,r/j)


def writeInNumpyFile():
    for e in ['train', 'val', 'test'] :
        path_images_filename = "../data/lst/list_path_"+e+".lst"
        npy_file = '../data/numpy/'+e+'_images.npy'

        path_images = obtainFilePath(path_images_filename=path_images_filename)
        # loaded_img_train = images
        images = np.zeros((len(path_images), 227, 227, 3))

        mean_R = int(171.6348940959126)
        mean_G = int(163.14820336282835)
        mean_B = int(171.6348940959126)

        for l in range(len(path_images)):
            imname = path_images[l]
            image = Image.open(imname)
            image = image.resize((227, 227), Image.ANTIALIAS)
            image = np.array(image)
            if len(image.shape) != 3:  # gray-image
                final_image = np.zeros((227, 227, 3))
                for c in range(3):  # gray to RGB
                    final_image[:, :, c] = image
            else:
                final_image = image


            # Normalization
            final_image[:, :, 0] -= mean_R
            final_image[:, :, 1] -= mean_G
            final_image[:, :, 2] -= mean_B
            images[l, :, :, :] = final_image
        print(images.shape)
        # save images in numpy file
        np.save(npy_file, images)

def defined_data_set(arg_train, arg_val, arg_test):
    write_list_path_divided(arg_train=arg_train, arg_val=arg_val, arg_test=arg_test)
    writeInNumpyFile()
    get_labels()
    get_vector_labels()
    get_npy_labels()

#write_list_path_divided(0.6, 0.1, 0.3)
defined_data_set(0.6, 0.1, 0.3)