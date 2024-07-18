import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from textwrap import wrap

def render_image_with_caption(image_path, caption):
    img = load_img(image_path, target_size=(224, 224))
    img = img_to_array(img) / 255.0

    plt.figure(figsize=(8, 8))
    plt.imshow(img)
    plt.title("\n".join(wrap(caption, 20)))
    plt.axis('off')
    plt.show()
