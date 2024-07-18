import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
from image_captioning import predict_caption, tokenizer, max_length, features
from config import MODEL_PATH

# Load the pre-trained model
caption_model = load_model(MODEL_PATH)

def generate_caption(image_path):
    # Load and preprocess the image
    def load_image(img_path):
        img = load_img(img_path, target_size=(224, 224))
        img = img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = img / 255.0
        return img

    # Extract image features
    img = load_image(image_path)
    image_features = features[os.path.basename(image_path)]

    # Generate caption using the model
    caption = predict_caption(caption_model, os.path.basename(image_path), tokenizer, max_length, features)
    
    # Remove start and end tokens
    caption = caption.replace('startseq', '').replace('endseq', '').strip()
    
    return caption
