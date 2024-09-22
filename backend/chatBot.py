from llama_cpp import Llama
import webScraper as ws

class chatBot:
    def __init__(self):
        self.model = Llama(model_path="backend/llama.cpp/models/llama-2-7b-chat.Q4_K_S.gguf", n_ctx=2048, n_batch=128)

    def generate_response(self, prompt, max_tokens=300, stop=["Human:", "\n"], echo=False):
        output = self.model(prompt, max_tokens=max_tokens, stop=stop, echo=echo)
        return output['choices'][0]['text']
    
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
        
        response = self.generate_response(prompt)
        print("AI: " + response.strip())

c = chatBot()
c.get_context("Arora")
