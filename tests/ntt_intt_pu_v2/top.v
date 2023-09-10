`timescale 1ps/1ps

module top (
    input clk,
    input [543:0] tf,
    input [543:0] tf_inv,
    input [543:0] a,
    input inv,
    output [543:0] b
    );
    
    ntt_intt_pu_v2 #(.N(17), .D(32)) uut(
        .clk(clk), 
        .a(a), 
        .an(b), 
        .twiddle_factor(tf), 
        .inverse_twiddle_factor(tf_inv), 
        .inv(inv), 
        .rst(1'B0)
        );

endmodule