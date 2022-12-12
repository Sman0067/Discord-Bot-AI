import openai

def create_image(prompt):
    
    try:

        response = openai.Image.create(
            prompt = prompt,
            n=1,
            size="1024x1024"
        )

        image_url = response['data'][0]['url']

        return image_url

    except:
    
        return "That prompt is invalid. Try a different prompt."

def create_story(prompt):

    try: 
        
        response = openai.Completion.create(
            engine = "text-davinci-003", 
            prompt = f"Continue the story:\n\n{prompt}.", 
            max_tokens = 3500,
            temperature = 0.7
        )

        return response["choices"][0]["text"]

    except:

        return 'Something went wrong. Try a different prompt.'