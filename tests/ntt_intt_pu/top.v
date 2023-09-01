`timescale 1ps/1ps

module top (
    input clk,
    input [271:0] tf,
    input [271:0] tf_inv,
    input [271:0] a,
    input inv,
    output [271:0] b
    );
    
    ntt_intt_pu #(.N(17), .D(32)) uut(
        .clk(clk), 
        .a(a), 
        .an(b), 
        .twiddle_factor(tf), 
        .inverse_twiddle_factor(tf_inv), 
        .inv(inv), 
        .rst(1'B0)
        );

endmodule