from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import pipeline, AutoTokenizer


path = "model"

model = ORTModelForSequenceClassification.from_pretrained(path, file_name="semantic.onnx")
tokenizer = AutoTokenizer.from_pretrained(path)

cls_pipeline = pipeline("text-classification", model=model, tokenizer=tokenizer)

meaning = cls_pipeline("I like  burritos a little bit")

class SemanticModel:

    def __init__(self):
        self.model = ORTModelForSequenceClassification.from_pretrained(path, file_name="semantic.onnx")
        self.tokenizer = AutoTokenizer.from_pretrained(path)
        self.pipeline = pipeline("text-classification", model=self.model, tokenizer=self.tokenizer)
    
    def get_result(self, string):

        if isinstance(string, str):
            result = self.pipeline(string)
            return result
        else:
            raise ValueError ("Class can get only string")
