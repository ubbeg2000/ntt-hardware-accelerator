`timescale 1ps/1ps

module radix_4_ntt_intt_pe_cell #(parameter N = 17) (
    input inv,
    input [N-1:0] a0,
    input [N-1:0] a1,
    input [N-1:0] a2,
    input [N-1:0] a3,
    input [N-1:0] tf0,
    input [N-1:0] tf1,
    input [N-1:0] tf2,
    output [N-1:0] b0,
    output [N-1:0] b1,
    output [N-1:0] b2,
    output [N-1:0] b3
    );

    wire add0_cout, add1_cout, add2_cout, add3_cout;
    wire add4_cout, add5_cout, add6_cout, add7_cout;
    wire [N-1:0] add0_out, add1_out, add2_out, add3_out;
    wire [N-1:0] add0_mr_out, add1_mr_out, add2_mr_out, add3_mr_out;
    wire [N-1:0] add4_out, add5_out, add6_out, add7_out;
    wire [N-1:0] mux0_out, mux1_out, mux2_out, mux3_out;
    wire [N:0] mul_out, mul0_out, mul1_out, mul2_out, mul3_out;

    modred_multiplier_v2 #(.LOGQ(N)) mul(.a({1'B0, a1}), .b({1'B0, tf2}), .p(mul0_out[N-1:0]));
    modred_multiplier_v2 #(.LOGQ(N)) mul0(.a({1'B0, a3}), .b({1'B0, tf1}), .p(mul0_out[N-1:0]));
    modred_multiplier_v2 #(.LOGQ(N)) mul1(.a({1'B0, a1}), .b({1'B0, tf1}), .p(mul1_out[N-1:0]));
    modred_multiplier_v2 #(.LOGQ(N)) mul2(.a({1'B0, a2}), .b({1'B0, tf0}), .p(mul2_out[N-1:0]));
    modred_multiplier_v2 #(.LOGQ(N)) mul3(.a({1'B0, a3}), .b({1'B0, tf2}), .p(mul3_out[N-1:0]));

    adder #(.N(N)) add0(.a(a0), .b(mul2_out[N-1:0]), .cin(1'B0), .s(add0_out), .cout(add0_cout));
    adder #(.N(N)) add1(.a(a0), .b(~mul2_out[N-1:0]), .cin(1'B1), .s(add1_out), .cout(add1_cout));
    adder #(.N(N)) add2(.a(mul1_out[N-1:0]), .b(mul0_out[N-1:0]), .cin(1'B0), .s(add2_out), .cout(add2_cout));
    adder #(.N(N)) add3(.a(mul_out[N-1:0]), .b(~mul3_out[N-1:0]), .cin(1'B1), .s(add3_out), .cout(add3_cout));

    // mux_2x1 #(.N(N)) mux0(.a({{(N-1){1'B0}}, 1'B1}), .b(tf0), .sel(inv), .s(mux0_out));
    // mux_2x1 #(.N(N)) mux1(.a(tf0), .b({{(N-1){1'B0}}, 1'B1}), .sel(inv), .s(mux1_out));
    // mux_2x1 #(.N(N)) mux2(.a(tf0), .b(tf1), .sel(inv), .s(mux2_out));

    modred_multiplier_v2 #(.LOGQ(N)) mr0(.a({~add0_cout, add0_out}), .b(18'D1), .p(add0_mr_out));
    modred_multiplier_v2 #(.LOGQ(N)) mr1(.a({~add1_cout, add1_out}), .b(18'D1), .p(add1_mr_out));
    modred_multiplier_v2 #(.LOGQ(N)) mr2(.a({~add2_cout, add2_out}), .b(18'D1), .p(add2_mr_out));
    modred_multiplier_v2 #(.LOGQ(N)) mr3(.a({~add3_cout, add3_out}), .b(18'D1), .p(add3_mr_out));

    // modred_multiplier_v2 #(.LOGQ(N)) mul4(.a({1'B0, add1_mr_out}), .b({1'B0, tf1}), .p(mul2_out[N-1:0]));
    // modred_multiplier_v2 #(.LOGQ(N)) mul5(.a({1'B0, add3_mr_out}), .b({1'B0, tf2}), .p(mul3_out[N-1:0]));
    
    adder #(.N(N)) add4(.a(add0_mr_out[N-1:0]), .b(add2_mr_out[N-1:0]), .cin(1'B0), .s(add4_out), .cout(add4_cout));
    adder #(.N(N)) add5(.a(add0_mr_out[N-1:0]), .b(~add2_mr_out[N-1:0]), .cin(1'B1), .s(add5_out), .cout(add5_cout));
    adder #(.N(N)) add6(.a(add1_mr_out[N-1:0]), .b(add3_mr_out[N-1:0]), .cin(1'B0), .s(add6_out), .cout(add6_cout));
    adder #(.N(N)) add7(.a(add1_mr_out[N-1:0]), .b(~add3_mr_out[N-1:0]), .cin(1'B1), .s(add7_out), .cout(add7_cout));

    modred_multiplier_v2 #(.LOGQ(N)) mr4(.a({~add4_cout, add4_out}), .b(18'D1), .p(b0));
    modred_multiplier_v2 #(.LOGQ(N)) mr5(.a({~add5_cout, add5_out}), .b(18'D1), .p(b1));
    modred_multiplier_v2 #(.LOGQ(N)) mr6(.a({~add6_cout, add6_out}), .b(18'D1), .p(b2));
    modred_multiplier_v2 #(.LOGQ(N)) mr7(.a({~add7_cout, add7_out}), .b(18'D1), .p(b3));

    // mux_2x1 #(.N(N)) mux3(.a(tf1), .b({{(N-1){1'B0}}, 1'B1}), .sel(inv), .s(mux3_out));

    
endmodule