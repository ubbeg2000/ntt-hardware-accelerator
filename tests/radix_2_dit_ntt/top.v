`timescale 1ps/1ps

module top();
    parameter N = 17;
    reg [N-1:0] tf;
    reg [N-1:0] a0, a1;
    wire [N-1:0] A0, A1;

    radix_2_dit_ntt #(.N(17), .Q(65537)) top(
        .a0(a0),
        .a1(a1),
        .tf(tf),
        .A0(A0),
        .A1(A1)
    );
endmodule