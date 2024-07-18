# AI based Image Captioning System

## Description
This project implements an end-to-end image captioning system using Convolutional Neural Networks (CNNs) and Long Short-Term Memory networks (LSTMs) on the Flickr8K dataset. It leverages the DenseNet201 architecture for image feature extraction and integrates OpenAI's Language Model (LLM) for customized caption generation based on specified themes.

## Goal 
The goal of this project is to develop an advanced image captioning system that leverages state-of-the-art deep learning techniques, including Convolutional Neural Networks (CNNs) for image feature extraction and Long Short-Term Memory networks (LSTMs) for natural language generation. By integrating these technologies, the project aims to automate the process of describing images with accurate and contextually relevant captions. Additionally, the system incorporates OpenAI's Language Model (LLM) to enable customized caption generation based on specified themes such as Descriptive, SocialMedia, Humorous, Storytelling, Formal, Casual, and Minimalistic. The ultimate objective is to demonstrate proficiency in computer vision and natural language processing (NLP) by creating a robust, end-to-end solution for generating descriptive and engaging captions for a variety of images.

## Project Structure
  - caption_generator.py: Generates captions using a pre-trained model built in image-captioning.ipynb.
  - image-captioning.ipynb: Includes code for preprocessing captions and images, performing feature extraction with DenseNet201, and training the CNN-LSTM model for image caption generation. The final model is saved in the model directory.
  - llm_customizer.py: Utilized by caption_generator.py to customize captions using OpenAI's LLM based on user-specified themes.
  - main.py: Controls the application flow, invoking caption generation, customization, and image rendering.
  - render_image.py: Renders the final image with overlaid captions for user visualization.

## Features
  - Model Architecture: Integrates CNN and LSTM models to automate image description generation.
  - Feature Extraction: Utilizes DenseNet201 for extracting comprehensive image features.
  - Customization: Implements OpenAI's LLM to tailor captions based on predefined themes such as Descriptive, SocialMedia, Humorous, Storytelling, Formal, Casual, and Minimalistic.
  - Visualization: Renders images with captions overlaid, providing a visual representation of the generated descriptions.

## Requirements
  - Python 3.x
  - TensorFlow
  - OpenAI API Key (for LLM customization)
  - Additional dependencies as listed in requirements.txt

## Getting Started
  - Clone the repository:
    ```bash
    git clone <repository_url>
    cd image-captioning-project
    ```
  - Install dependencies
    ```bash
    python -m venv venv
    # for windows
    .\venv\Scripts\activate
    # for linux/mac
    source venv/bin/activate
    
    pip install -r requirements.txt
    ```
  - Configure OpenAI API Key :
      - Create an account on OpenAI and obtain an API key
      - Update the config.py file with your API key
   
  - Run the application:
```bash
python main.py <image_path> <theme>
```
  - Replace <image_path> with the path to your image.
  - Replace <theme> with one of the supported themes: Descriptive, SocialMedia, Humorous, Storytelling, Formal, Casual, Minimalistic.
