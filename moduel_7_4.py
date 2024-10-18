team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
team_1 = '"Мастера кода"'
team_2 = '"Волшебники данных"'
task_total = score_1 + score_2
average_time = (team1_time + team2_time) / 2


print('В команде мастера кода участников: %s' % team1_num)
print('Итого сегодня в командах участников: %(a)d и %(b)d' % {'a': team1_num, 'b': team2_num})
print('Команда "Волшебники данных" решила задач: {}'.format(score_2))
print('Волшебники данных решили задачи за {}'.format(team1_time))
print(f'Команды решили {score_1} и {score_2} задач')
print(f'Сегодня было решено {task_total} задач, в среднем по {average_time} секунды на задачу')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    print(f'Победа команды {team_1}')
elif score_2 > score_1 or score_2 == score_1 and team2_time > team1_time:
    print(f'Победа команды {team_2}')
else:
    print('Ничья')