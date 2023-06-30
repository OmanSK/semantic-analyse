class Answer:
    def __init__(self):
        self.semantics = {"LABEL_1": "Positive", "LABEL_0": "Negative"}

    def get_semantic(self, x):
        if isinstance(x, str):
            return self.semantics.get(x)
        else:
            raise ValueError("Wrong value. Only string")

    def get_rating(self, x, status):
        if isinstance(x, float):
            x = round(x, 2)
            if status == "Positive":
                value = round(x * 10)
            else:
                value = round((1 - x) * 10)
            return value

    def get_result(self, answer):
        answer = answer[0]
        label, score = answer["label"], answer["score"]

        semantic = self.get_semantic(label)
        if semantic is not None:
            rating = self.get_rating(score, semantic)
            #because minimum is 1
            if rating == 0:
                rating += 1
        return semantic, rating
