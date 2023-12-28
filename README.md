# Diagnosing the need for epichoectomy surgery through OPG images with deep learning

In this project, using deep learning techniques, we tried to detect the need for Apicoectomy surgery through dental Orthopantomography images.
We have used U-NET.
Also for feature extraction from DenseNet169 Used.

# Description

When the soft inner pulp of your tooth becomes infected, there is only one way to treat the problem and save the tooth
There is your natural and that is to remove the pulp from the tooth.

Dentists can usually fix this problem and restore the tooth with the help of non-surgical (non-invasive) methods or root canal treatment, but sometimes there is no other option than dental surgery.

When the treatment is done, the pulp is pulled out through the outer crown of your tooth.

When direct access to the pulp and root of the tooth is needed, an incision is made on the gum.

This method helps the dentists to clean the pulp and infection through the root of the tooth and to remove the infected tissues of the bone under the gums.

# Apicoectomy

An apicoectomy (also referred to as apicectomy, root end resection or periapical surgery) is a minor dental procedure that is performed to save a tooth that would otherwise need to be removed. An apicoectomy involves removing the end of the root of a tooth (known as the apex) and is performed on both children and adults.


![Apicectomy](https://github.com/MojtabaZarreh/Diagnosing-the-need-for-epichoectomy-surgery-through-OPG-images-with-deep-learning/assets/71370569/852b4d89-f958-4590-b5b3-44ebaeecbd31)


We are trying to diagnose the need for this surgery in OPG modality.


![Apicoectomy-and-retrofill](https://github.com/MojtabaZarreh/Diagnosing-the-need-for-epichoectomy-surgery-through-OPG-images-with-deep-learning/assets/71370569/05018d21-59be-4845-b0a9-661c1ec37a43)



# Dataset

The dataset contains a limited number of whole-mouth OPG images labeled by experienced dentists.

It also contains images of masks for problematic teeth.

The image format is DICOM.

https://www.kaggle.com/datasets/iaaaevent/iaaa-v2

![1 2 246 512 1 2 0 4 882960520908 1749715128 20230104093912](https://github.com/MojtabaZarreh/Diagnosing-the-need-for-epichoectomy-surgery-through-OPG-images-with-deep-learning/assets/71370569/1056f447-fa50-4197-b42f-7eb16991b454)


# Preprocessing

Crop around and resize images
![bandicam 2023-12-28 13-33-49-478](https://github.com/MojtabaZarreh/Diagnosing-the-need-for-epichoectomy-surgery-through-OPG-images-with-deep-learning/assets/71370569/874e4e53-8b3d-458d-8453-c8e8bc9e426e)

Apply filters to images
![image](https://github.com/MojtabaZarreh/Diagnosing-the-need-for-epichoectomy-surgery-through-OPG-images-with-deep-learning/assets/71370569/773531c0-e412-4e5d-8210-edc824eab02e)







# Model

As mentioned above, we have used the U-NET architecture.


![10462_2022_10152_Fig3_HTML](https://github.com/MojtabaZarreh/Diagnosing-the-need-for-epichoectomy-surgery-through-OPG-images-with-deep-learning/assets/71370569/8185501e-713c-4d5a-83ce-4d0d68687126)


And DenseNet169 has been used for feature extraction.


![The-architecture-of-DenseNet-169-used-to-implement-the-proposed-method](https://github.com/MojtabaZarreh/Diagnosing-the-need-for-epichoectomy-surgery-through-OPG-images-with-deep-learning/assets/71370569/8b465802-0f15-4154-884f-ee45c01ae846)

The final architecture of the model :

![Picture1](https://github.com/MojtabaZarreh/Diagnosing-the-need-for-epichoectomy-surgery-through-OPG-images-with-deep-learning/assets/71370569/02629176-86cd-45a2-9898-dbd5a655e84d)





