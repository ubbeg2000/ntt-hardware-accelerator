#!/bin/bash

VERILOG_COMPLIER=iverilog
VERILOG_RUNTIME=vvp
VERILOG_STANDARD=2012
TEMP_FILE_NAME=temp.v

TB=$1

CWD=$(pwd)
TOP=$(echo ./tests/$(echo $TB)_tb.v)

SOURCE_FILES=$(find designs/*)

TEMP_FILE_INCLUDES=$(for i in $SOURCE_FILES; do printf "\`include \"$i\"\n"; done)

printf "$TEMP_FILE_INCLUDES" > $TEMP_FILE_NAME
printf "\n\n" >> $TEMP_FILE_NAME
cat $TOP >> $TEMP_FILE_NAME
mkdir -p ./simulations/$TB

$VERILOG_COMPLIER -g2012 -ldesigns -v -o ./simulations/$TB/"$TB"_tb.vvp -s "$TB"_tb $TEMP_FILE_NAME > ./simulations/$TB/$TB_tb_compile.log
$VERILOG_RUNTIME -n -v ./simulations/$TB/"$TB"_tb.vvp -lxt2 > ./simulations/$TB/"$TB"_tb_sim.log
gtkwave "$(echo $TB)_tb.vcd"
rm $TEMP_FILE_NAME