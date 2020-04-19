'''scrabble'''

import plotly
from plotly.offline import plot

import numpy as np
from string import ascii_lowercase


letter_count_map = {
	'a': 9,
	'b': 2,
	'c': 2,
	'd': 4,
	'e': 12,
	'f': 2,
	'g': 3,
	'h': 2,
	'i': 9,
	'j': 1,
	'k': 1,
	'l': 4,
	'm': 2,
	'n': 6,
	'o': 8,
	'p': 2,
	'q': 1,
	'r': 6,
	's': 4,
	't': 6,
	'u': 4,
	'v': 2,
	'w': 2,
	'x': 1,
	'y': 2,
	'z': 1,
}

letter_value_map = {
	'a': 1,
	'b': 3,
	'c': 3,
	'd': 2,
	'e': 1,
	'f': 4,
	'g': 2,
	'h': 4,
	'i': 1,
	'j': 8,
	'k': 5,
	'l': 1,
	'm': 3,
	'n': 1,
	'o': 1,
	'p': 3,
	'q': 10,
	'r': 1,
	's': 1,
	't': 1,
	'u': 1,
	'v': 4,
	'w': 4,
	'x': 8,
	'y': 4,
	'z': 10,
}

filename = 'Collins Scrabble Words (2015).txt'
with open(filename, 'r') as f:
	LEGAL_SCRABBLE_WORDS = f.readlines()


# count letters in all legal words
collinsLetter_count_map = {}
for letter in ascii_lowercase:
	count = 0
	for word in LEGAL_SCRABBLE_WORDS:
		count += word.lower().count(letter)
	collinsLetter_count_map[letter] = count

lettersInCollins = 1.0 * sum(collinsLetter_count_map.values())
scrabbleTileCount = 1.0 * sum(letter_count_map.values())


alphabet = list(ascii_lowercase)
trace0 = {
	'x': alphabet,
	'y': [collinsLetter_count_map[k]/lettersInCollins for k in alphabet],
	'type': 'bar',
	'name': 'letter % in Collins Dictionary',
}
trace1 = {
	'x': alphabet,
	'y': [letter_count_map[k]/scrabbleTileCount for k in alphabet],
	'type': 'bar',
	'name': 'tile % per 92 scrabble tiles',
}
trace2 = {
	'x': alphabet,
	'y': [abs(trace1['y'][k] - trace0['y'][k]) for k in range(len(alphabet))],
	'type': 'scatter',
	'mode': 'markers',
	'marker': {
		'size': 10,
		'symbol': 'triangle-up',
		'color': 'rgb(0,0,0)',
	},
	'name': 'delta',
}

fig = {
	'data': [trace0, trace1, trace2],
	'layout': {
		'title': 'scrabble letter frequency and points',

	}
}

correlation = np.corrcoef(trace0['y'], trace1['y'])[0][1]
plot(fig)
