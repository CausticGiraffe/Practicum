# Practicum
MSDS Practicum Project 

In this competition we have a multi-class classification problem with three classes. We are asked, given an image, to identify the cervix type.

From the data description:
In this competition, you will develop algorithms to correctly classify cervix types based on cervical images. These different types of cervix in our data set are all considered normal (not cancerous), but since the transformation zones aren't always visible, some of the patients require further testing while some don't. This decision is very important for the healthcare provider and critical for the patient. Identifying the transformation zones is not an easy task for the healthcare providers, therefore, an algorithm-aided decision will significantly improve the quality and efficiency of cervical cancer screening for these patients.

Data sets: 
File descriptions – Images were collected over the last three years from 21 countries, mostly in East Africa and Mexico
train.7z - the training set. The images are organized in their labeled categories: Type_1, Type_2, and Type_3.
test.7z - the first stage test set. All the images are in this same folder.
additional_Type_{x}.7z - images from duplicated patients organized in their labeled categories: Type_1, Type_2, and Type_3.  These images have different lighting, filters, angles, and quality. 
solution_stg1_release.csv - stage 1 test data labels release. Updated June 15,2017.
test_stg2.7z - the 2nd stage test set. Updated June 15,2017.
update 3 labels:
train/Type_1/80 - type 3
train/Type_3/968 - type 1
train/Type_3/1120 - type 1

All images have a fixed white balance (android camera api) and a fixed cross polarized light source.
All images have configurable working distance (225-450mm), manual focus, digital zoom (X1-X4), and file size. 

In some images a green filter is applied to highlight blood vessals which will then appear black.
In some images acidic acid has been applied, which paints abnormal celss white. Lugol's Iodine will cause abnormal cells to appear white and normal cells to appear dacker. 

# Cervix anatomy 
Two important areas of the cervix:
Squamo-columnar junction (SCJ) where two different types of epithelial cells meet
Transformation zone (TZ) which is the area between the original SCJ and the new SCJ

Why is the cervix type important?
Cervical cancers begin in the transformation zone
Cervix types 2 and 3 may contain hidden lesions that require different treatments


