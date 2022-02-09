MAIN=src/main.py
PYCACHES=$(wildcard src/*/__pycache__)

clean:
	rm -rf $(PYCACHES)

run:
	python $(MAIN)

vim:
	nvim $(MAIN) src/*/*.py

git-update:
	git add Makefile README.md src/
	git commit -m "update commit"
	git push origin main
