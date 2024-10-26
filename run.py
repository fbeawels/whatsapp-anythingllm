import logging
from libs.config import get_config
from app import create_app

config = get_config("conf/app.props")

app = create_app()

if __name__ == "__main__":
    logging.info("Microservice WhatsApp / AnythingLLM started")
    app.run(host=config['SERVER']['server'], port=int(config['SERVER']['port']))
