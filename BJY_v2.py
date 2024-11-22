class BasicCalories:
    def __init__(self, weight, height ,age):
        self.weight = weight
        self.height = height
        self.age = age
        self.BOV = 447.593 + (9.247 * self.weight) + (3.098 * self.height) - (4.330 * self.age)  # Формула Харисса-Бенедикта базового обмена веществ
        self.CH_low_activity = round(self.BOV * 1.2)        # Суточная каллорийность при низкой активности
        self.CH_middle_activity = round(self.BOV * 1.375)   # Суточная каллорийность при средней активности
        self.CH_high_activity = round(self.BOV * 1.55)      # Суточная каллорийность при высокой активности

    def weight_loss_or_gain(self, loss_or_gain: str) ->str:
        if loss_or_gain == 1:
            self.x = 0.8      #коэффициент для похудения
        self.x = 1.2          #коэффициент для набора массы

        self.CH_low_activity *= self.x
        self.CH_middle_activity *= self.x
        self.CH_high_activity *= self.x
        return (f"Норма каллорийности:  \nПри низкой активности {round(self.CH_low_activity)} \n"
                f"Б:{round((self.CH_low_activity / 4) * 0.25)} Ж:{round((self.CH_low_activity / 9) * 0.35)} У:{round((self.CH_low_activity / 4) * 0.4)} "

                f"\nПри средней активности {round(self.CH_middle_activity)} \n"
                f"Б:{round((self.CH_middle_activity / 4) * 0.25)} Ж:{round((self.CH_middle_activity / 9) * 0.35)} У:{round((self.CH_middle_activity / 4) * 0.4)}"

                f"\nПри высокой активности {round(self.CH_high_activity)} \n"
                f"Б:{round((self.CH_high_activity / 4) * 0.25)} Ж:{round((self.CH_high_activity / 9) * 0.35)} У:{round((self.CH_high_activity / 4) * 0.4)}")
        input()
def get_input(prompt: str, valid_inputs: tuple) -> str:   # Функция, проверяющая, что ввели именно 1 или 2
     while True:
         user_input = input(prompt)
         if user_input in valid_inputs:
            return user_input
         else:
            print("Некорректный ввод. Введите 1 или 2.")
def user_input(prompt: str)->float: #Проверка, что вводные данные - это числа
    while True:
        user_input = input(prompt)
        try:
            user_input = float(user_input)
            return user_input
        except ValueError:
            print("Введите число! (если число с десятымы, то введите его через символ «.»)")


loss_or_gain = get_input('Введите 1 - для похудения . 2 - для набора массы', ('1','2'))
weight = user_input('Введите ваш вес: ')
height = user_input('Введите ваш рост: ')
age = user_input('Введите ваш возраст: ')
person = BasicCalories(weight, height ,age)
print(person.weight_loss_or_gain(loss_or_gain))



