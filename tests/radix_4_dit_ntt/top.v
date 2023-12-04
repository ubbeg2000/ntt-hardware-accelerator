`timescale 1ps/1ps

module top();
    parameter N = 17;
    reg [N-1:0] tf1, tf2, tf3;
    reg [N-1:0] a0, a1, a2, a3;
    wire [N-1:0] A0, A1, A2, A3;

    radix_4_dit_ntt #(.N(17), .Q(65537)) top(
        .a0(a0),
        .a1(a1),
        .a2(a2),
        .a3(a3),
        .tf1(tf1),
        .tf2(tf2),
        .tf3(tf3),
        .A0(A0),
        .A1(A1),
        .A2(A2),
        .A3(A3)
    );
endmodule

// 1547