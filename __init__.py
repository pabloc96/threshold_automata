from . import ThresholdAutomaton as ta

"""
This module allow you to simulate a threshold cellular
automaton. You can create multiple instances and iterate
them in a sequential or parallel way.

Functions
---------
	make_automata(n, W, b, grid = None)
		Creates a threshold cellular automaton for the
		given parameters.

	rand(n, W, b, proportion = 0.5)
		Creates a threshold cellular automaton with 
		random grid's values.

	negative(n, W, b)
		Creates a threshold cellular automaton with a 
		grid full of -1s.

"""

def make_automata(n, W, b, grid = None):
	"""
	Creates a threshold cellular automaton.

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

	Returns
	-------
	threshold_automata.ThresholdAutomaton
		A threshold automaton with the given parameters.

	"""
	return ta.ThresholdAutomaton(n, W, b, grid = grid)

def rand(n, W, b, proportion = 0.5):
	"""
	Creates a threshold cellular automaton with random grid's values.
	The probability of a cell taking the value +1 is given by
	the "proportion" parameter.
	
	Parameters
	----------

	n : int
		Size of the grid.
	W : 2-dimensional list or 2-dimensional numpy.ndarray
		Weights matrix.
	b : list or 1-dimensional numpy array
		Threshold vector.
	proportion : float
		Probability of every cell taking a +1 value

	Returns
	-------
	threshold_automata.ThresholdAutomaton
		A threshold automaton with random states following the 
		given parameters.
	"""

	return ta.ThresholdAutomaton(n, W, b, random_grid = True, proportion = proportion)

def negative(n, W, b):
	"""
	Creates a threshold cellular automaton with a grid full of
	-1s.

	Parameters
	----------

	n : int
		Size of the grid.
	W : 2-dimensional list or 2-dimensional numpy.ndarray
		Weights matrix.
	b : list or 1-dimensional numpy array
		Threshold vector.

	Returns
	-------
	threshold_automata.ThresholdAutomaton
		A threshold automaton with the given parameters and a
		grid full of -1s.	
	"""

	return make_automata(n, W, b, grid = None)