`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04.08.2023 15:37:03
// Design Name: 
// Module Name: mux
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


module mux #(parameter N = 64, S = 64) (
    input [(2**$clog2(S))*N-1:0] a,
    input [$clog2(S)-1:0] sel,
    output [N-1:0] s
    );
    
    wire [N-1:0] mux_out [$clog2(S)-1:0][(2**$clog2(S))-1:0];
    
    genvar i, j;
    generate
    for (i = $clog2(S) - 1; i > -1; i = i-1) begin
        for (j = 0; j < 2**i; j = j+1) begin
            if (i == 0)
                mux_2x1 #(.N(N)) m(.a(mux_out[i+1][2*j]), .b(mux_out[i+1][2*j+1]), .sel(sel[$clog2(S)-i-1]), .s(s));
            else if (i == $clog2(S) - 1)
                mux_2x1 #(.N(N)) m(.a(a[N*(2*j+1):N*2*j]), .b(a[N*(2*j+2)-1:N*(2*j+1)]), .sel(sel[$clog2(S)-i-1]), .s(mux_out[i][j]));
            else
                mux_2x1 #(.N(N)) m(.a(mux_out[i+1][2*j]), .b(mux_out[i+1][2*j+1]), .sel(sel[$clog2(S)-i-1]), .s(mux_out[i][j]));
        end
    end
    endgenerate
endmodule
