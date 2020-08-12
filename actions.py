# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import mysql.connector
import traceback

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query = "select text from test_table where id = 1"

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="123456789",
                database="rasa"
            )

            cursor = mydb.cursor()
            cursor.execute(query)

            results = cursor.fetchall()
            print(results)
        except:
            print("Error occured while connecting to database or fetching data from database. Error Trace: {}".format(traceback.format_exc()))

        dispatcher.utter_message(text="Hello World!",json_message=results)

        return []
