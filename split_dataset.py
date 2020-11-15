import json
import os
import shutil

def split_dataset(training_path, classes_path, root_training_path):
    # training_path -> "./MaskDataset/training"
    # classes_path -> "./MaskDataset/train_gt.json"
    # root_training_path -> new folder to be used with 'flow_from_directory'

    with open(classes_path) as classes_json:
        classes = json.load(classes_json)
    
    class0 = [os.path.join(training_path, image_path) for (image_path, image_class) in classes.items() if image_class == 0]
    class1 = [os.path.join(training_path, image_path) for (image_path, image_class) in classes.items() if image_class == 1]
    class2 = [os.path.join(training_path, image_path) for (image_path, image_class) in classes.items() if image_class == 2]

    os.makedirs(root_training_path)
    class0_path = os.path.join(root_training_path, "class_0")
    class1_path = os.path.join(root_training_path, "class_1")
    class2_path = os.path.join(root_training_path, "class_2")
    os.makedirs(class0_path)
    os.makedirs(class1_path)
    os.makedirs(class2_path)

    for class0_image in class0:
        shutil.copy2(class0_image, class0_path)
    for class1_image in class1:
        shutil.copy2(class1_image, class1_path)
    for class2_image in class2:
        shutil.copy2(class2_image, class2_path)
