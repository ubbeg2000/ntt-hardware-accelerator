`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 28.07.2023 11:13:35
// Design Name: 
// Module Name: intt_pe_tb
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


module intt_pe_tb();
    wire [8:0] s;
    
    intt_pe #(.N(9)) uut (.a(1), .b(8), .c(1), .sub(1), .s(s));
    
    initial #(100) $stop;
endmodule
