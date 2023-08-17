`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 21.07.2023 16:01:14
// Design Name: 
// Module Name: barret_multiplier
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


module barret_multiplier #(
    parameter N = 17, 
    parameter MU = 8193,
    parameter K = 13,
    parameter Q = 8191
    ) (
    input [N-1:0] a,
    input [N-1:0] b,
    output [N-1:0] p
    );
    
    reg [N-1:0] mu = MU;
    reg [N-1:0] q = Q;
    wire [2*N-1:0] z, m, temp, t, tl;
    wire test;
    
    multiplier #(.N(N)) m0(.a(a), .b(b), .p(z));
    multiplier #(.N(N)) m1(.a({0, z[2*N-1:K]}), .b(MU), .p(m));
    multiplier #(.N(N)) m2(.a({0, m[2*N-1:K]}), .b(q), .p(temp));
    
    adder #(.N(2*N)) sub0(.a(z), .b(~temp), .cin(1), .s(t));
    adder #(.N(2*N)) sub1(.a(t), .b({0, ~q}), .cin(1), .s(tl));
    
    mux_2x1 #(.N(N)) mux(.a(t[N-1:0]), .b(tl[N-1:0]), .sel(|t[2*N-1:K]), .s(p));
endmodule
