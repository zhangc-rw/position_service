SRC = ..
INCL = -I $(SRC)/include -I $(SRC)/listener -I $(SRC)/worker -I /usr/local/include

GCC_ARGS= -c -Wall -g
CFLAGS += $(INCL)
CFLAGS += $(GCC_ARGS)

OBJ_DIR= ../../build
OBJS= $(patsubst %.c, $(OBJ_DIR)/%.o, $(wildcard *.c)) 

all: $(OBJS) 

$(OBJ_DIR)/%.o: %.c
	$(CC) $(CFLAGS) $^ -o $@

clean:
	rm $(OBJS)
