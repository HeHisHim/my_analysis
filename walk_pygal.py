from random_walk import RandomWalk
import pygal

rw = RandomWalk()
rw.fill_walk()

print(rw.x_values)
print(rw.y_values)

frequencies = [rw.y_values.count(value) for value in rw.y_values]

hist = pygal.Bar()
hist.x_labels = [str(x) for x in rw.x_values]

hist.add("D", frequencies)
hist.render_to_file("fuck.svg")