from random import randint


class Human:
    child = 0

    def __init__(self, name):
        self.name = name
        Human.child += 1
        self.__var = 42

    def answer_question(self, question):
        if question in ["Как твое имя?", "Как тебя зовут?"]:
            return f"{self}> " + self.get_name()
        elif "погод" in question.lower():
            return self.get_weather()
        elif question == "Сколько у меня наследников?":
            return self.get_child_number()
        return f"{self}> Очень интересный вопрос! Не знаю."

    def get_name(self):
        return self.name

    def get_weather(self):
        temp = randint(-10, 10)
        return f"{self}> Я думаю, примерно {temp} градусов"

    @classmethod
    def get_child_number(cls):
        return f"У меня {cls.child} наследников"

    def __str__(self):
        return "Человек"
