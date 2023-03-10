from __future__ import annotations
import openai


openai.api_key = 'YOUR API KEY from https://platform.openai.com/account/api-keys'


def bot_response(prompt: str) -> str | None:
    text: str | None = None

    try:
        response: dict = openai.Completion.create(
            model='text-davinci-003',
            prompt=prompt,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[' You:', ' Bot:']
        )

        choices: dict = response.get('choices')[0]
        text = choices.get('text')

    except Exception as e:
        print('ERROR:', e)

    return text


def update_list(message: str, prompt_list: list[str]):
    prompt_list.append(message)


def create_prompt(message: str, prompt_list: list[str]) -> str:
    p_message: str = f'\nYou: {message}'
    update_list(p_message, prompt_list)
    prompt: str = ''.join(prompt_list)
    return prompt


def get_bot_response(message: str, prompt_list: list[str]) -> str:
    prompt: str = create_prompt(message, prompt_list)
    bot_response: str = bot_response(prompt)

    if bot_response:
        update_list(bot_response, prompt_list)
        pos: int = bot_response.find('\nBot: ')
        bot_response = bot_response[pos + 5:]
    else:
        bot_response = 'Something went wrong...'

    return bot_response


def main():
    prompt_list: list[str] = ['You will pretend as a representative of marketplace company named Sadiq',
                              '\nYou: What is your website?',
                              '\nBot: It is www.sadiq.ai', 
                              '\nYou: Who is the CEO of your company?'
                              '\nBot: It is Fahad Khalid',]
    loop= True
    while loop:
        user_input: str = input('You: ')
        if user_input == 'exit':
            loop= False
        else:
            response: str = get_bot_response(user_input, prompt_list)
            print(f'Bot: {response}')


if __name__ == '__main__':

    main()