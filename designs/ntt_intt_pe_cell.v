`timescale 1ps/1ps

module ntt_intt_pe_cell #(parameter N = 17) (
    input [N-1:0] a,
    input [N-1:0] b,
    input [N-1:0] tf,
    input [N-1:0] q,
    input inv,
    input sub,
    output [N-1:0] p
    );

    wire [2*N-1:0] a_mul_tf, b_mul_tf, add_out;
    wire [N-1:0] atf;

    mux_2x1 #(.N(N)) m(.a({{(N-1){1'B0}}, 1'B1}), .b(tf), .sel(inv), .s(atf));

    multiplier #(.N(N)) mul0(.a(a), .b(atf), .p(a_mul_tf));
    multiplier #(.N(N)) mul1(.a(b), .b(tf), .p(b_mul_tf));

    adder #(.N(2*N)) add(.a(a_mul_tf), .b(b_mul_tf ^ {2*N{sub}}), .cin(sub), .s(add_out));
    modred #(.LOGQ(N)) mr(.a(add_out), .s(p));
endmodule