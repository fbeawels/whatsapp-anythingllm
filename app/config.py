import sys
import os
from dotenv import load_dotenv
import logging

def load_configurations(app):
    load_dotenv()
    app.config["ACCESS_TOKEN"] = os.getenv("WAP_ACCESS_TOKEN")
    app.config["APP_ID"] = os.getenv("WAP_APP_ID")
    app.config["APP_SECRET"] = os.getenv("WAP_APP_SECRET")
    app.config["RECIPIENT_WAID"] = os.getenv("WAP_RECIPIENT_WAID")
    app.config["VERSION"] = os.getenv("WAP_VERSION")
    app.config["PHONE_NUMBER_ID"] = os.getenv("WAP_PHONE_NUMBER_ID")
    app.config["VERIFY_TOKEN"] = os.getenv("WAP_VERIFY_TOKEN")
    app.config["API_KEY"] = os.getenv("LLM_API_KEY")
    app.config["WORKSPACE_ID"] = os.getenv("LLM_WORKSPACE_ID")
    app.config["THREAD_ID"] = os.getenv("LLM_THREAD_ID")
    app.config["API_HOST"] = os.getenv("LLM_API_HOST")


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        stream=sys.stdout,
    )