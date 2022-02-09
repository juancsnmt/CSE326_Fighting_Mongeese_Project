
vim:
	vim src/*/*.py

git-update:
	git add Makefile README.md src/
	git commit -m "update commit"
	git push origin main
