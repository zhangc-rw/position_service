CC = gcc
LINKER = gcc
INCL = 

GCC_ARGS= -c -Wall -g 
CFLAGS += $(INCL)
CFLAGS += $(GCC_ARGS)

LDFLAGS = -lpthread 

OBJ_DIR= ./
OBJS= $(patsubst %.c, %.o, $(wildcard *.c))  

EXECUTABLE = ./fork_test


all: $(OBJS) $(EXECUTABLE)

%.o: %.c
	$(CC) $(CFLAGS) $^ -o $@ 

$(EXECUTABLE): $(OBJS)
	$(LINKER) $(LDFLAGS) $^ -o $(EXECUTABLE)

clean:
	rm -f *.o $(EXECUTABLE)


