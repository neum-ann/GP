#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import db
from app.models import *

db.create_all()

# Вопрос 1
T=Test(question_A='Иногда я предоставляю другим возможность взять на себя ответственность за решение спорного вопроса.', question_B='Чем обсуждать то, в чем мы расходимся, я стараюсь обратить внимание на то, в чем согласны мы оба.')
db.session.add(T)

# Вопрос 2
T=Test(question_A='Я стараюсь найти компромиссное решение.', question_B='Я пытаюсь уладить дело с учетом всех интересов другого и моих собственных.')
db.session.add(T)

# Вопрос 3
T=Test(question_A='Обычно я настойчиво стремлюсь добиться своего.', question_B='Я стараюсь успокоить другого и стремлюсь, главным образом, сохранить наши отношения.')
db.session.add(T)

# Вопрос 4
T=Test(question_A='Я стараюсь найти компромиссное решение.', question_B='Иногда я жертвую своими собственными интересами ради интересов другого человека.')
db.session.add(T)

# Вопрос 5
T=Test(question_A='Улаживая спорную ситуацию, я все время стараюсь найти поддержку у другого.', question_B='Я стараюсь сделать все, чтобы избежать бесполезной напряженности.')
db.session.add(T)

# Вопрос 6
T=Test(question_A='Я стараюсь избежать возникновения неприятностей для себя.', question_B='Я стараюсь добиться своего.')
db.session.add(T)

# Вопрос 7
T=Test(question_A='Я стараюсь отложить решение сложного вопроса с тем, чтобы со временем решить его окончательно.', question_B='Я считаю возможным в чем-то уступить, чтобы добиться чего-то другого.')
db.session.add(T)

# Вопрос 8
T=Test(question_A='Обычно я настойчиво стремлюсь добиться своего.', question_B='Первым делом я стараюсь ясно определить то, в чем состоят все затронутые интересы и спорные вопросы.')
db.session.add(T)

# Вопрос 9
T=Test(question_A='Думаю, что не всегда стоит волноваться из-за каких-то возникающих разногласий.', question_B='Я предпринимаю усилия, чтобы добиться своего.')
db.session.add(T)

# Вопрос 10
T=Test(question_A='Я твердо стремлюсь достичь своего.', question_B='Я пытаюсь найти компромиссное решение.')
db.session.add(T)

# Вопрос 11
T=Test(question_A='Первым делом я стараюсь ясно определить то, в чем состоят все затронутые интересы и спорные вопросы.', question_B='Я стараюсь успокоить другого и стремлюсь, главным образом, сохранить наши отношения.')
db.session.add(T)

# Вопрос 12
T=Test(question_A='Зачастую я избегаю занимать позицию, которая может вызвать споры.', question_B='Я даю возможность другому в чем-то остаться при своем мнении, если он также идет навстречу мне.')
db.session.add(T)

# Вопрос 13
T=Test(question_A='Я предлагаю среднюю позицию.', question_B='Я пытаюсь убедить другого в преимуществах своей позиции.')
db.session.add(T)

# Вопрос 14
T=Test(question_A='Я сообщаю другому свою точку зрения и спрашиваю о его взглядах.', question_B='Я пытаюсь показать другому логику и преимущество своих взглядов.')
db.session.add(T)

# Вопрос 15
T=Test(question_A='Я стараюсь успокоить другого и стремлюсь, главным образом, сохранить наши отношения.', question_B='Я стараюсь сделать все необходимое, чтобы избежать напряженности.')
db.session.add(T)

# Вопрос 16
T=Test(question_A='Я стараюсь не задеть чувства другого.', question_B='Я пытаюсь убедить другого в преимуществах моей позиции.')
db.session.add(T)

# Вопрос 17
T=Test(question_A='Обычно я настойчиво стремлюсь добиться своего.', question_B='Я стараюсь сделать все, чтобы избежать бесполезной напряженности.')
db.session.add(T)

# Вопрос 18
T=Test(question_A='Если это сделает другого счастливым, я дам ему возможность настоять на своем.', question_B='Я дам возможность другому в чем-то оставаться при своем мнении, если он также идет мне навстречу.')
db.session.add(T)

# Вопрос 19
T=Test(question_A='Первым делом я стараюсь ясно определить то, в чем состоят все затронутые интересы и спорные вопросы.', question_B='Я стараюсь отложить решение сложного вопроса с тем, чтобы со временем решить его окончательно.')
db.session.add(T)

# Вопрос 20
T=Test(question_A='Я пытаюсь немедленно разрешить наши разногласия.', question_B='Я стараюсь найти наилучшее сочетание выгод и потерь для нас обоих.')
db.session.add(T)

# Вопрос 21
T=Test(question_A='Ведя переговоры, я стараюсь быть внимательным к желаниям другого.', question_B='Я всегда склоняюсь к прямому обсуждению проблемы.')
db.session.add(T)

# Вопрос 22
T=Test(question_A='Я пытаюсь найти позицию, которая находится посередине между моей и той, которая отстаивается другим.', question_B='Я отстаиваю свои желания.')
db.session.add(T)

# Вопрос 23
T=Test(question_A='Как правило, я озабочен тем, чтобы удовлетворить желания каждого из нас.', question_B='Иногда я предоставляю другим возможность взять на себя ответственность за решение спорного вопроса.')
db.session.add(T)

# Вопрос 24
T=Test(question_A='Если позиция другого кажется ему очень важной, я постараюсь пойти навстречу его желаниям.', question_B='Я стараюсь убедить другого в необходимости прийти к компромиссу.')
db.session.add(T)

# Вопрос 25
T=Test(question_A='Я пытаюсь показать другому логику и преимущество своих взглядов.', question_B='Ведя переговоры, я стараюсь быть внимательным к желаниям другого.')
db.session.add(T)

# Вопрос 26
T=Test(question_A='Я предлагаю среднюю позицию.', question_B='Я почти всегда озабочен тем, чтобы удовлетворить желания каждого.')
db.session.add(T)

# Вопрос 27
T=Test(question_A='Зачастую я избегаю занимать позицию, которая может вызвать споры.', question_B='Если это сделает другого счастливым, я дам ему возможность настоять на своем.')
db.session.add(T)

# Вопрос 28
T=Test(question_A='Обычно я настойчиво стремлюсь добиться своего.', question_B='Улаживая спорную ситуацию, я обычно стараюсь найти поддержку у другого.')
db.session.add(T)

# Вопрос 29
T=Test(question_A='Я предлагаю среднюю позицию.', question_B='Думаю, что не всегда стоит волноваться из-за каких-то возникающих разногласий.')
db.session.add(T)

# Вопрос 30
T=Test(question_A='Я стараюсь не задеть чувств другого.', question_B='Я всегда занимаю такую позицию в спорном вопросе, чтобы мы могли совместно с другим заинтересованным человеком добиться успеха.')
db.session.add(T)

db.session.commit()

# Действия если запускается именно этот файл
if __name__=='__main__':
	pass