import openai
from api_secrets import API_KEY

openai.api_key = API_KEY


def create_image_on_prompt(prompt_sentence):

    print(prompt_sentence)
    try:
        response = openai.Image.create(
            prompt=prompt_sentence,
            n=1,
            size="512x512"
        )

        image_url = response['data'][0]['url']
        return image_url

    except openai.error.OpenAIError as e:

        print(e.http_status)
        print(e.error)


# output = create_image_on_prompt(
#     "princess diana as a disney princess realistic")

output = create_image_on_prompt(
    "jawaharlal nehru as a british victorian aristocrat realistic")
print(output)
