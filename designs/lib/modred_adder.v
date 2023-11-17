`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 23.07.2023 02:47:11
// Design Name: 
// Module Name: modred_adder
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


module modred_adder #(parameter LOGQ = 17) (
    input [2*LOGQ-1:0] a,
    input [2*LOGQ-1:0] b,
    input sub,
    output [LOGQ-1:0] s
    );
    
    wire [2*LOGQ+1:0] sum;
    
    adder #(.N(2*LOGQ+1)) adder(.a(a), .b({(2*LOGQ+1){sub}}^b), .cin(sub), .s(sum));
    modred_v2 #(.LOGQ(LOGQ)) mr(.a(sum), .s(s));
endmodule
