CC = gcc
CFLAGS = -std=c99 -Wall -Werror
app.exe: main.o cdio.o functions.o
        $(CC) -o app.exe main.o cdio.o functions.o
main.o: main.c var.h
        $(CC) $(CFLAGS) -c main.c
cdio.o: cdio.c var.h
        $(CC) $(CFLAGS) -c cdio.c
functions.o: functions.c var.h
        $(CC) $(CFLAGS) -c functions.c
clean:
        rm *.o *.exe
