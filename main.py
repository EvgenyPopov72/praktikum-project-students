from code_reviewer import CodeReviewer
from curator import Curator
from human import Human
from mentor import Mentor
from student import Student
from weather_man import WeatherMan

student = Student("Тимофей")
curator = Curator("Марина")
mentor = Mentor("Ира")
reviewer = CodeReviewer("Евгений")
friend = Human("Виталя")
weather_man = WeatherMan("Игорь")
# weather_man2 = WeatherMan("Игорь")

print(student.ask_question(curator, 'мне грустненько, что делать?'))
print(student.ask_question(friend, 'Как твое имя?'))
print(student.ask_question(mentor, 'мне грустненько, что делать?'))
print(student.ask_question(reviewer, 'когда каникулы?'))
print(student.ask_question(reviewer, 'что не так с моим проектом?'))
print(student.ask_question(friend, 'как устроиться на работу питонистом?'))
print(student.ask_question(mentor, 'как устроиться работать питонистом?'))
print(student.ask_question(mentor, 'как с погодой?'))

print(student.ask_question(weather_man, 'как с погодой?'))
print(student.ask_question(friend, 'Сколько у меня наследников?'))
