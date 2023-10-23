`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 22.07.2023 19:57:44
// Design Name: 
// Module Name: modred_v3
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


module modred_v2 #(parameter LOGQ = 17) (
    input [2*LOGQ-1:0] a,
    output [LOGQ-1:0] s
    );
    
    parameter [2*LOGQ-1:0] Q = (1 << (LOGQ-1)) + 1;
    parameter K = LOGQ - 1;
    
    wire [LOGQ:0] t, s_temp, m0_out;
    wire gte;
    wire pos;

    assign pos = ~t[LOGQ];
    assign gte = t[LOGQ-1] & |t[LOGQ-2:0] & pos;
    
    adder #(.N(LOGQ+1)) a0(
        .a({2'B0, a[K-1:0]}), 
        .b(~a[2*LOGQ-1:K]), 
        .cin(1'B1), 
        .s(t)
    );
    adder #(.N(LOGQ+1)) a1(
        .a(t), 
        .b({(LOGQ+1){pos}}^(Q[LOGQ:0]&{(LOGQ+1){gte|(~gte&~pos)}})), 
        .cin(pos), 
        .s(s_temp)
    );

    assign s = s_temp[LOGQ-1:0];
    
endmodule
