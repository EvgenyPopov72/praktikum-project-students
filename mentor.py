from human import Human


class Mentor(Human):
    def answer_question(self, question):
        if question == "мне грустненько, что делать?":
            return f"{self}> Отдохни и возвращайся с вопросами по теории."
        else:
            return super().answer_question(question)

    def __str__(self):
        return "Ментор"
