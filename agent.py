import warnings
warnings.filterwarnings(action="ignore", message=r"datetime.datetime.utcnow") 

from strands import Agent
# Initialize your agent
agent = Agent(
    model="anthropic.claude-3-5-sonnet-20240620-v1:0",  # Optional: Specify the model ID
    system_prompt="You are a helpful assistant that provides concise responses."
)

# Send a message to the agent
response = agent("Hello! Tell me a joke.")
print(response)