# Makefile for Entregas Caracol Lda

CC = g++
CFLAGS = -std=c++11 -O3 -Wall
TARGET = project

all: $(TARGET)

$(TARGET): main.cpp
	$(CC) $(CFLAGS) -o $(TARGET) main.cpp -lm

clean:
	rm -f $(TARGET)
