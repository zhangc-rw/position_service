CC = gcc
LINKER = gcc
SRC = ../..
INCL = -I $(SRC)/include
GCC_ARGS= -c -Wall -g -fPIC 
GCC_ARRCGS= -c -Wall -g 
CFLAGS += $(INCL)
CFLAGS += $(GCC_ARGS)
CFARLAGS += $(GCC_ARRCGS)
LDFLAGS = -fPIC -shared -lpthread
ARFLAGS = ar -rc 
LIB_DIR = ../../../lib

OBJS= $(patsubst %.c, %.o, $(wildcard *.c))
LIB_NAME = $(LIB_DIR)/libconfig_file_ctrl_device.a

all: $(OBJS) $(LIB_NAME)

%.o: %.c
	$(CC) $(CFARLAGS) $(CFLAGS) $^ -o $@ 


$(LIB_NAME): $(OBJS)
	$(ARFLAGS) $@ $^
	@echo "@@ building $(LIB_NAME) completed"


clean:
	rm $(LIB_NAME) $(OBJS)