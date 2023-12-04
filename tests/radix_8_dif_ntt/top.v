`timescale 1ps/1ps

module top();
    parameter N = 17;
    reg [N-1:0] tf0, tf1, tf2, tf3, tf4, tf5, tf6, tf7;
    reg [N-1:0] a0, a1, a2, a3, a4, a5, a6, a7;
    wire [N-1:0] A0, A1, A2, A3, A4, A5, A6, A7;

    radix_8_dif_ntt #(.N(17), .Q(65537)) top(
        .a0(a0),
        .a1(a1),
        .a2(a2),
        .a3(a3),
        .a4(a4),
        .a5(a5),
        .a6(a6),
        .a7(a7),
        .tf0(tf0),
        .tf1(tf1),
        .tf2(tf2),
        .tf3(tf3),
        .tf4(tf4),
        .tf5(tf5),
        .tf6(tf6),
        .tf7(tf7),
        .A0(A0),
        .A1(A1),
        .A2(A2),
        .A3(A3),
        .A4(A4),
        .A5(A5),
        .A6(A6),
        .A7(A7)
    );
endmodule