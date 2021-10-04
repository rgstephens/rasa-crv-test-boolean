# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import random
import logging
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

logger = logging.getLogger(__name__)

class ActionSetBoolean(Action):

    def name(self) -> Text:
        return "action_set_boolean"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        test_boolean = bool(random.getrandbits(1))
        logger.error(f"test_boolean = {test_boolean}")

        return [SlotSet('agent_queue_open', test_boolean)]
