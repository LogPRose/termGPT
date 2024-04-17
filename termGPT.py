import openai
from template.env import OPEN_API_KEY
# Set your API key
openai.api_key = OPEN_API_KEY

# Example prompt
prompt = "All of these requests are related to the programming language "

file_path = "logs/log"

file_type = input("Which file type would you like work with? (Python, C++, C, .txt, .md)")
mode_type = input("Would you like one contiguous output log or a new output log for each type?\n 1: Contiguous 2: New ").strip()




if file_type != ".txt":
    prompt += file_type.strip()
if input == "Python":
    file_path += ".py"
elif input == "C++":
    file_path += ".cpp"
elif input == "C":
    file_path += ".c"

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=50
)

if (mode_type == 1):
    with open('logs/log.txt', 'w') as file:
        while 1:

            user_input = input("Prompt: ")
        response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=50
                )
        generated_text = response.choices[0].text.strip()
        print(generated_text)
        file.write(generated_text)

else:
    while 1:
        with open('logs/log.txt', 'w') as file:

            user_input = input("Prompt: ")
            response = openai.Completion.create(
                    engine="text-davinci-002",
                    prompt=prompt,
                    max_tokens=50
                    )
            generated_text = response.choices[0].text.strip()
            print(generated_text)
            file.write(generated_text)
