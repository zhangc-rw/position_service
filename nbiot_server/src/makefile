LINKER = gcc
CC = gcc
export LINKER
export CC
OBJ_DIR = ../build
EXE_DIR = ../bin/
OBJS = $(OBJ_DIR)/*.o 
LIB_OBJS = ../lib/*.so ../lib/*/*.so ../lib/*.a ../lib/*/*.a
MAKE_PRE = make pre

MASTER = master
LISTENER = listener
WORKER = worker
TOOLS = tools
OP_LOG = $(TOOLS)/operation
CONFIG = $(TOOLS)/config
CONFIG_DEVICE = $(TOOLS)/config_device
DATA_SAVE = $(TOOLS)/data_save_mysql_basic
STRMATCH = $(TOOLS)/string_match
BIGSMALL = $(TOOLS)/big_small
CICULARBUF = $(TOOLS)/circular_buffer
MSGTRASFER = $(TOOLS)/message_transfer
FTPDOWNLOAD = $(TOOLS)/ftp_download
OPERATION_F = $(TOOLS)/operation_file
OPERATE_F = $(TOOLS)/operate_log_mysql
LOG = $(TOOLS)/log
SEND_MESSAGE = $(TOOLS)/send_message
SS_LOG_PRINT = $(TOOLS)/ss_log

MSG_QUEUE = $(TOOLS)/msg_queue

EXECUTABLE = nbiot
LDFLAGS = -ldl -lpthread -lssl -lcrypto -lldap60 -L../lib -L/usr/lib64/mysql -lmysqlclient -lz -lstdc++ -lrt  -L /usr/local/lib -llog4cplus -lpthread ../lib/libconfig_file_ctrl_device.a ../lib/msg_queue.a

all: $(EXECUTABLE) $(OBJS) 

$(OBJS):
	@echo "== making config_device ==" && cd $(CONFIG_DEVICE) && $(MAKE)
	@echo "== making msg_queue ==" && cd $(MSG_QUEUE) && $(MAKE)
	#@echo "== making operation_log ==" && cd $(OP_LOG) && $(MAKE)
	#@echo "== making operation_file ==" && cd $(OPERATION_F) && $(MAKE)
	#@echo "== making operate_log ==" && cd $(OPERATE_F) && $(MAKE)
	#@echo "== making log ==" && cd $(LOG) && $(MAKE)
	#@echo "== making send_message ==" && cd $(SEND_MESSAGE) && $(MAKE)
	#@echo "== making error_upload ==" && cd $(ERROR_UPLOAD) && $(MAKE)

	#@echo "== making data_save ==" && cd $(DATA_SAVE) && $(MAKE)
	#@echo "== making ftp_download ==" && cd $(FTPDOWNLOAD) && $(MAKE)	
	#@echo "== making log print obj ==" && cd $(SS_LOG_PRINT) && $(MAKE)
	#@echo "== making big_small ==" && cd $(BIGSMALL) && $(MAKE)
	#@echo "== making circular_buffer ==" && cd $(CICULARBUF) && $(MAKE)
	#@echo "== making message_transfer ==" && cd $(MSGTRASFER) && $(MAKE)	
	#@echo "== making config ==" && cd $(CONFIG) && $(MAKE) 
	#@echo "== making data_send_basic ==" && cd $(DATASENDBASIC) && $(MAKE)

	#@echo "== making string_match ==" && cd $(STRMATCH) && $(MAKE)
	#@echo "== making bandwidth_judge ==" && cd $(BANDWIDTH_JUDGE) && $(MAKE)
	
	@echo "== making listener ==" && cd $(LISTENER) && $(MAKE)
	@echo "== making worker ==" && cd $(WORKER) && $(MAKE)
	@echo "== making master ==" && cd $(MASTER) && $(MAKE) 

$(EXECUTABLE): $(OBJS) 
	@echo "== You are linking to generate final executable =="
	$(LINKER)  -o $(EXE_DIR)$@ $^ $(LDFLAGS)
	@echo "== Building completed, executable generated =="
	
clean:
	rm -f $(OBJS) $(EXE_DIR)$(EXECUTABLE) $(LIB_OBJS) ../src/listener/*.o ../src/worker/*.o ../src/tools/*/*.o