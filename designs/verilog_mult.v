`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 23.07.2023 06:40:02
// Design Name: 
// Module Name: verilog_mult
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


module verilog_mult(
    input [71:0] a,
    input [71:0] b,
    output [71:0] c
    );
    
//    ntt_intt_poly_mult #(.N(17), .D(32)) nipm(.a(a), .b(b), .c(c));
    ntt_flat #(.N(9), .D(8)) ni(.a(a), .b(c), .clk(0));
endmodule
