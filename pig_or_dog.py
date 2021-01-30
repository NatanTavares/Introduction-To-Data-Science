def second_ml():
    from sklearn.svm import LinearSVC
    from sklearn.metrics import accuracy_score

    # long hair
    # short leg
    # barks
    # likes mud

    pig1 = [0, 1, 0, 1]
    pig2 = [1, 1, 0, 1]

    dog1 = [1, 0, 1, 0]
    dog2 = [0, 1, 1, 1]
    dog3 = [0, 0, 1, 1]

    train_x = [pig1, pig2, dog1, dog2, dog3]
    train_y = [0, 0, 1, 1, 1] # 0: Pig | 1: Dog

    model = LinearSVC()
    model.fit(train_x, train_y)

    test_x = [[1, 0, 0, 1], [0, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 1, 0]]
    predict = model.predict(test_x)

    test_y = [0, 1, 1, 0, 1]
    accuracy = accuracy_score(test_y, predict)

    return [predict, accuracy]


def tr_second():
    animals, porcent = second_ml()
    porcent *= 100

    list_animals = []
    for animal in animals:
        if animal == 0:
            list_animals.append('Pig')
        else:
            list_animals.append('Dog')

    return list_animals, porcent


print(tr_second())