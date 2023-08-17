`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 27.07.2023 11:12:27
// Design Name: 
// Module Name: ntt_4_tb
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


module ntt_4_tb();
    reg [35:0] a = 40'H1008040201;
    wire [35:0] an;
    
    ntt_4 uut(.a(a), .an(an));
    
    initial #(100) $stop;
endmodule
