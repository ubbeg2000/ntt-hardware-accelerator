`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 25.07.2023 13:34:43
// Design Name: 
// Module Name: karatsuba_uint_mult_tb
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


module karatsuba_uint_mult_tb();
    parameter N = 8;
    integer a = 16;
    integer b = 13;
    wire [2*N-1:0] p;
    
    karatsuba_uint_mult #(.N(N)) uut(.a(a), .b(b), .p(p));
    
    initial #(100) $stop;
endmodule
