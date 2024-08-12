countWorkHome = 12          # Количество выполненных домашних заданий
countTime = 1.5             # Количество затраченных часов
nameCourse = 'Python'       # Название курса
oneHomeWorkTime = countTime / countWorkHome     # Среднее время на выполнение 1 дом. задания

print('Курс: ', nameCourse, ', всего задач: ', countWorkHome, ', затрачено часов: ', countTime,
      ', среднее время выполнения: ', oneHomeWorkTime, ' часа.')
