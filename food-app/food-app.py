import random
food=["استنبلي", "خورشت بادمجان", "ماکاروني", "بيف استروگانف", "کشک و بادمجان", "دلمه", "زرشک پلو با مرغ", "لازانيا", "پيتزا", "خورشت قيمه", "خوراک لوبيا", "آلبالو پلو", "آبگوشت", "گوشت و لوبيا", "قيمه ريزه", "کله گنجشکي", "ماهي", "کتلت", "کباب تابه اي", "آش رشته", "خورشت نعناع جعفري", "خورشت آلوچه", "تن ماهي"]
print(random.choice(food))
new=input()
food.append(new)
print(food)
