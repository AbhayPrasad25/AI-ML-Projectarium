from flask import Flask, request, render_template
from flask_cors import CORS
import json
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


app = Flask(__name__)
CORS(app)

model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
conversational_history = []

@app.route('/chatbot', methods = ['POST'])
def handle_prompt():
    data = request.get_data(as_text =TRUE)
    data = json.loads(data)
    input_text = data['prompt']

    # Creating conversational history string 
    history = "/n".join(conversational_history)

    # Tokenize the input text and history
    inputs = tokenizer.encode_plus(history, input_text, return_tensors ="pt")

    # Generating the response from the model
    outputs = model.generate(**inputs, max_length = 60)

    # Decode the response
    response = tokenizer.decode(outputs[0],skip_special_tokens = True).strip()

    # Add interaction to the conversational history
    conversational_history.append(input_text)
    conversational_history.append(response)

    return response

if __name__ == '__main__':
    app.run()

