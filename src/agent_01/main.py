import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
from dotenv import load_dotenv
load_dotenv()

# Set Provider, Base URL and API Key
provider = AsyncOpenAI(
    api_key = os.getenv("GIMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Creating model and configure model
model = OpenAIChatCompletionsModel(
            model = "gemini-2.0-flash-exp",
            openai_client = provider,           
)

# Creating Agent
def run():
    agent = Agent(name="Assistant", instructions="You are a helpful assistant", model = model )
    # Running Agent
    response = Runner.run_sync(agent, "Tell me about most demanding skills to earn massive income in 2025.")
    print(response.final_output)

# Disable the OpenAPI Tracing because we use Gemini API
set_tracing_disabled(disabled = True)