`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 19.07.2023 22:28:28
// Design Name: 
// Module Name: top
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


module top(
    input [511:0] a,
    input [511:0] b,
    input clk,
    output [2031:0] p
    );
    
    karatsuba_poly_mult_preprocessor #(.N(8), .D(64)) kpm(.a(a), .b(b), .clk(clk), .p(p));
endmodule
