# Задание: Игра "Угадай слово"
'''
Создай игру, где компьютер случайным образом выбирает слово из списка. 
Игроку нужно угадать это слово, вводя буквы. Если игрок угадывает букву, она открывается в слове. 
Если буква не угадана — добавляется «ошибка». Игрок может допустить максимум 6 ошибок. 
Игра должна выводить подсказки и количество ошибок.
'''

# Подсказки
'''
1. Создай список слов для игры
    Начни с создания списка слов, которые компьютер может случайно выбирать для игры. 
    Это может быть список любимых фруктов или любых других коротких слов.

2. Выбор случайного слова
    Используй модуль 'random' для выбора случайного слова из списка. 
    Это будет то слово, которое игрок должен угадать.
    
3. Подготовь переменные для хранения состояния игры
    Чтобы отслеживать, что уже угадано, создай список 'guessed_letters', в который ты будешь добавлять угаданные буквы. 
    Также создай переменную для ошибок 'errors', которая будет увеличиваться при каждой неверной попытке.

4. Приветствие и объяснение правил игры
    Выведи приветствие с помощью 'print', чтобы игрок знал, что от него ожидается. 
    Напомни, что у него ограниченное количество попыток, чтобы угадать слово.
    
5. Основной цикл игры
    Используй цикл 'while', который будет работать, пока количество ошибок меньше максимального значения (max_errors). 
    Этот цикл будет повторяться, пока игрок не угадает слово или не исчерпает свои попытки.
    
6. Отображение текущего состояния слова
    Внутри цикла, с помощью цикла for, собери строку 'display_word', которая показывает игроку, какие буквы он уже угадал, а какие еще нет. 
    Угаданные буквы будут открыты, а неугаданные — скрыты под символами _.    
    
7. Ввод игрока и проверка буквы
    Используй команду 'input', чтобы игрок мог ввести букву. 
    Проверь, не вводил ли он эту букву ранее (например, через условие if).
     -Если буква уже была угадана ранее, выведи сообщение, чтобы игрок попробовал другую букву.
     -Если буква есть в загаданном слове, добавь её в список 'guessed_letters' и выведи сообщение о правильном угадывании.
     -Если буквы нет в слове, увеличь errors на 1 и выведи сообщение, что игрок ошибся.
    
8. Проверка на выигрыш
    После ввода каждой буквы проверь, не угаданы ли уже все буквы. 
    Для этого можно использовать условие, которое проверяет, что все буквы в загаданном слове находятся в 'guessed_letters'.
    
9. Сообщение о проигрыше при превышении попыток
    Если количество ошибок достигает max_errors, игра завершается, 
    и ты выводишь сообщение с загаданным словом, чтобы игрок знал ответ.
'''

# Можешь начать тут




