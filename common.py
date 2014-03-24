from termprint import *

info, err, warn = "INFO", "ERROR", "WARNING"

def printobj(obj):
	"""Prints the objects instancemethods and """
	for o in dir(obj):
		try:
			termprint(warn, '- %s (%s)' % (o, type(getattr(obj, o))))
		except AttributeError:
			termprint(warn, '- %s ---' % (o))
	termprint(info, 'WE GOOD...')
