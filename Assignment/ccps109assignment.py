#   Program:    Photo Image Manipulator Program
#   Version:    1.0
#   Date:       April 18th, 2020
#
#   Author:     Sivatma Maharaj
#   Student #:  501043693
#
#   CCPS109 Assignment
#   (single developer)
#
#   Instructor: Nhan Tran
#   Course: CCPS109
#   Ryerson University, Toronto


from PIL import Image
import numpy as np
import os               # only used for file deletion and error checking, not used in image manipulation


def close():
        if image != None:
            image.close()

        print("\nRemoving temporary working files:")    
        try:
            os.remove("testimage.png")
            print("...removed 'testimage.png'")
        except OSError:
            pass
        try:
            os.remove("greyscale.png")
            print("...removed 'greyscale.png'")
        except OSError:
            pass
        try:
            os.remove("threshold.png")
            print("...removed 'threshold.png'")
        except OSError:
            pass
        try:
            os.remove("reflection.png")
            print("...removed 'reflection.png'")
        except OSError:
            pass
        print("\n\nThanks for using Photo Image Manipulator Program.")
        print("To use again type>python ccps109assignment.py")
        quit()

def load_image():
    image_filename = "testimage.jpg"
    try:
        Image.open(image_filename).save("testimage.png")
    except FileNotFoundError:
        print("\n'"+image_filename+"' not found.\n\nPlease ensure a valid jpg file is saved in current directory with the name '"+image_filename+"'.\n")
        quit()

    image = Image.open("testimage.png")
    image_array = np.array(image)
    width, height, = image.size
    print("\nImage ",image_filename," loaded!")
    print("\nHeight:",height,"Width: ",width,"Mode: ",image.mode)
    print("Array shape: ",image_array.shape,"\n")
    return (image, image_array)
    
def greyscale(image):
    image.convert(mode='L').save("greyscale.png")
    image = Image.open("greyscale.png")
    image_array = np.array(image)
    width, height, = image.size
    print("\nImage converted to greyscale!")
    print("\nHeight:",height,"Width: ",width,"Mode: ",image.mode)
    print("Array shape: ",image_array.shape,"\n")
    return (image, image_array)

def threshold(image_array, level):
    temp_list = []
    new_pixel = None
    for pixel in np.nditer(image):
        if pixel <= level:
            new_pixel = 0
        else:
            new_pixel = 255
        temp_list.append(new_pixel)
    image_array = np.array(temp_list)
    image_array = image_array.reshape(960,958)
    return image_array
     
def reflection(image_array, direction, percentage):
      height, width = image_array.shape
      
      if direction == 'H':
          reflection_row = int((height / 100) * percentage) 
          bottom_array = image_array[reflection_row+1:]
          reflect_array = image_array[reflection_row+1:reflection_row+1+reflection_row]
          image_array = np.concatenate((reflect_array[::-1], bottom_array))
      elif direction == 'V':
          reflection_column = int((width / 100) * percentage) 
          transpose_image_array = image_array.T
          right_array = transpose_image_array[reflection_column+1:]
          reflect_array = transpose_image_array[reflection_column+1:(reflection_column*2)+1]
          reflected_array = np.concatenate((reflect_array[::-1], right_array))
          image_array = reflected_array.T


      return image_array

def banner():
    return """
    #####################################################################
    #                                                                   #
    #                   Photo Image Manipulator Program                 #
    #                           Version 1.0                             #
    #                                                                   #
    #               Created by Sivatma Maharaj,501043693                #
    #                     Assignment for CCPS 109                       #
    #                      Instructor Nhan Tran                         #
    #                                                                   #
    #                 Ryerson University, Toronto, 2020                 #
    #                                                                   #
    # ###################################################################
                    
    """


def help():
    return """
      Photo Image Manipulator Program
      Version 1.0

      User Help File

      Command name: load
      Synopsis:     load
      Description:  loads the "testimage.jpg" file into the program.

      Command name: show
      Synopsis:     show
      Description:  Displays the current working image.

      Command name: array
      Synopsis:     array
      Description:  Displays a sample of the image as a numpy array.

      Command name: grey
      Synopsis:     grey
      Description:  Creates a greyscale version of the image.

      Command name: thresh
      Synopsis:     tresh THRESHOLD_VALUE
      Description:  Creates a black and white version of the image 
                    depending on THRESHOLD_VALUE.
      Option:       THRESHOLD_VALUE an integer between 0 and 255.
                    Any pixel less or equal than THRESHOLD_VALUE will be 
                    substituted with 0
                    Any pixel greater than THRESHOLD_VALUE will be 
                    substituted with 255

      Command name: reflect
      Synopsis:     reflect AXIS PERCENT
      Description:  Creates a reflection of the image along a 
                    horizontal or vertical axis.
      Option:       AXIS - either H for horizontal axis or 
                    V for vertical axis
                    PERCENT - between 0 and 50
    
      Command name: save
      Synopsis:     save TRANSFORMATION
      Description:  Saves a copy of the transformation as file.
      Option:       TRANSFORMATION - grey, thresh or reflect
      Examples:     "save grey" saves the greyscale image as "grey.jpg"
                    "save thresh" saves the threshold image as "threshold.jpg"
                    "save reflect" saves the reflected image as "reflection.jpg"

      Command name: quit
      Synopsis:     quit
      Description:  Deletes temporary files and exits the program.


    """

def save(transform):
    if transform == "thresh":
        try:
            threshImg = Image.open("threshold.png")
            rgbThreshImg = threshImg.convert('RGB')
            rgbThreshImg.save("threshold.jpg")
        except FileNotFoundError:
            return "\nThreshold image not generated. File not saved.\n\nPlease type 'help' for instructions.\n"
        return "\nThreshold image saved as 'threshold.jpg'\n"
    elif transform == "reflect":
        try:
            reflectImg = Image.open("reflection.png")
            rgbReflectImg = reflectImg.convert('RGB')
            rgbReflectImg.save("reflection.jpg")
        except FileNotFoundError:
            return "\nReflection image not generated. File not saved.\n\nPlease type 'help' for instructions.\n"
        return "\nReflection image saved as 'reflection.jpg'\n"
    elif transform == "grey":
        try:
            greyImg = Image.open("greyscale.png")
            rgbGreyImg = greyImg.convert('RGB')
            rgbGreyImg.save("greyscale.jpg")
        except FileNotFoundError:
            return "\nGreyscale image not generated. File not saved.\n\nPlease type 'help' for instructions.\n"
        return "\nGreyscale image saved as 'greyscale.jpg'\n"
    else:
        return "\nInvalid TRANSFORMATION type. Expected 'thresh', 'reflect' or 'grey'. File not saved.\n\nPlease type 'help' for instructions.\n"


image = None
image_array = None
print(banner())
while True:
    cmd = input("Enter command (Type 'help' for instructions): ")
    cmd_list = cmd.split()

    if cmd_list[0].lower() == "load":
        image, image_array = load_image()
    elif cmd_list[0].lower()== "show":
        if image == None:
            image, image_array = load_image()
        image.show()
    elif cmd_list[0].lower()== "grey" or cmd_list[0].lower()== "gray":      
        image, image_array = load_image()
        image, image_array = greyscale(image)
    elif cmd_list[0].lower()== "array":
        if image == None:
            image, image_array = load_image()
        print(image_array)
    elif cmd_list[0].lower()== "thresh":
        level = None
        try:
            level = int(cmd_list[1])
            if level < 0 or level > 255:
                raise ValueError("Integer out of range.")
        except ValueError:
            print("\nInvalid THRESHOLD_VALUE. Expected an integer value between 0 and 255.\n\nPlease type 'help' for instructions.\n")
            continue  
        except IndexError:
            print("\nInvalid THRESHOLD_VALUE. Expected an integer value between 0 and 255.\n\nPlease type 'help' for instructions.\n")
            continue    
        image, image_array = load_image()
        image, image_array = greyscale(image)
        image_array = threshold(image_array, level)
        image = Image.fromarray(image_array)
        image.save("threshold.png")

    elif cmd_list[0].lower()== "reflect":
        try:
            direction = cmd_list[1].upper()
            if direction.strip().upper() != 'H' and direction.strip().upper() != 'V':
                raise ValueError("Unexpect AXIS of reflection.")
        except IndexError:
            print("\nInvalid AXIS of reflection. Expected 'H' or 'V'. \n\nPlease type 'help' for instructions.\n")
            continue
        except ValueError:
            print("\nInvalid AXIS of reflection. Expected 'H' or 'V'. \n\nPlease type 'help' for instructions.\n")
            continue

        try:
            percentage = int(cmd_list[2])
            if percentage < 0 or percentage > 50:
                raise ValueError("Invalid reflection limit")
        except IndexError:
            print("\nInvalid reflection limit. Expected an integer value between 0 and 50'. \n\nPlease type 'help' for instructions.\n")
            continue
        except ValueError:
            print("\nInvalid reflection limit. Expected an integer value between 0 and 50'. \n\nPlease type 'help' for instructions.\n")
            continue

        image, image_array = load_image()
        image, image_array = greyscale(image)
        image_array = reflection(image_array, direction, percentage)
        image = Image.fromarray(image_array)
        image.save("reflection.png")

    elif cmd_list[0].lower()== "save":
        try:
            transform = cmd_list[1].lower()
        except IndexError:
            print("\nInvalid TRANSFORMATION type. Expected 'thresh', 'reflect' or 'grey'. File not saved.\n\nPlease type 'help' for instructions.\n")
            continue
        print(save(transform))
    elif cmd_list[0].lower()== "quit":
        close()
    elif cmd_list[0].lower()== "help":
        print(help())
    else:
        print("\nInvalid input. Please type 'help' for instructions.\n")
 