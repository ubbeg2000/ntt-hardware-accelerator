`timescale 1ps/1ps
`define N = 17

module top (
    input inv,
    input sub,
    input [17-1:0] tf,
    input [17-1:0] a,
    input [17-1:0] b,
    output [17-1:0] p
    );

    ntt_intt_pe_cell_v2 #(.N(17)) uut(.a(a), .b(b), .tf(tf), .inv(inv), .sub(sub), .p(p));
endmodule