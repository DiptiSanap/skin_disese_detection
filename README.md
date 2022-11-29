# skin_disese_detection

**Aim & Objective of project:

	Dermatological disorders are one of the most widespread diseases in the world. Despite being common its diagnosis is extremely difficult because of its complexities of skin tone, colour, presence of hair.
Our objective behind this project was,  to use various deep learning based techniques (Convolutional Neural networks) to automatically predict the various kinds of skin diseases. 
The aim was to develop an application that will help both dermatologist and users to easily predict the skin lesion by just uploading an image of infected area. 


**About Dataset

HAM10000 ("Human Against Machine with 10000 training images") dataset
Source: Harvard Dataverse

Among the whole dataset we choose 3 classes with maximum number of samples for our experiment. They are listed below:
•	Melanocytic nevi(nv)
•	Melanoma(mel)
•	Benign keratosis-like lesions(bkl)


**Preprocessing Steps:

![image](https://user-images.githubusercontent.com/107847530/204492137-9379ff40-e90d-49fb-a821-169c188cf93d.png)

As we observed in the above graph, it is clear that the dataset is imbalanced. It is more biased towards the class Melanocytic nevi(nv). For balancing the dataset,we decided to do sampling for balance the dataset.
We take 1500 samples of each class and divided them into (1250+250) for the train set and test set respectively. Total size of train set is 3750 and that of test set is 750 resp.
We resize the images to the size (224×224) where original size was (600×450).
The data augmentation was applied to the training dataset by 30° rotation, and horizontal and vertical image flipping to increase the number of datasets.


**Architectures Used:
1. ResNet50
2. MobileNetV2
3. efficientNetB0

Conclusion:

   ![image](https://user-images.githubusercontent.com/107847530/204493238-965ba925-0a61-4612-b457-e03d376172a3.png)


After experimenting with these 3 architectures, it is concluded that 
a.	ResNet50 suffered from underfitting 
b.	MobileNet suffered from overfitting.
c.	EfficientnetB0 gave the highest accuracy and good fit.
d.	EfficientNetB0 is considered as the best model for the used dataset.

**Application and future scope:

A webpage is developed as an application of this project, using which a user can easily detect the type of disease by uploading an image. The webpage also displays some information about each disease such as symptoms, causes, preventions, and treatments.
![image](https://user-images.githubusercontent.com/107847530/204494972-204b1e06-4940-4381-8d68-eca3d154ce1d.png)
![image](https://user-images.githubusercontent.com/107847530/204495243-d4fa0821-7ae3-4299-84d7-ca308cc2c72c.png)



