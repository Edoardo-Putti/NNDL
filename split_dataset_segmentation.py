from os import listdir, makedirs
from os.path import isfile, join, basename, splitext
from random import seed, shuffle

def split_dataset(training_dir, split_dir, training_percentage=0.90):
    """
    Starting from a training directory, creates a split directory
    with two text files, enumerating the images present in the 
    training and the validation set. 
    """

    seed(1234)

    file_names = [f for f in listdir(training_dir) if isfile(join(training_dir, f))]
    shuffle(file_names)

    split = int(len(file_names)*training_percentage)
    train_file_names = "\n".join([splitext(basename(f))[0] for f in file_names[:split]])
    valid_file_names = "\n".join([splitext(basename(f))[0] for f in file_names[split:]])

    makedirs(split_dir)
    with open(join(split_dir, './train.txt'), 'w') as train:
        train.write(train_file_names)
    with open(join(split_dir, './valid.txt'), 'w') as valid:
        valid.write(valid_file_names)



dataset_dir = 'D:/OneDrive - Politecnico di Milano/Corsi/2 Anno - 1 Sem/Artificial Neural Networks and Deep Learning/Homework/hw2/Development_Dataset/Training/Bipbip/Haricot/'
split_dataset(join(dataset_dir, 'Images'), join(dataset_dir, 'Splits'))