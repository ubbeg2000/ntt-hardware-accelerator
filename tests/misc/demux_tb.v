`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 02.08.2023 10:50:15
// Design Name: 
// Module Name: demux_tb
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


module demux_tb();
    parameter N = 9;
    parameter S = 3;
    
    reg [N-1:0] a = 4'HF;
    reg [$clog2(S)-1:0] sel = 0;
    wire [S*N-1:0] s;
    
    demux #(.N(N), .S(S)) d(.a(a), .sel(sel), .s(s));
    
    always #(10) sel = sel + 1;
    initial #(100) $stop;
endmodule
