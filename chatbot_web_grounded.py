import os
import uuid

import cohere

co = cohere.Client(str(os.environ.get("COHERE_KEY")))
user_input = ""
conversation_id = str(uuid.uuid4())
MAX_TURNS = 10

for i in range(MAX_TURNS):
  user_input = input("User: ")

  if user_input.lower() == "stop":
    break

  response = co.chat(
      user_input,
      model="command-nightly",
      conversation_id=conversation_id,
      connectors=[{"id":"web-search"}],
  )

  print("\nChatbot:\n", response.text.strip(),
        "\n\n")  # Newlines because LLMs are wordy
  
