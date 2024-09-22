import subprocess

# Define the path to the Alpaca binary
ALPACA_BIN = "backend/alpaca.cpp/chat"  # Change this to the correct path of your 'chat' binary
MODEL_PATH = "backend/alpaca.cpp/ggml-alpaca-7b-q4.bin"  # Path to your .bin model file

# Function to run the Alpaca chatbot with an input prompt
def get_alpaca_response(prompt):
    process = subprocess.Popen(
        [ALPACA_BIN, "-m", MODEL_PATH, "-p", prompt],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    
    output, error = process.communicate()

    if error:
        print(f"Error: {error.decode('utf-8')}")
        return None

    # Print the raw output for debugging
    raw_output = output.decode('utf-8')
    print(f"Raw Output: {repr(raw_output)}")  # Use repr to show any hidden characters
    return raw_output

# Example usage as a method
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    response = get_alpaca_response(user_prompt)
    if response:
        print("Alpaca's response:")
        print(response)
