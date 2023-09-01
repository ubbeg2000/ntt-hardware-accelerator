`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 13.08.2023 14:26:11
// Design Name: 
// Module Name: counter_tb
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


module counter_tb();
    parameter N = 4;
    
    reg clk = 0;
    wire [N-1:0] count;
    
    counter #(.N(N)) uut(.clk(clk), .rst(0), .count(count));
    
    always #(10) clk = ~clk; 
endmodule
