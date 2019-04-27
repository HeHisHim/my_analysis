from die import Die
import pygal

#创建两个D6骰子
die_1 = Die()
die_2 = Die(10)

#掷几次骰子，并将结果存储在一个列表中
# results = []
# for roll_num in range(50000):
# 	result = die_1.roll() + die_2.roll()
# 	results.append(result)
results = [die_1.roll() + die_2.roll() for roll_num in range(50000)]


#分析结果
# frequencies = []
# for value in range(2, die_1.num_sides + die_2.num_sides + 1):
# 	frequency = results.count(value)
# 	frequencies.append(frequency)
frequencies = [results.count(value) for value in range(2, die_1.num_sides + die_2.num_sides + 1)]


#对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50,000 times"

label_list = [str(x) for x in range(2, die_1.num_sides + die_2.num_sides + 1)]

hist.x_labels = label_list
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D10", frequencies)
hist.render_to_file("different_visual.svg")