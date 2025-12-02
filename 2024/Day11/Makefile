CC = gcc
CC_FLAGS = -Wall -Wextra -Wpedantic -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -ggdb
CC_LINK_FLAGS =

.PHONY: all run clean
all: run

run: build
	./target/main.o

build: src/main.c
	mkdir -p target
	$(CC) -o target/main.o src/main.c $(CC_FLAGS) $(CC_LINK_FLAGS)
	chmod u+x target/main.o

clean:
	rm -r target/*
