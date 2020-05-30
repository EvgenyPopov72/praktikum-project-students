from human import Human


class Student(Human):
    #  метод ask_question() принимает параметр someone:
    #  это объект, экземпляр класса Curator, Mentor или CodeReviewer,
    #  которому Student задаёт вопрос;
    #  параметр question — это просто строка
    #  имя объекта и текст вопроса задаются при вызове метода ask_question
    def ask_question(self, someone, question):
        return f"{self}> {someone.name}, {question}\n" + (
               someone.answer_question(question) + "\n")

    def __str__(self):
        return "Студент"
