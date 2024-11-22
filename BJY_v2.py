class BasicCalories:
    def __init__(self, weight, height ,age):
        self.weight = weight
        self.height = height
        self.age = age
        self.BOV = 447.593 + (9.247 * self.weight) + (3.098 * self.height) - (4.330 * self.age)  # Формула Харисса-Бенедикта базового обмена веществ
        self.CH_low_activity = round(self.BOV * 1.2)        # Суточная каллорийность при низкой активности
        self.CH_middle_activity = round(self.BOV * 1.375)   # Суточная каллорийность при средней активности
        self.CH_high_activity = round(self.BOV * 1.55)      # Суточная каллорийность при высокой активности

    def count_for_weight_loss(self):
        self.CH_low_activity *= 0.8
        self.CH_middle_activity *= 0.8
        self.CH_high_activity *= 0.8
        return (f"Норма каллорийности:  \nПри низкой активности {round(self.CH_low_activity)} \n"
                f"Б:{round((self.CH_low_activity/4)*0.25)} Ж:{round((self.CH_low_activity/9)*0.35)} У:{round((self.CH_low_activity/4)*0.4)} "
                
                f"\nПри средней активности {round(self.CH_middle_activity)} \n"
                f"Б:{round((self.CH_middle_activity/4)*0.25)} Ж:{round((self.CH_middle_activity/9)*0.35)} У:{round((self.CH_middle_activity/4)*0.4)}"
                
                f"\nПри высокой активности {round(self.CH_high_activity)} \n"
                f"Б:{round((self.CH_high_activity/4)*0.25)} Ж:{round((self.CH_high_activity/9)*0.35)} У:{round((self.CH_high_activity/4)*0.4)}")
    def count_for_weight_gain(self):
        self.CH_low_activity *= 1.2
        self.CH_middle_activity *= 1.2
        self.CH_high_activity *= 1.2
        return (f"Норма каллорийности:  \nПри низкой активности {round(self.CH_low_activity)} \n"
                f"Б:{round((self.CH_low_activity / 4) * 0.25)} Ж:{round((self.CH_low_activity / 9) * 0.35)} У:{round((self.CH_low_activity / 4) * 0.4)} "

                f"\nПри средней активности {round(self.CH_middle_activity)} \n"
                f"Б:{round((self.CH_middle_activity / 4) * 0.25)} Ж:{round((self.CH_middle_activity / 9) * 0.35)} У:{round((self.CH_middle_activity / 4) * 0.4)}"

                f"\nПри высокой активности {round(self.CH_high_activity)} \n"
                f"Б:{round((self.CH_high_activity / 4) * 0.25)} Ж:{round((self.CH_high_activity / 9) * 0.35)} У:{round((self.CH_high_activity / 4) * 0.4)}")

def get_input(prompt, valid_inputs):   # Функция, проверяющая, что ввели именно 1 или 2
 while True:
  user_input = input(prompt)
  if user_input in valid_inputs:
   return user_input
  else:
   print("Некорректный ввод. Введите 1 или 2.")

question = get_input("Если похудение введите '1', если набор массы введите '2': ", ("1", "2"))
weight = float(input('Введите ваш вес: '))
height = int(input('Введите ваш рост: '))
age = int(input('Введите ваш возраст: '))

person = BasicCalories(weight, height ,age)
if question == "1":
    print(person.count_for_weight_loss())
if question == "2":
    print(person.count_for_weight_gain())
input()