#Егор Рузанов
def rate(right, questions, answer):
    for i in range(len(questions)):
        ask = input(questions[i])
        if ask == answer[i]:
            right += 1
    if right > 3:
        rating = 'Хороший результат, можно принять на работу.'
    elif right == 3:
        rating = 'Средний результат, можно принять человека, но не в первую очередь.'
    elif right < 3:
        rating = 'На данный момент Мы не готовы принять вас как потенциального кандидата на должность.'
    return(right, rating)
