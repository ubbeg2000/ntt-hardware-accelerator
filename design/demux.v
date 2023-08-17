`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 02.08.2023 10:28:49
// Design Name: 
// Module Name: demux_1xn
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

module demux_1x2 #(parameter N = 2) (
    input [N-1:0] a,
    input sel,
    output [2*N-1:0] s
    );
    
    assign {s[2*N-1:N],s[N-1:0]} = sel ? {a,{N{1'B0}}} : {{N{1'B0}},a};

endmodule

module demux #(parameter N = 2, S = 2) (
    input [N-1:0] a,
    input [$clog2(S)-1:0] sel,
    output [(2**$clog2(S))*N-1:0] s
    );
    
    wire [N-1:0] demux_out [$clog2(S)-2:0][(2**$clog2(S))-1:0];
    
    genvar i, j;
    generate
    for (i = 0; i < $clog2(S); i = i+1) begin
        for (j = 0; j < 2**i; j = j+1) begin
            if (i == 0)
                demux_1x2 #(.N(N)) d(.a(a), .sel(sel[$clog2(S)-i-1]), .s({demux_out[i][2*j+1], demux_out[i][2*j]}));
            else if (i == $clog2(S)-1)
                demux_1x2 #(.N(N)) d(.a(demux_out[i-1][j]), .sel(sel[$clog2(S)-i-1]), .s(s[(2*(j+1))*N-1:2*j*N]));
            else
                demux_1x2 #(.N(N)) d(.a(demux_out[i-1][j]), .sel(sel[$clog2(S)-i-1]), .s({demux_out[i][2*j+1], demux_out[i][2*j]}));
        end
    end
    endgenerate
    
endmodule
