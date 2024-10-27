# WhatsApp AnythingLLM

WhatsApp AnythingLLM is a Python-based application designed to integrate advanced language models into WhatsApp, enabling enhanced communication and automation capabilities. The application leverages tools to make LLMs accessible, manageable, and deployable within the WhatsApp messaging platform.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- Integrate language models with WhatsApp to automate conversations.
- Deploy and manage responses dynamically.
- Customizable settings and environment.
- Scalable using Docker.

## Prerequisites

- Python 3.7+
- Docker
- WhatsApp API Access (e.g., Twilio)
- Account in a platform providing LLM capabilities

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/fbeawels/whatsapp-anythingllm.git
   cd whatsapp-anythingllm

2. **Set up a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt

4. **Configure environment variables**
   Copy example.env to .env and fill in the required details.

5. **Build Docker Image (optional)**
   ```bash
   docker build -t whatsapp-anythingllm .

## Usage

1. **Run the application**
   ```bash
   python run.py

2. **Use Docker (if preferred)**
   ```bash
   docker run -d -p 5000:5000 whatsapp-anythingllm

3. **Interacting via WhatsApp**
    Set up your WhatsApp bot to point to the running service.
    Send messages to see LLM in action.



