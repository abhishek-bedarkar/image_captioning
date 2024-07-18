from caption_generator import generate_caption
from llm_customizer import customize_caption
from render_image import render_image_with_caption
import argparse

def main(image_path, theme):
    
    # Generate initial caption
    initial_caption = generate_caption(image_path)
    # print(f"Initial Caption: {initial_caption}")

    # Customize caption using OpenAI LLM 
    custom_caption = customize_caption(initial_caption, theme)
    # print(f"Customized Caption: {custom_caption}")

    # Render image with customized caption
    render_image_with_caption(image_path, custom_caption)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image Caption Generator")
    parser.add_argument('image_path', type=str, help='Path to the image file')
    parser.add_argument('theme', type=str, nargs='?', default='Format', choices=[
        'Descriptive', 'SocialMedia', 'Humorous', 'Storytelling', 'Formal', 'Casual', 'Minimalistic'],
        help='Theme for caption customization')
    
    args = parser.parse_args()
    
    main(args.image_path, args.theme)
