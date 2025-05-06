# 🤖 Introduction to OpenAI Agent SDK powered by Google Gemini 

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/waheed444/OpenAI_SDK_Agent_01)


## Table of Contents 🚀

* [Description](#description)
* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)

⚡ * [Official Documentation ](https://openai.github.io/openai-agents-python/)

## Description

The OpenAI Agents SDK enables you to build agentic AI apps in a lightweight, easy-to-use package with very few abstractions.This project demonstrates the integration of the OpenAI-compatible SDK with Google's Gemini API to build an intelligent, conversational AI agent. The agent is designed to understand user prompts and generate insightful, human-like responses.
In this implementation, the AI agent is tasked with recommending high-income skills for 2025, showcasing its ability to deliver relevant and valuable information. By leveraging the Gemini 2.0 Flash model, the system benefits from fast and efficient language generation.This setup reflects a modular, production-ready approach for integrating third-party large language models (LLMs) into custom AI solutions.




## Features

* 🤖 **Custom AI Agent:** Built using the Agent and Runner pattern for modularity and scalability.
* 🌐 **Google Gemini 2.0 Flash Integration:**  Utilizes Google's API for access to the powerful Gemini language model.
* 🔑 **Secure API Key Management:** Employs `python-dotenv` for safe and convenient API key handling.
* 🧠 **Dynamic Prompt Handling:**  Processes and responds effectively to a wide range of user prompts.
* ⚡ **Asynchronous Communication:**  Leverages `AsyncOpenAI` for optimized asynchronous communication with OpenAI, improving speed and responsiveness.
* 🐍 **Clean Python Codebase:**  Maintained with a focus on readability, modularity, and best practices.


## Installation

1. **Clone the Repository:**

```bash
git clone https://github.com/waheed444/OpenAI_SDK_Agent_01.git
cd OpenAI_SDK_Agent_01
```

2. **Create and Activate a Virtual Environment:**

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

3. **Install Dependencies:**

```bash
pip install -r requirements.txt
```
**OR Install Dependencies:**
```bash
pip install openai-agents python-dotenv

```

4. **Set up `.env` file:**

Create a `.env` file in the root directory and add your Gemini API key:

```
GIMINI_API_KEY  =  your_actual_gemini_api_key_here 
```

**Note:** Replace `your_actual_gemini_api_key_here` with your actual Gemini API key.


## Usage

The agent is designed to provide insightful responses to various prompts.  For example, a prompt such as "What are the most in-demand skills for high income in 2025?" might produce output similar to:

```
"The most in-demand skills for massive income in 2025 include... [list of skills]"
```

More detailed usage instructions and example prompts will be provided in the project's documentation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Contributing
We welcome contributions to improve this project! Please follow these steps:

1. **Fork** the repository.
2. **Create a new branch:** `git checkout -b feature-name`
3. **Make your changes** and ensure they adhere to the project's coding style and best practices.
4. **Commit your changes:** `git commit -m "Add feature"`
5. **Push to the branch:** `git push origin feature-name`
6. **Submit a pull request** with a clear description of your changes and their benefits.
If you find any issues or want to improve this project, feel free to open a [GitHub issue](https://github.com/waheed444/OpenAI_SDK_Agent_01/issues) or submit a pull request.

This repo is only for learning and exploring new things, feel free to fork it, explore, or give suggestions!

**Star ⭐ the repo if it helps you!**

---

## 🙌 Let's Connect

<p align="left">
  <a href="https://www.linkedin.com/in/waheed444/?originalSubdomain=pk)" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=flat-square&logo=linkedin" alt="LinkedIn">
  </a>
  <a href="https://github.com/waheed444" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub">
  </a>
  <a href="waheedahmad5519@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Gmail">
  </a>
</p>

---
