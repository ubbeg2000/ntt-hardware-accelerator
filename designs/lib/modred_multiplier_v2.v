`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 23.07.2023 02:47:11
// Design Name: 
// Module Name: modred_multiplier
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


module modred_multiplier_v2 #(parameter LOGQ = 17) (
    input [LOGQ:0] a,
    input [LOGQ:0] b,
    output [LOGQ-1:0] p
    );
    
    wire [2*LOGQ+1:0] prod;
    
    multiplier_signed #(.N(LOGQ+1)) multiplier(.a(a), .b(b), .p(prod));
    modred_v2 #(.LOGQ(LOGQ)) mr(.a(prod[2*LOGQ-1:0]), .s(p));
endmodule
