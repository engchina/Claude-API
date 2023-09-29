import asyncio
import json
import os
from claude_api import Client


def get_cookie():
    # cookie = os.environ.get('cookie')
    cookie = "sessionKey=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"
    if not cookie:
        raise ValueError("Please set the 'cookie' environment variable.")
    return cookie


def main():
    cookie = get_cookie()
    claude = Client(cookie)
    conversation_id = None

    print("Welcome to Claude AI Chat!")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Thank you!")
            break

        if not conversation_id:
            conversation = claude.create_new_chat()
            conversation_id = conversation['uuid']

        response = claude.send_message(user_input, conversation_id)
        print(response)


async def main_stream():
    cookie = get_cookie()
    claude = Client(cookie)
    conversation_id = None

    print("Welcome to Claude AI Chat!")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Thank you!")
            break

        if not conversation_id:
            conversation = claude.create_new_chat()
            conversation_id = conversation['uuid']
            print("Chatbot:", end='')
            async for response in claude.send_message_stream(user_input, conversation_id):
                print(response["completion"], end='')
            print()


if __name__ == "__main__":
    # main()
    asyncio.run(main_stream())
