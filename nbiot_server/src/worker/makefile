CC = gcc
LINKER = gcc
SRC = ..
INCL = -I../include -I /usr/include -I /usr/local/include  -L /usr/local/lib -llog4cplus -lpthread
GCC_ARGS= -c -Wall -g -fPIC
CFLAGS += $(INCL)
CFLAGS += $(GCC_ARGS)
LDFLAGS = -fPIC -shared -lrt 
LIB_DIR = ../../lib
OBJ_DIR=../../build

OBJS= $(patsubst %.c,%.o, $(wildcard *.c))
LIB_NAME = $(LIB_DIR)/lib_worker_proc.so

all: $(OBJS) $(LIB_NAME)

%.o: %.c
	$(CC) $(CFLAGS) $^ -L/usr/lib64/mysql -lmysqlclient -lz -lstdc++ -lrt -o $@

$(LIB_NAME): $(OBJS) ../../lib/libconfig_file_ctrl_device.a  ../../lib/msg_queue.a
	$(LINKER) $(LDFLAGS) $^ -o $@ -L/usr/lib64/mysql -lmysqlclient -lz -lstdc++ -lrt
	@echo "@@ building $(LIB_NAME) completed"
	
clean:
	rm $(OBJS)
