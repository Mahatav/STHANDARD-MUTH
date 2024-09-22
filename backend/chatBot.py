from llama_cpp import Llama
from backend import webScraper as ws

class chatBot:
    def __init__(self):
        self.model = Llama(model_path="backend/llama.cpp/models/llama-2-7b-chat.Q4_K_S.gguf", n_ctx=2048, n_batch=128)
        self.conversation_history = []

    def generate_response(self, user_input, max_tokens=300):
        self.conversation_history.append(f"Human: {user_input}")
        prompt = "\n".join(self.conversation_history) + "\nAI:"
        
        response = self.model(prompt, max_tokens=max_tokens, stop=["Human:", "\n"], echo=False)
        ai_response = response['choices'][0]['text'].strip()
        
        self.conversation_history.append(f"AI: {ai_response}")
        
        # Keep conversation history within context window
        while len("\n".join(self.conversation_history)) > 1500:
            self.conversation_history.pop(0)
        
        return ai_response
    
    def get_context(self, lastName):
        webScraper = ws.WebScraper(lastName)
        context = webScraper.name_info
        prompt = f"Please summarize the following information about the last name {lastName} in concise sentences:\n"
        for info in context:
            prompt += f"{info['title']}: {info['content'][:500]}\n"
                 
        # Ensure the prompt fits within the context window
        max_prompt_length = 3000  # Adjusted to a lower value
        if len(prompt) > max_prompt_length:
            prompt = prompt[:max_prompt_length] + "..."
        
        return self.generate_response(prompt)
