.PHONY: build deploy

b build:
	python3 build.py > README.md

d deploy:
	make build
	git add .
	git commit -m 'updated README'
	git push origin master
