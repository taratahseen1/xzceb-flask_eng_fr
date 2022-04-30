"""
This file contains code to translate English to French and French to English.
"""

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def create_translator_instance():
    """This function initialises and returns a language
    translator instance."""
    
    authenticator = IAMAuthenticator(f'{apikey}')
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )

    language_translator.set_service_url(f'{url}')
    
    return language_translator

def english_to_french(english_text):
    """This function translates English to French."""

    # Check input is not None
    if not english_text:
        return None

    # Initialise language_translator
    language_translator = create_translator_instance()

    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()

    french_text = translation['translations'][0]['translation']

    return french_text

def french_to_english(french_text):
    """This function translates French to English"""

    # Check input is not None
    if not french_text:
        return None

    # Initialise language_translator
    language_translator = create_translator_instance()

    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()

    english_text = translation['translations'][0]['translation']

    return english_text