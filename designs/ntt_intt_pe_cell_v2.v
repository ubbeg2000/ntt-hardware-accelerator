`timescale 1ps/1ps

module ntt_intt_pe_cell_v2 #(parameter N = 17) (
    input inv,
    input sub,
    input [N-1:0] tf,
    input [N-1:0] a,
    input [N-1:0] b,
    output [N-1:0] p
    );

    wire [N-1:0] m0_out, m2_out, m3_out;
    wire [N-1:0] add0_out;
    wire [N:0] m1_out;
    wire [2*N-1:0] add1_out, m4_out;
    wire add0_cout;
    wire [2*N+1:0] mul0_out;

    mux_2x1 #(.N(N)) m0(.a(b), .b(a), .sel(sub), .s(m0_out));
    mux_2x1 #(.N(N+1)) m1(.a({1'B0, m0_out}), .b({sub&~add0_cout, add0_out}), .sel(inv), .s(m1_out));
    mux_2x1 #(.N(N)) m2(.a({{(N-1){1'B0}}, 1'B1}), .b(tf), .sel(~inv|(inv&sub)), .s(m2_out));
    mux_2x1 #(.N(N)) m3(.a(a), .b(b), .sel(sub), .s(m3_out));
    mux_2x1 #(.N(2*N)) m4(.a({{N{1'B0}}, m3_out}), .b({(2*N){1'B0}}), .sel(inv), .s(m4_out));
    
    adder #(.N(N)) add0(.a(b), .b({N{sub}}^a), .cin(sub), .s(add0_out), .cout(add0_cout));
    adder #(.N(2*N)) add1(.a({(2*N){~inv}} & {{N{1'B0}}, m3_out}), .b({(2*N){(~inv&sub)}} ^ mul0_out[2*N-1:0]), .cin(~inv&sub), .s(add1_out), .cout());

    multiplier_signed #(.N(N+1)) mul0(.a(m1_out), .b({1'B0, m2_out}), .p(mul0_out));

    modred #(.LOGQ(N)) mr0(.a(add1_out), .s(p));
endmodule