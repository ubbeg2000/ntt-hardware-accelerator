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
    input [2:0] addr,
    output reg [16:0] value
    );

    always @ (addr) begin
    case (addr)
        3'B000: value = 1;
        3'B001: value = 256;
        3'B010: value = 16;
        3'B011: value = 4096;
        3'B100: value = 4;
        3'B101: value = 1024;
        3'B110: value = 64;
        3'B111: value = 16384;
    endcase
    end
endmodule

