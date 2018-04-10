import cv2
import numpy as np
from PIL import Image






#def main():


    # =====================================
    # path_images_filename = "test_path.lst"
    #
    # # read list of images
    # with open(path_images_filename, 'r') as path_images_file:
    #     path_images = [x.strip() for x in path_images_file.readlines()]
    #
    # images = np.zeros((5532, 227, 227, 3))
    # mean_R = int(121.613038961)
    # mean_G = int(116.624289758)
    # mean_B = int(102.788134198)
    # for l in range(len(path_images)):
    #     print(l)
    #     # print(path_images[l])
    #     imname = path_images[l]
    #     image = Image.open(imname)
    #     image = image.resize((227, 227), Image.ANTIALIAS)
    #     image = np.array(image)
    #     if len(image.shape) != 3:  # gray-image
    #         final_image = np.zeros((227, 227, 3))
    #         for c in range(3):  # gray to RGB
    #             final_image[:, :, c] = image
    #     else:
    #         final_image = image
    #     # print(final_image.shape)
    #     final_image[:, :, 0] -= mean_R
    #     final_image[:, :, 1] -= mean_G
    #     final_image[:, :, 2] -= mean_B
    #     images[l, :, :, :] = final_image
    # print(images.shape)
    # # save images in numpy file
    # np.save('test_images.npy', images)


# if __name__ == '__main__':
#     main()




#writeInNumpyFile()