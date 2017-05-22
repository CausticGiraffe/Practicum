# Practicum
MSDS Practicum Project 

In this competition we have a multi-class classification problem with three classes. We are asked, given an image, to identify the cervix type.

From the data description:
In this competition, you will develop algorithms to correctly classify cervix types based on cervical images. These different types of cervix in our data set are all considered normal (not cancerous), but since the transformation zones aren't always visible, some of the patients require further testing while some don't. This decision is very important for the healthcare provider and critical for the patient. Identifying the transformation zones is not an easy task for the healthcare providers, therefore, an algorithm-aided decision will significantly improve the quality and efficiency of cervical cancer screening for these patients.

The submission format is asking for a probability for each of the three different cervix types.

Data sets: Train, Test, and Additional Images
Additional Images contains photos from the same patient appointment and vary in levels of quality, different angles and filters, etc.

All images have a fixed white balance (android camera api) and a fixed cross polarized light source.
All images have configurable working distance (225-450mm), manual focus, digital zoom (X1-X4), and file size. 

In some images a green filter is applied to highlight blood vessals which will then appear black.
In some images acidic acid has been applied, which paints abnormal celss white. Lugol's Iodine will cause abnormal cells to appear white and normal cells to appear dacker. 

Steps:
0. Explore Intel SDK Tools 
1. Explore data and create dataframe for images
2. Figure out how many images there are for each cervix type and which file types they have
3. How many different shapes of images by class are there (some images also have oval frames)
4. Explore possiblity of reducing image size by RBG and greyscale
5. Segment images
6. Start CNN (Ensemble vs single model https://arxiv.org/abs/1704.00109) 

Possible Models:
VGGNet, 
AlexNet(smaller), 
GoogleNet, 
ResNet, 
ImageNet - Natural images

Resource: Stanford CS 231n Convolutional Neural Networks for Visual Recognition http://cs231n.github.io/ 
