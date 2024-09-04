.PHONY: all cpp go python clean

all: cpp go python

cpp: c++/main

c++/main: c++/main.cpp
	@g++ -std=c++11 -I/opt/homebrew/Cellar/gmp/6.3.0/include c++/main.cpp -o c++/main -L/opt/homebrew/Cellar/gmp/6.3.0/lib -lgmp
	@echo "Running C++ program:"
	@./c++/main

go: golang/cmd/main

golang/cmd/main: golang/cmd/math.go
	@echo "Compiling Go program:"
	@cd golang/cmd && go build -o main math.go
	@echo "Running Go program:"
	@golang/cmd/./main

python: python/test.py
	@echo "Running Python program:"
	@python3 python/test.py

clean:
	@rm -f c++/main golang/cmd/main
