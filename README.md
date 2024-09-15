# OpenAI Chatbot

A simple chatbot that uses the OpenAI GPT-4o model to generate responses to user input. I created this project to learn
how to use the OpenAI API and experiment with different chatbot configurations.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory of the project and add your OpenAI API key:
    ```sh
    echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
    ```

### Usage

1. Run the main script:
    ```sh
    python src/main.py
    ```

### Environment Variables

The following environment variables are required:

- `OPENAI_API_KEY`: Your OpenAI API key.

Example `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here