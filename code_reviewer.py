from human import Human


class CodeReviewer(Human):
    def answer_question(self, question):
        if question == "что не так с моим проектом?":
            return f"{self}> О, вопрос про проект, это я люблю."
        else:
            return super().answer_question(question)

    def __str__(self):
        return "Ревьюер"
