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


module poly_mult #(parameter N = 2) (
    input [2*N-1:0] a,
    input [2*N-1:0] b,
    output [3*N-1:0] p
    );
    
    wire [N-1:0] inter0, inter1;
    
    multiplier #(.N(N)) m0(.a(a[2*N-1:N]), .b(b[2*N-1:N]), .p(p[3*N-1:2*N]));
    multiplier #(.N(N)) m1(.a(a[N-1:0]), .b(b[N-1:0]), .p(p[N-1:0]));
    multiplier #(.N(N)) m2(.a(a[2*N-1:N]), .b(b[N-1:0]), .p(inter0));
    multiplier #(.N(N)) m3(.a(a[N-1:0]), .b(b[2*N-1:N]), .p(inter1));
    adder #(.N(N)) a0(.a(inter0), .b(inter1), .cin(0), .s(p[2*N-1:N]));
endmodule
