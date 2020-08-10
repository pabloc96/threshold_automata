from . import ThresholdAutomaton as ta

def threshold_automaton(n, W, b, grid = None, random_grid = False):
	return ta.ThresholdAutomaton(n, W, b, grid, random_grid)