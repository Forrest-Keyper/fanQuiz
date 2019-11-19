quiz = [
        'What color is the sky? \n A) Red\n B) Blue C) Yellow \n D)The sky is an illusion.\n Choose with A-D.\n',
        'What color are pine trees?',
        'How many leaves are on a clover?',
        'How many legs does a walrus have?',
        'Can a chicken fly?',
        'Can a european swallow carry a coconut?'
        ]

answerKey = ['d', 'c', '15', '100', 'F', 'T']

responses = []
respQuality = []


def questionOne():
    answer = 'd'
    print('1. What is the name of Warcraft\'s planet?')
    response = input('Please choose you answer by responding with A-D\nA)Artlong\nB)Azul\nC)Archon\nD)Azeroth\n')
    responses.append(response)
    quality = 0
    if response.lower() == answer:
        quality = 1
        pass
    else:
        pass
    respQuality.append(quality)
    return quality


def questionTwo():
    answer = 'c'
    print('2. What was the second WoW expansion?')
    response = input('Please choose you answer by responding with A-D\nA)Blazing Saddles\nB)Holy Purification\nC)Burning Crusade\nD)Demon\'s Descent\n')
    responses.append(response)
    quality = 0
    if response.lower() == answer:
        quality = 1
        pass
    else:
        pass
    respQuality.append(quality)
    return quality


def questionThree():
    answer = '15'
    print('3. Rounded to the nearest dollar what does a WoW subscription cost each month?')
    response = input('Please provide a numerical response. \n')
    responses.append(response)
    quality = 0
    if response.lower() == answer:
        quality = 1
        pass
    else:
        pass
    respQuality.append(quality)
    return quality

def questionFour():
    answer = '100'
    print('4. How many silver pieces comprise 1 gold piece?')
    response = input('Please provide a numerical response. \n')
    responses.append(response)
    quality = 0
    if response.lower() == answer:
        quality = 1
        pass
    else:
        pass
    respQuality.append(quality)
    return quality

def questionFive():
    answer = 'f'
    print('5. Once you delete your hearthstone you can never attain a new one.')
    response = input('Please respond \'T\' or \'F\' to the statment to mark as true or false.\n')
    responses.append(response)
    quality = 0
    if response.lower() == answer:
        quality = 1
        pass
    else:
        pass
    respQuality.append(quality)
    return quality

def questionSix():
    answer = 't'
    print('6. Blizzard has immortalized fans who have left their mark upon the community in the game.')
    response = input('Please respond \'T\' or \'F\' to the statment to mark as true or false.\n')
    responses.append(response)
    quality = 0
    if response.lower() == answer:
        quality = 1
        pass
    else:
        pass
    respQuality.append(quality)
    return quality

def score(responses):
    correct = 0
    for response in range(len(responses)):
        if responses[response] == 0:
            questionNumber = str(response + 1)
            print('Question ' + questionNumber + ' was incorrect. The correct answer was ' + answerKey[response] + '.')
            pass
        elif responses[response] == 1:
            questionNumber = str(response + 1)
            print('Question ' + questionNumber + ' was correct!')
            correct += 1
            pass
    print('You scored ' + str(correct) + ' out of 6!')
    if correct <= 2:
        print('You\'ve surely explored some territory, but you\'ll need a few levels to beat this boss!')
    elif correct > 2 and correct <= 4:
        print('As a clearly experienced warrior I would have expected more. No matter. There are always more battles to fight.')
    else:
        print('Your prowess is unmatched. Lok\'tar Ogar. For the Horde!')


def quiz():
    print(questionOne())
    print(questionTwo())
    print(questionThree())
    print(questionFour())
    print(questionFive())
    print(questionSix())
    # print(score(respQuality))

quiz()
