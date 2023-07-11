from auth import *

def execute():
    prompt = "Translate the following English text to French: 'Hello, world!'"

    # Get a response from the API
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=60
    )

    # Print the response
    print(response.choices[0].text.strip())

set_openai_key()
execute()
