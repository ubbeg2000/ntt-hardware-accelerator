`timescale 1ps/1ps

module top();
    parameter N = 17;
    reg [N-1:0] tf0, tf1;
    reg [N-1:0] a0, a1;
    wire [N-1:0] A0, A1;

    radix_2_dif_ntt #(.N(17), .Q(65537)) top(
        .a0(a0),
        .a1(a1),
        .tf0(tf0),
        .tf1(tf1),
        .A0(A0),
        .A1(A1)
    );
endmodule