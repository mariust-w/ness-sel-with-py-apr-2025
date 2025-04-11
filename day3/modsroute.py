class Calc:

    def add(self,num1,num2):
        result = num1+num2
        print(result)

    def sub(self,num1,num2):
        result = num1-num2
        print(result)

    def mul(self,num1,num2):
        result = num1*num2
        print(result)

    def div(self,num1,num2):
        result = num1/num2
        print(result)


class WordProcessor:

    def __init__(self):
        print('Inside constructor')

    @staticmethod
    def get_length(word):
        result = len(word)
        print(result)

    def no_of_words(self,sentence):
        word_list = str(sentence).lower().split(" ")
        print(len(word_list))

    def mul(self,num1,num2):
        result = num1*num2
        print(result)

    def div(self,num1,num2):
        result = num1/num2
        print(result)
