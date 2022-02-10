MAIN=src/main.py
PYCACHES=$(wildcard src/*/__pycache__)

all:
	pdflatex mathematical_correctness.tex
	rm *.log *.aux
	clear
	clear

open:
	evince mathematical_correctness.pdf&

clean:
	rm -rf $(PYCACHES)

run:
	python $(MAIN)

vim:
	nvim $(MAIN) src/*/*.py

git-update:
	git add Makefile README.md src/ mathematical_correctness.*
	git commit -m "update commit"
	git push origin main
