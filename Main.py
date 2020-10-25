# (English)
#-------------------------------------------------------------------------------|
#   Title:      Decorators                                                      |
#   Author:     Drake G. Cummings                                               |
#   Purpose:    Fiddling with the Python decorators                             |
#-------------------------------------------------------------------------------|
#   Total time spent programming: 0 hour(s) 0 minute(s) 0 second(s)             |
#-------------------------------------------------------------------------------|
#
# (Italiano)
#-----------------------------------------------------------------------------------------------|
#   Il Titolo:  	Decoratori                                              		|
#   Lo Scrittore:     	Drake G. Cummings                                       		|
#   Lo Scopo:  	 	Giocare con i decoratori di pitone                        		|
#-----------------------------------------------------------------------------------------------|
#   Tempo totale impiegato per la programmazione: 0 or(a/e) 0 minut(o/i) 0 second(o/i) 		|
#-----------------------------------------------------------------------------------------------|


# (English)  The counter decorator
# (Italiano) Il decoratore del contatore 
def CallCounter(func):
	def Helper(x):
		Helper.calls += 1
		return func(x)
	Helper.calls = 0
	return Helper


# (English)  Decorate the test function with the counter
# (Italiano) Decora la funzione di test con il contatore
@CallCounter
def Tester(x):
	return x**x

# (English)  Run if this file was ran directly
# (Italiano) Esegui se questo file è stato eseguito direttamente
if __name__ == "__main__":
	print(Tester.calls)
	for i in range(10):
		print(Tester(i))
	print(Tester.calls)
