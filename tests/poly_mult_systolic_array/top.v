`timescale 1ps/1ps

module top (
    input clk,
    input [135:0] a,
    input [135:0] b,
    output [135:0] c
    );
    
    poly_mult_systolic_array #(.N(17), .D(8)) uut (.horz(a), .vert(b), .clk(clk), .rst(1'B0), .p(c));
endmodule