DataGPT: A Text Generation Toolkit
This repository provides the source code for DataGPT, a toolkit for generating SQL from natural language text.

## Getting Started
1. Download the Source Code
  Clone the repository using Git:
    git clone https://github.com/Asifig1133/DataGPT.git
    
2. Environment Setup

The default database uses SQLite, so no additional database installation is required in the default mode. However, if you want to use other databases, we recommend creating a Python virtual environment using conda.

  i. Install Miniconda (if not already installed):
  Refer to the official Miniconda installation guide for instructions: https://docs.anaconda.com/miniconda/

  ii. Create and Activate the Virtual Environment:
  python >= 3.10 conda create -n dbgpt_env python=3.10
  conda activate dbgpt_env
  
3. Install Dependencies:
  Install project dependencies using pip:
  pip install -e ".[default]"

5. Configure Environment Variables:
  Copy the .env.template file to .env and modify the following variables according to your needs:

  LLM_MODEL (default: chatgpt_proxyllm)
  PROXY_API_KEY (replace with your OpenAI API key)
  PROXY_SERVER_URL (default: https://api.openai.com/v1/chat/completions)
  If using GPT-4
  PROXYLLM_BACKEND=gpt-4

5. Download Large Language Model (Optional):

  download a specific large language model from Hugging Face. For example, to download the text2vec-large-chinese model:

  cd DataGPT
  mkdir models
  cd models
  git clone https://huggingface.co/GanymedeNil/text2vec-large-chinese
  
6. Run the Service:

  Start the server by running:

  python dbgpt/app/dbgpt_server.py
