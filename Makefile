all:
	pip3 install .

clean:
	rm blackjack.egg-info build -rf

uninstall:
	pip3 uninstall blackjack
