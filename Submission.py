import argparse
import os
import cv2
import numpy as np
import pandas as pd
import pydicom
import tensorflow as tf

def preprocess_dicom_image(image_path):
    dicom_data = pydicom.read_file(image_path)
    image = dicom_data.pixel_array.astype('uint16')
    image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)
    image = image.astype('uint8')
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    factor = 1
    image_output = cv2.convertScaleAbs(image, alpha=factor)
    gray = cv2.cvtColor(np.array(image_output), cv2.COLOR_RGB2GRAY)
    kernel = np.array([
        [-1,-1,-1,-1,-1],
        [-1, 1, 1, 1,-1],
        [-1, 1, 9.5, 1,-1],
        [-1, 1, 1, 1,-1],
        [-1,-1,-1,-1,-1]]) / 4.0
    filtered = cv2.filter2D(gray, -1, kernel)
    gaussian_img = cv2.GaussianBlur(filtered, (0, 0), 1.5)
    imS = cv2.resize(gaussian_img, (1000, 500))
    crop = imS[120:400, 200:800]
    image = cv2.resize(crop, (512, 256))
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    return image

def predict(images_path, csv_path):
    model_filepath = os.path.join(os.path.dirname(__file__),'U_NET2.h5')
    loaded_model = tf.keras.models.load_model(
        model_filepath,
        custom_objects=None,
        compile=False
    )
    loaded_model.summary()

    dicom_list = os.listdir(images_path)
    labels = {"SOPInstanceUID": [], "Label": []}

    for dcm in dicom_list:
        if "dcm" == dcm.split(".")[-1]:
            image_path = os.path.join(images_path, dcm)
            dicom_image = preprocess_dicom_image(image_path)
            
            prediction = loaded_model.predict(dicom_image[tf.newaxis, ...])
            mask_value = np.mean(prediction)
            rounded_mask_value = round(mask_value, 7) 
            mask_value = 1 if rounded_mask_value > 0.0140000 else 0

            labels["SOPInstanceUID"].append(dcm[:-4])
            labels["Label"].append(mask_value)

    df = pd.DataFrame(labels)
    df.to_csv(csv_path, index=False)
    print(f"Results saved to: {csv_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", help="path to folder containing test images")
    parser.add_argument("--output", help="path to final CSV output")
    args = parser.parse_args()
    predict(args.inputs, args.output)
