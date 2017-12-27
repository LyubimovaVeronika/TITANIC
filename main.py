import pandas
import numpy
import statistics

src = pandas.read_csv('test.csv', index_col='PassengerId')
src2 = pandas.read_csv('train.csv', index_col='PassengerId')

def get_genders_count(data):
    # Функция, которая позволяет найти количество мужчин и женщин
    males = 0
    females = 0
    for gender in data:
        if gender == 'male':
            males += 1
        else:
            females += 1
    return [males,females]

def get_embarked(data):
    # Функция возвращает сопоставление [типы портов] - [кол-во отправившихся из этих портов]
    ports = []
    counts = []
    for port in data:
        if ports.count(port) == 0:
            ports.append(port)
            counts.append(0)
        else:
            counts[ports.index(port)] += 1

    return (ports,counts)

def get_False_count(data):
    # Функция ищет кол-во нулей(False) в переданном поле
    f = 0
    for person in data:
        if person == 0:
            f += 1
    return f

def get_True_count(data):
    # Функция ищет кол-во единиц(True) в переданном поле
    t = 0
    for person in data:
        if person == 1:
            t += 1
    return t

def getGenderInInt(data):
    # Функция переводит пол (male/female) в числовое представление (1/0)
    res = []
    for d in data:
        if d == 'male':
            res.append(1)
        else:
            res.append(0)
    return res

def getNames(sexTarget,ageTarget=0):
    # Функция возвращает список всех лиц нужного пола, возраст которых больше заданной величины
    res = []
    allNames = list(src2['Name'])
    sex = list(src2['Sex'])
    age = list(src2['Age'])
    for i in range(len(allNames)):
        #перебираем список
        name = allNames[i]
        if (sex[i] == sexTarget and ageTarget <= age[i]):
            if (sex[i] == 'male'):
                if (name.find('(') != -1):
                    tmp = name.split('(')[0].split(' ')
                    index = -2
                    if (tmp[index] == 'Mr.' or tmp[index] == 'Master.'):
                        index = -1
                    res.append(tmp[index])
                else:
                    tmp = name.split('(')[0].split(' ')
                    index = -3
                    if (tmp[index] == 'Mr.' or tmp[index] == 'Master.'):
                        index = -2
                    res.append(tmp[index])
            else:
                if (name.find('(') != -1):
                    tmp = name.split('(')[0].split(' ')
                    index = -3
                    if (tmp[index] == 'Mrs.' or tmp[index] == 'Miss.'):
                        index = -2
                    res.append(tmp[index])
                else:
                    tmp = name.split('(')[0].split(' ')
                    index = -2
                    if (tmp[index] == 'Mrs.' or tmp[index] == 'Miss.'):
                        index = -1
                    res.append(tmp[index])
    return res

print('Количество мужчин, женщин')
print(get_genders_count(src2['Sex']))
print()

print('Из каких портов сколько начали путь')
print(get_embarked(src2['Embarked']))
print()

print('Количество погибших людей')
print('{} из {}. Соотношение: {:.2%}'.format(get_False_count(src2['Survived']),len(src2),get_False_count(src2['Survived'])/len(src2)))
print()

print('Количество пассажиров в каждом классе')
print(get_embarked(src['Pclass']))
print()

print('Количество супругов')
print(get_True_count(src2['SibSp']))
print()

print('Количество детей')
print(get_True_count(src2['Parch']))
print()

print('Коэффициент корреляции Пирсона между супругами и детьми')
print(numpy.corrcoef(src2['SibSp'],src2['Parch']))
#Вычисляем коэффициент между двумя величинами
print()

print('Коэффициент корреляции Пирсона между возрастом и параметром survival')
print(numpy.corrcoef(src2['Age'],src2['Survived']))
print()

print('Коэффициент корреляции Пирсона между полом человека и параметром survival')
print(numpy.corrcoef(getGenderInInt(src2['Sex']),src2['Survived']))
print()

print('Коэффициент корреляции Пирсона между классом пассажира и параметром survival')
print(numpy.corrcoef(src2['Pclass'],src2['Survived']))
print()

# mean - среднее значение
print('Средний возраст')
print(src2['Age'].mean())

#median - медиана
print('Медиана возраста')
print(src2['Age'].median())
print()

print('Cредняя стоимость билета')
print(src2['Fare'].mean())

print('Медиана стоимости билета')
print(src2['Fare'].median())
print()

print('Cамое популярное мужское имя')
print(statistics.mode(getNames('male')))
print()

print('Cамое популярное мужское имя среди людей, старше 15 лет')
print(statistics.mode(getNames('male',15)))
print()
print('Самое популярное женское имя')
print(statistics.mode(getNames('female')))
print()
print('Cамое популярное женское имя на корабле среди людей, старше 15 лет')

print(statistics.mode(getNames('female',15)))