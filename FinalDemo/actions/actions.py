# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
#
#
# This is a simple example for a custom action which utters "Hello World!"
#
# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

import os
import openai
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import SlotSet

# Initialize OpenAI API (Replace with your OpenAI API key)
openai.api_key = os.getenv("OPENAI_API_KEY")

class ActionGenerateGPTResponse(Action):

    def name(self) -> str:
        return "action_generate_gpt_response"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        # Extract the user's latest message
        user_message = tracker.latest_message.get('text')

        # Send the message to OpenAI GPT-3 or Hugging Face
        response = openai.Completion.create(
            engine="text-davinci-003",  # GPT-3 engine
            prompt=user_message,
            max_tokens=100,
            temperature=0.7,
        )

        # Extract the GPT-generated response
        bot_message = response.choices[0].text.strip()

        # Send the response back to the user
        dispatcher.utter_message(text=bot_message)

        return []

