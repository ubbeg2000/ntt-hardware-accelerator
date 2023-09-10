`timescale 1ps/1ps

module top (
    input clk,
    input [543:0] a,
    input [543:0] b,
    output [543:0] c
    );
    
    karatsuba_negacyclic_conv #(.N(17), .D(32)) uut(.a(a), .b(b), .clk(clk), .p(c));
    
endmodule