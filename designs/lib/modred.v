`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 22.07.2023 19:57:44
// Design Name: 
// Module Name: modred
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


module modred #(parameter LOGQ = 17) (
    input [2*LOGQ-1:0] a,
    output [LOGQ-1:0] s
    );
    
    parameter [2*LOGQ-1:0] Q = (1 << (LOGQ-1)) + 1;
    parameter K = LOGQ - 1;
    
    wire a0_cout;
    wire [LOGQ-1:0] mux_out;
    wire [LOGQ:0] t, s1;
    wire [LOGQ:0] s0;
    
//    assign s = a % 257;
    
    adder #(.N(LOGQ + 1)) a0(.a({2'B0, a[K-1:0]}), .b(~a[2*LOGQ-1:K]), .cin(1'B1), .s(t));
    adder #(.N(LOGQ + 1)) a1(.a(t), .b(~Q[LOGQ:0]), .cin(1'B1), .s(s1));
    adder #(.N(LOGQ + 1)) a2(.a(t), .b({mux_out[K-1], mux_out}), .cin(1'B0), .s(s0));
    
    mux_2x1 #(.N(LOGQ)) mux0(.a({LOGQ{1'B0}}), .b(Q[LOGQ-1:0]), .sel(t[LOGQ]), .s(mux_out));
    mux_2x1 #(.N(LOGQ)) mux1(.a(s1[LOGQ-1:0]), .b(s0[LOGQ-1:0]), .sel(s1[LOGQ]), .s(s));
    
endmodule
