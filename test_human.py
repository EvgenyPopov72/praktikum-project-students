from student import Student
from curator import Curator

student = Student("Тимофей")
curator = Curator("Марина")


def test_human():
    assert student.ask_question(curator, "мне грустненько, что делать?") == (
           "Студент> Марина, мне грустненько, что делать?\nКуратор> Держись, "
           "всё получится. Хочешь видео с котиками?\n")
