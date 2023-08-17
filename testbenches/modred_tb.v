`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 22.07.2023 20:07:40
// Design Name: 
// Module Name: modred_tb
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


module modred_tb();
    parameter LOGQ = 17;
    parameter Q = 65537;
    
    reg [2*LOGQ-1:0] a = 2;
    wire [LOGQ-1:0] s;
    
    modred #(.LOGQ(LOGQ)) m(.a(a), .s(s));
endmodule
