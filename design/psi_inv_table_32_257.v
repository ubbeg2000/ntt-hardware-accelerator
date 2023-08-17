`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 07.08.2023 19:57:32
// Design Name: 
// Module Name: psi_inv_table_32_257
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


module psi_inv_table (
    input [2:0] addr,
    output reg [8:0] value
    );

    always @ (addr) begin
    case (addr)
        3'B000: value = 1;
        3'B001: value = 241;
        3'B010: value = 193;
        3'B011: value = 253;
        3'B100: value = 129;
        3'B101: value = 249;
        3'B110: value = 225;
        3'B111: value = 255;
    endcase
    end
endmodule