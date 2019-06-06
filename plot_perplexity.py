import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

exponential = lambda x, a, b, c: a + (b * np.exp(x*-c))
linear = lambda x, a, b: a + b * x
powerlaw = lambda x, amp, index: amp * (x**index)

with plt.style.context(('seaborn')):

	xdata = np.array([2,4,8,16])
	ydata = np.array([1.6855,1.8038,1.9611,2.0759])
	xdata1 = np.arange(2,xdata[3]+1)
	# a = 2.1193
	# b = -0.6065917
	# c = 0.1659847
	# plt.plot(xdata1, exponential(xdata1.astype(float), a, b, c), label='Transformer XL - Exponential fit')
	plt.plot(xdata, ydata, label='Transformer XL - V=4')
	plt.scatter(xdata, ydata)

	xdata = np.array([2,4,8,16])
	ydata = np.array([1.413,1.486,1.658,1.708])
	# amp = 1.320213
	# index = 0.09699675
	# plt.plot(xdata1, powerlaw(xdata1.astype(float), amp, index), 'g-.', label='AWD-LSTM - Power Law fit')
	# a = 1.736612
	# b = -0.4979032
	# c = 0.198834
	# plt.plot(xdata1, exponential(xdata1.astype(float), a, b, c), 'g:', label='AWD-LSTM - Exponential fit')
	plt.plot(xdata, ydata, label='AWD-LSTM - V=4')
	plt.scatter(xdata, ydata)

	xdata = np.array([2,4,6,8])
	ydata = np.array([4.6846,4.7320,4.7384,4.7385])
	plt.plot(xdata, ydata, label='Transformer XL - V=26')
	plt.scatter(xdata, ydata)

	xdata = np.array([2,4,6,8])
	ydata = np.array([4.525,4.635,4.707,4.709])
	plt.plot(xdata, ydata, label='AWD-LSTM - V=26')
	plt.scatter(xdata, ydata)

	plt.tick_params(labelsize='large', width=3)
	plt.grid(True)
	plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
	plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
	plt.legend(fontsize='large')
	ax = plt.axes()
	ax.set_ylabel('Test Perplexity in bpc', fontsize=18)
	ax.set_xlabel('k', fontsize=18)

	plt.savefig("perplexity")
	plt.show()