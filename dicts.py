from random import randint

# участники чата
people = ['@guitaristdave', '@Mishana88', '@forevermarche', '@MaxSolo94', '@ne_max', '@KickAss6666', '@alexaktug']

# список фраз 1
wait_phrases = ['Хмммм очень сложно... Столько любителей футбола...', 'Пиздец, тут даже есть болельщик Реала и любитель огромных черных хуев. Зачем меня позвали то? Ну ладно, поищу', 'Так-так-так.. Кажется кто-то на самом деле болеет за Барсу. Сейчас я вычислю эту геюгу', 'Хахаха ребята, ну вы даете. Мне же придется искать пидора в пидорском чате. Ладно, сейчас достану голубой радар', 'Хммм...Я вижу много пидорства...Еще неплохой внешний вид, есть разработанное очко, о да...и неукротимое желание ебаться с мужиками']

# список фраз 2
final_phrases = ['Любитель Барселоны и Тоттенхема, пероснальный фанат пары Кокорин-Мамаев.\nФу таким быть', 'Он настолько пидор, что смотрит матчи РПЛ вместо порно', 'В юношестве он играл в футбол на позиции вратаря, но все команды мира его забраковали из-за того, что он часто пускал в очко.\nПосле матча', 'Он настолько пидор, что его пердеж пахнет членами. И сосиски он не жует, а сразу глотает целиком', 'Дзюба записывал видео для него', 'Во время исполнения штрафного удара держался руками за член. Не свой', 'I WANNA TAKE YOU TO THE GAY BAR!']

call_phrase = 'Сейчас я вычислю пидорка'
desicion_phrase = 'Что ж. Кажется, я определился'


# список для обнуления статистики
null_list = ['@guitaristdave;0\n', '@Mishana88;0\n', '@forevermarche;0\n', '@MaxSolo94;0\n', '@ne_max;0\n', '@KickAss6666;0\n', '@alexaktug;0\n']

# фраа при вызове команды /start
start_phrase = 'Привет\nВот что я умею:\n/today - покажу матчи топ-5 чемпионатов на сегодня + ЛЧ и ЛЕ\n/yest - результаты вчерашних матчей\n/table - турнирные таблицы топ-5\n/pidor - выясню, кто тут пидор\n/stat - покажу статистику по пидорам\n'

def say_it(phrases: list):
    return phrases[randint(0, len(phrases) - 1)]