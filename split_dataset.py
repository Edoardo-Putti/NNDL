import json
import os
import shutil
import random

def split_dataset(training_path, classes_path, root_training_path, root_validation_path, training_percentage=0.90):
    """
    Split a dataset into training + validation.

    training_path: path to the full dataset

    classes_path: path to the json associating file names to classes

    root_training_path: path to the splitted training set

    root_validation_path: path to the splitted validation set

    training_percentage: value indicating the percentage of samples to use for training

    """

    # Fix a seed for reproducibility purposes
    random.seed(1234)

    with open(classes_path) as classes_json:
        classes = json.load(classes_json)
    
    # Load images' path and shuffle them
    class0 = [os.path.join(training_path, image_path) for (image_path, image_class) in classes.items() if image_class == 0]
    class1 = [os.path.join(training_path, image_path) for (image_path, image_class) in classes.items() if image_class == 1]
    class2 = [os.path.join(training_path, image_path) for (image_path, image_class) in classes.items() if image_class == 2]
    random.shuffle(class0)
    random.shuffle(class1)
    random.shuffle(class2)

    # Create training dir
    os.makedirs(root_training_path)
    class0_training_path = os.path.join(root_training_path, "class_0")
    class1_training_path = os.path.join(root_training_path, "class_1")
    class2_training_path = os.path.join(root_training_path, "class_2")
    os.makedirs(class0_training_path)
    os.makedirs(class1_training_path)
    os.makedirs(class2_training_path)

    # Create validation dir
    os.makedirs(root_validation_path)
    class0_validation_path = os.path.join(root_validation_path, "class_0")
    class1_validation_path = os.path.join(root_validation_path, "class_1")
    class2_validation_path = os.path.join(root_validation_path, "class_2")
    os.makedirs(class0_validation_path)
    os.makedirs(class1_validation_path)
    os.makedirs(class2_validation_path)
    
    # Copy the files into training/validation dirs according to training_percentage
    class0_split = int(len(class0)*training_percentage)
    for class0_image in class0[0:class0_split]:
        shutil.copy2(class0_image, class0_training_path)
    for class0_image in class0[class0_split:]:
        shutil.copy2(class0_image, class0_validation_path)

    class1_split = int(len(class1)*training_percentage)
    for class1_image in class1[0:class1_split]:
        shutil.copy2(class1_image, class1_training_path)
    for class1_image in class1[class1_split:]:
        shutil.copy2(class1_image, class1_validation_path)

    class2_split = int(len(class2)*training_percentage)
    for class2_image in class2[0:class2_split]:
        shutil.copy2(class2_image, class2_training_path)
    for class2_image in class2[class2_split:]:
        shutil.copy2(class2_image, class2_validation_path)
