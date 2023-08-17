`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 27.07.2023 12:33:10
// Design Name: 
// Module Name: intt_4_tb
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


module intt_4_tb();
    reg [35:0] a = 40'H1008040201;
    wire [35:0] an;
    wire [35:0] aout;
    
    ntt_4 uut0(.a(a), .an(an));
    intt_4 uut(.an(an), .a(aout));
    
    initial #(100) $stop;
endmodule
