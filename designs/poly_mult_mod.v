`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 19.07.2023 21:55:01
// Design Name: 
// Module Name: poly_mult
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


module poly_mult_mod #(parameter N = 2) (
    input [2*N-1:0] a,
    input [2*N-1:0] b,
    output [3*N-1:0] p
    );
    
    wire [2*N-1:0] inter0, inter1, c0, c1, c2;
    
    multiplier #(.N(N)) m0(.a(a[2*N-1:N]), .b(b[2*N-1:N]), .p(c0));
    multiplier #(.N(N)) m1(.a(a[N-1:0]), .b(b[N-1:0]), .p(c2));
    multiplier #(.N(N)) m2(.a(a[2*N-1:N]), .b(b[N-1:0]), .p(inter0));
    multiplier #(.N(N)) m3(.a(a[N-1:0]), .b(b[2*N-1:N]), .p(inter1));

    adder #(.N(2*N)) a0(.a(inter0), .b(inter1), .cin(1'B0), .s(c1));

    modred #(.LOGQ(N)) mr0(.a(c0), .s(p[3*N-1:2*N]));
    modred #(.LOGQ(N)) mr1(.a(c1), .s(p[2*N-1:N]));
    modred #(.LOGQ(N)) mr2(.a(c2), .s(p[N-1:0]));
endmodule
