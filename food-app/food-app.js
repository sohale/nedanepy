function choose(choices) {
  var index = Math.floor(Math.random() * choices.length);
  return choices[index];
}
food=["استنبلي", "خورشت بادمجان", "ماکاروني", "بيف استروگانف", "کشک و بادمجان", "دلمه", "زرشک پلو با مرغ", "لازانيا", "پيتزا", "خورشت قيمه", "خوراک لوبيا", "آلبالو پلو", "آبگوشت", "گوشت و لوبيا", "قيمه ريزه", "کله گنجشکي", "ماهي", "کتلت", "کباب تابه اي", "آش رشته", "خورشت نعناع جعفري", "خورشت آلوچه", "تن ماهي"]

console.log(choose(food))
var new1=input()
food.push(new1)
console.log(food)
