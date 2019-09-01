CC=gcc
CFLAGS=-Wall

get-target-temperature: get-target-temperature.c
	$(CC) -c $(FLAGS) -o $@ $^

.PHONY: clean

clean:
	rm -f get-target-temperature
