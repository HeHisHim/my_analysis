from random import choice

class RandomWalk():
	"""一个生成随机漫步数据的类"""
	def __init__(self, number_points = 10):
		"""初始化随机漫步属性"""
		self.number_points = number_points

		#所有随机漫步都始于(0, 0)
		self.x_values = [0]
		self.y_values = [0]

	def get_step(self):
		"""确定每次漫步的距离和方向"""
		direction = choice([1, -1])
		distance = choice([1, 2, 3, 4, 5])
		step = direction * distance

		return step

	def fill_walk(self):
		"""计算随机漫步包含的所有点"""

		#不断漫步，直到列表达到指定的长度
		while len(self.x_values) < self.number_points:
			#决定前进方向以及沿这个方向前进的距离
			x_step = self.get_step()
			y_step = self.get_step()

			#拒绝原地踏步
			if 0 == x_step and 0 == y_step:
				continue

			#计算下一个点的x和y值
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step

			self.x_values.append(next_x)
			self.y_values.append(next_y)




	