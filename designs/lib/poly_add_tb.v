`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 19.07.2023 19:57:45
// Design Name: 
// Module Name: poly_add_tb
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


module poly_add_tb();
    parameter DEG = 4;
    parameter N = 4;
    
    reg [DEG*N-1:0] a = 32'HAA5F;
    reg [DEG*N-1:0] b = 32'HAA5F;
    wire [DEG*N-1:0] s;
    
    poly_add #(.D(DEG), .N(N)) padd(.a(a), .b(b), .s(s));
    
    initial #(100) $stop;
endmodule
