`timescale 1ps/1ps

module top();
    parameter N = 17;
    reg [N-1:0] tf1, tf2, tf3, tf4, tf5, tf6, tf7, tf8, tf9, tf10, tf11, tf12, tf13, tf14, tf15;
    reg [N-1:0] a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15;
    wire [N-1:0] A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15;

    radix_16_dit_ntt #(.N(17), .Q(65537)) top(
        .a0(a0),
        .a1(a1),
        .a2(a2),
        .a3(a3),
        .a4(a4),
        .a5(a5),
        .a6(a6),
        .a7(a7),
        .a8(a8),
        .a9(a9),
        .a10(a10),
        .a11(a11),
        .a12(a12),
        .a13(a13),
        .a14(a14),
        .a15(a15),
        .tf1(tf1),
        .tf2(tf2),
        .tf3(tf3),
        .tf4(tf4),
        .tf5(tf5),
        .tf6(tf6),
        .tf7(tf7),
        .tf8(tf8),
        .tf9(tf9),
        .tf10(tf10),
        .tf11(tf11),
        .tf12(tf12),
        .tf13(tf13),
        .tf14(tf14),
        .tf15(tf15),
        .A0(A0),
        .A1(A1),
        .A2(A2),
        .A3(A3),
        .A4(A4),
        .A5(A5),
        .A6(A6),
        .A7(A7),
        .A8(A8),
        .A9(A9),
        .A10(A10),
        .A11(A11),
        .A12(A12),
        .A13(A13),
        .A14(A14),
        .A15(A15)
    );
endmodule