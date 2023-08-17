`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 07.08.2023 19:54:21
// Design Name: 
// Module Name: psi_table_32_257
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module psi_table (
    input [4:0] addr,
    output reg [16:0] value
    );

    always @ (addr) begin
    case (addr)
        5'B00000: value = 1;
        5'B00001: value = 65536;
        5'B00010: value = 256;
        5'B00011: value = 65281;
        5'B00100: value = 16;
        5'B00101: value = 65521;
        5'B00110: value = 64;
        5'B00111: value = 65473;
        5'B01000: value = 4;
        5'B01001: value = 65533;
        5'B01010: value = 16;
        5'B01011: value = 65521;
        5'B01100: value = 64;
        5'B01101: value = 65473;
        5'B01110: value = 256;
        5'B01111: value = 65281;
        5'B10000: value = 2;
        5'B10001: value = 65535;
        5'B10010: value = 8;
        5'B10011: value = 65529;
        5'B10100: value = 32;
        5'B10101: value = 65505;
        5'B10110: value = 128;
        5'B10111: value = 65409;
        5'B11000: value = 512;
        5'B11001: value = 65025;
        5'B11010: value = 2048;
        5'B11011: value = 63489;
        5'B11100: value = 8192;
        5'B11101: value = 57345;
        5'B11110: value = 32768;
        5'B11111: value = 32769;
    endcase
    end
endmodule