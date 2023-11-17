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


module radix_2_ntt_pe #(parameter N = 17, Q = 65537) (
    input unsigned [N-1:0] a,
    input unsigned [N-1:0] b,
    input unsigned [N-1:0] tf,
    output unsigned [N-1:0] an,
    output unsigned [N-1:0] bn
    );

    reg unsigned [N-1:0] q = Q;
    wire unsigned [N-1:0] temp;
    wire unsigned [N-1:0] atemp;
    wire signed [N-1:0] btemp;
    // reg unsigned [N-1:0] btemp = (a - (b * tf) % q)
    
    assign temp = (b * tf) % Q;
    assign atemp = (a + temp);
    assign btemp = (a - temp);
    assign an = atemp % Q;
    assign bn = btemp < 0 ? btemp + Q : btemp;

endmodule
