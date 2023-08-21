`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04.08.2023 15:47:10
// Design Name: 
// Module Name: mux_tb
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


module mux_tb();
    parameter N = 4, S = 16;
    reg [S*N-1:0] a = 64'H0123456789ABCDEF;
    reg [$clog2(S)-1:0] sel = 0;
    wire [N-1:0] s;
    
    mux #(.N(N), .S(S)) uut(.a(a), .sel(sel), .s(s));
    
    always #(10) sel = sel+1;
    initial #(200) $stop;
endmodule
