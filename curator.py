from human import Human


class Curator(Human):
    def answer_question(self, question):
        if question == "мне грустненько, что делать?":
            return f"{self}> Держись, всё получится. Хочешь видео с котиками?"
        else:
            return super().answer_question(question)

    def __str__(self):
        return "Куратор"
