# (English)
# ----------------------------------------------------------------------------|
#   Title:      Decorators                                                    |
#   Author:     Drake G. Cummings                                             |
#   Purpose:    Fiddling with the Python decorators                           |
# ----------------------------------------------------------------------------|
#   Total time spent programming:                                             |
#   1 hour(s) 42 minute(s) 03 second(s)                                       |
# ----------------------------------------------------------------------------|
#
# (Italiano)
# ----------------------------------------------------------------------------|
#   Il Titolo:  	Decoratori                                            |
#   Lo Scrittore:     	Drake G. Cummings                              	      |
#   Lo Scopo:  	 	Giocare con i decoratori di pitone             	      |
# ----------------------------------------------------------------------------|
#   Tempo totale impiegato per la programmazione:			      |
#   1 or(a/e) 42 minut(o/i) 03 second(o/i)				      |
# ----------------------------------------------------------------------------|


# (English)  The counter decorator
# (Italiano) Il decoratore del contatore
def CallCounter(func):
	def Helper(x):
		Helper.calls += 1
		return func(x)
	Helper.calls = 0
	return Helper


# (English)  The printer decorator
# (Italiano) Il decoratore dello stampatore
def ArgumentPrinter(func):
	def Helper(*args, **kwargs):
		print("--------------------------------------------")
		print(f"Calling {func.__name__} with arguments: ", end="")
		for arg in args:
			print(arg, end=" ")
		print("\n--------------------------------------------")
		return func(*args, **kwargs)
	return Helper


# (English)  Decorate the test function with the counter
# (Italiano) Decora la funzione di test con il contatore
@CallCounter
@ArgumentPrinter
def ToThePowerOfItself(x):
	return x**x


# (English)  Run if this file was ran directly
# (Italiano) Esegui se questo file e (con grave) stato eseguito direttamente
if __name__ == "__main__":
	print()
	print()
	print(f"ToThePowerOfItself has been called: {ToThePowerOfItself.calls} times")
	print()
	for i in range(10):
		print(ToThePowerOfItself(i))
		print()
	print(f"ToThePowerOfItself has been called: {ToThePowerOfItself.calls} times")
	print()
