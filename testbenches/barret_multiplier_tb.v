`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 21.07.2023 16:19:42
// Design Name: 
// Module Name: barret_multiplier_tb
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


module barret_multiplier_tb();
    reg [15:0] a;
    reg [15:0] b;
    wire [15:0] p;
    
    barret_multiplier 
    #(.N(16), .MU(8193), .K(13), .Q(8191))
    bm(.a(a), .b(b), .p(p));
endmodule
