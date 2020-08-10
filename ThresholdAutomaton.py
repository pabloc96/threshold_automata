import numpy as np

class ThresholdAutomaton():
	"""
	This class is used to simulate a threshold cellular automaton.

	Attributes
	----------

	n : int
		Size of the grid.
	W : numpy.ndarray (2-dimesional)
		Weights matrix.
	b : numpy.ndarray (1-dimesional)
		Threshold vector.
	grid : numpy.ndarray (2-dimesional)
		An nxn matrix containing each cell's state (-1 or +1).

	Methods
	-------

	iterate(self, mode = "sequential", order = None)
		Iterates the grid sequentially or in parallel.

	"""

	def __init__(self, n, W, b, grid = None, random_grid = False, proportion = 0.5):
		"""
		Parameters
		----------

		n : int
			Size of the grid.
		W : 2-dimensional list or 2-dimensional numpy.ndarray
			Weights matrix.
		b : list or 1-dimensional numpy array
			Threshold vector.
		grid : 2-dimensional list or 2-dimensional numpy.ndarray or None
			A grid containing -1s and 1s. Its size has to be n, otherwise
			there will be malfunction. If None is given, an nxn grid full 
			of -1s will be created
		random_grid: boolean
			If True, the parameter "grid" will be omited and an nxn grid
			with random values will be created.
		proportion : float
			If the "random_grid" parameter is True, "proportion" indicates
			the percentage of randomly +1s chosen.
		"""


		if not isinstance(W,np.ndarray):
			W = np.array(W)
		if not isinstance(b,np.ndarray):
			b = np.array(b)

		self.n = n
		self.W = W 
		self.b = b 

		if random_grid:
			self.grid = np.random.choice([-1,1], n**2 , p = [1-proportion, proportion]).reshape(n, n)
		elif grid == None:
			self.grid = np.array([[-1]*n]*n)	
		else:
			self.grid = np.array(grid)
	
	def __str__(self):
		return '\n'.join([' | '.join([str("%2i " % u) for u in row]) for row in self.grid])

	def vn_neighborhood(self,x, y):
		return [tuple(np.array([x, y])), tuple(np.array([x + 1, y]) % self.n),\
		tuple(np.array([x - 1, y]) % self.n), tuple(np.array([x, y + 1]) % self.n),\
		tuple(np.array([x, y - 1]) % self.n)]

	def f(self, x, y):
		neighborhood = self.vn_neighborhood(x,y)

		total = 0
		W_x = b_i = self.n*x + y

		for neighbour in neighborhood:
			W_y = self.n*neighbour[0] + neighbour[1] 
			total += self.W[W_x,W_y] * self.grid[neighbour[0], neighbour[1]] 
			
		total -= self.b[b_i]

		if total <= 0:
			return -1
		return 1

	def iterate(self, mode = "sequential", order = None):
		"""
		Iterates the automaton.

		Parameters
		----------

		mode : str
			If "parallel" is given, it evolves the whole grid 
			simoultaniesly. If "sequential" is given, it evolves the
			grid in the order given by the "order" parameter.
		order : list or numpy.ndarray (1-dimensional)
			If the "mode" parameter is "sequential", the grid will
			be iterated following the order given by this parameter
			(from 0 to n**2).
		"""
		if not order is None:
			order = np.array(order)

		if mode == "parallel":	
			new_grid = np.array([[0]*self.n]*self.n)

			for i in range(self.n):
				for j in range(self.n):
					new_grid[i,j] = self.f(i,j)
			self.grid = np.copy(new_grid)
		else:
			if order is None or (not order.size == self.n**2):
				print("Iteration mode is not parallel but no (or incomplete) order matrix was given. It was not iterated.")
			else:
				for i in order:
					j = 0
					while i >= self.n:
						j += 1
						i -= self.n
					self.grid[j,i] = self.f(j,i)