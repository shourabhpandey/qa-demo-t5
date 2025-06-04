from transformers import T5Tokenizer, T5ForConditionalGeneration

class Answerer:
    def __init__(self):
        self.tokenizer = T5Tokenizer.from_pretrained("t5-small")
        self.model = T5ForConditionalGeneration.from_pretrained("t5-small")

    def generate_answer(self, context, question):
        prompt = f"question: {question} context: {context}"
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True)
        outputs = self.model.generate(**inputs, max_length=64)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
