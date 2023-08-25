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
    input [3:0] addr,
    output reg [16:0] value
    );

    always @ (addr) begin
    case (addr)
        4'B0000: value = 1;
        4'B0001: value = 256;
        4'B0010: value = 16;
        4'B0011: value = 4096;
        4'B0100: value = 4;
        4'B0101: value = 1024;
        4'B0110: value = 64;
        4'B0111: value = 16384;
        4'B1000: value = 2;
        4'B1001: value = 512;
        4'B1010: value = 32;
        4'B1011: value = 8192;
        4'B1100: value = 8;
        4'B1101: value = 2048;
        4'B1110: value = 128;
        4'B1111: value = 32768;
    endcase
    end
endmodule

