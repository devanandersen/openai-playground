from auth import *

def gpt():
    prompt = "Translate the following English text to French: 'Hello, world!'"

    openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user", "content": "Where was it played?"}
        ]
    )

    # Print the response
    print(response.choices[0].text.strip())

set_openai_key()
gpt()
