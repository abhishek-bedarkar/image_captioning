import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def customize_caption(initial_caption, theme):
    prompt = f"Here is an image caption: '{initial_caption}'. Customize this caption based on the following theme: '{theme}'"
    response = openai.Completion.create(
        engine="text-davinci-004",
        prompt=prompt,
        max_tokens=50
    )
    customized_caption = response.choices[0].text.strip()
    return customized_caption
