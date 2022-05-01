all:
	pip3 install . --log LOG_FILE

clean:
	rm blackjack.egg-info build -rf LOG_FILE

uninstall:
	pip3 uninstall blackjack
