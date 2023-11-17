`timescale 1ns / 1ps

//`include "adder.v"
//`include "multiplier.v"
//`include "modred.v"
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 27.07.2023 10:52:40
// Design Name: 
// Module Name: ntt_pe
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

module radix_2_intt_pe #(parameter N = 17, Q = 65537, TWOINV = 32769) (
    input signed [N-1:0] an,
    input signed [N-1:0] bn,
    input signed [N-1:0] tf,
    output [N-1:0] a,
    output [N-1:0] b
    );
    
    assign a = ((an + bn) * TWOINV) % Q;
    assign b = ((an - bn) * tf * TWOINV) % Q;

endmodule
