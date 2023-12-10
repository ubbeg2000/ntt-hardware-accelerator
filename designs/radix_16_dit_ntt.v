`timescale 1ns / 1ps

//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 27.07.2023 10:52:40
// Design Name: 
// Module Name: ntt_pe
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////

module radix_16_dit_ntt #(parameter N = 17, Q = 65537, TWOINV = 32769) (
    input signed [N-1:0] a0,
    input signed [N-1:0] a1,
    input signed [N-1:0] a2,
    input signed [N-1:0] a3,
    input signed [N-1:0] a4,
    input signed [N-1:0] a5,
    input signed [N-1:0] a6,
    input signed [N-1:0] a7,
    input signed [N-1:0] a8,
    input signed [N-1:0] a9,
    input signed [N-1:0] a10,
    input signed [N-1:0] a11,
    input signed [N-1:0] a12,
    input signed [N-1:0] a13,
    input signed [N-1:0] a14,
    input signed [N-1:0] a15,
    input signed [N-1:0] tf1,
    input signed [N-1:0] tf2,
    input signed [N-1:0] tf3,
    input signed [N-1:0] tf4,
    input signed [N-1:0] tf5,
    input signed [N-1:0] tf6,
    input signed [N-1:0] tf7,
    input signed [N-1:0] tf8,
    input signed [N-1:0] tf9,
    input signed [N-1:0] tf10,
    input signed [N-1:0] tf11,
    input signed [N-1:0] tf12,
    input signed [N-1:0] tf13,
    input signed [N-1:0] tf14,
    input signed [N-1:0] tf15,
    output [N-1:0] A0,
    output [N-1:0] A1,
    output [N-1:0] A2,
    output [N-1:0] A3,
    output [N-1:0] A4,
    output [N-1:0] A5,
    output [N-1:0] A6,
    output [N-1:0] A7,
    output [N-1:0] A8,
    output [N-1:0] A9,
    output [N-1:0] A10,
    output [N-1:0] A11,
    output [N-1:0] A12,
    output [N-1:0] A13,
    output [N-1:0] A14,
    output [N-1:0] A15
    );

    wire [N-1:0] mr1_out, mr2_out, mr3_out, mr4_out, mr5_out, mr6_out, mr7_out, mr8_out;
    wire [N-1:0] mr9_out, mr10_out, mr11_out, mr12_out, mr13_out, mr14_out, mr15_out;
    
    wire [N-1:0] a0a8p, a0a8m, a2a10p, a2a10m, a4a12p, a4a12m, a6a14p, a6a14m;
    wire [N-1:0] a1a9p, a1a9m, a3a11p, a3a11m, a5a13p, a5a13m, a7a15p, a7a15m;
    wire [N-1:0] a4a12m_temp, a5a13m_temp, a6a14m_temp, a7a15m_temp;

    wire [N-1:0] a0a4pa2a6pp, a0a4pa2a6pm, a0a4ma2a6mp, a0a4ma2a6mm;
    wire [N-1:0] a1a5pa3a7pp, a1a5pa3a7pm, a1a5ma3a7mp, a1a5ma3a7mm;

    wire [N-1:0] a2a6m_temp, a3a7m_temp;
    wire [N-1:0] a1a5pa3a7pm_temp, a1a5ma3a7mp_temp, a1a5ma3a7mm_temp;

    modred_multiplier_v2 #(.LOGQ(N)) mr1(a1, tf1, mr1_out);
    modred_multiplier_v2 #(.LOGQ(N)) mr2(a2, tf2, mr2_out);
    modred_multiplier_v2 #(.LOGQ(N)) mr3(a3, tf3, mr3_out);
    modred_multiplier_v2 #(.LOGQ(N)) mr4(a4, tf4, mr4_out);
    modred_multiplier_v2 #(.LOGQ(N)) mr5(a5, tf5, mr5_out);
    modred_multiplier_v2 #(.LOGQ(N)) mr6(a6, tf6, mr6_out);
    modred_multiplier_v2 #(.LOGQ(N)) mr7(a7, tf7, mr7_out);
    modred_multiplier_v2 #(.LOGQ(N)) mr8(a8, tf8, mr8_out);
    modred_multiplier_v2 #(.LOGQ(N)) mr9(a9, tf9, mr9_out);
    modred_multiplier_v2 #(.LOGQ(N)) mr10(a10, tf10, mr10_out);
    modred_multiplier_v2 #(.LOGQ(N)) mr11(a11, tf11, mr11_out);
    modred_multiplier_v2 #(.LOGQ(N)) mr12(a12, tf12, mr12_out);
    modred_multiplier_v2 #(.LOGQ(N)) mr13(a13, tf13, mr13_out);
    modred_multiplier_v2 #(.LOGQ(N)) mr14(a14, tf14, mr14_out);
    modred_multiplier_v2 #(.LOGQ(N)) mr15(a15, tf15, mr15_out);

    modred_adder #(.LOGQ(N)) add0(.a(a0), .b(mr8_out), .sub(1'B0), .s(a0a8p));
    modred_adder #(.LOGQ(N)) add1(.a(mr2_out), .b(mr10_out), .sub(1'B0), .s(a2a10p));
    modred_adder #(.LOGQ(N)) add2(.a(mr4_out), .b(mr12_out), .sub(1'B0), .s(a4a12p));
    modred_adder #(.LOGQ(N)) add3(.a(mr6_out), .b(mr14_out), .sub(1'B0), .s(a6a14p));
    modred_adder #(.LOGQ(N)) add4(.a(a0), .b(mr8_out), .sub(1'B1), .s(a0a8m));
    modred_adder #(.LOGQ(N)) add5(.a(mr2_out), .b(mr10_out), .sub(1'B1), .s(a2a10m));
    modred_adder #(.LOGQ(N)) add6(.a(mr4_out), .b(mr12_out), .sub(1'B1), .s(a4a12m_temp));
    modred_adder #(.LOGQ(N)) add7(.a(mr6_out), .b(mr14_out), .sub(1'B1), .s(a6a14m_temp));

    modred_adder #(.LOGQ(N)) add8(.a(a1), .b(mr9_out), .sub(1'B0), .s(a1a9p));
    modred_adder #(.LOGQ(N)) add9(.a(mr3_out), .b(mr11_out), .sub(1'B0), .s(a3a11p));
    modred_adder #(.LOGQ(N)) add10(.a(mr5_out), .b(mr13_out), .sub(1'B0), .s(a5a13p));
    modred_adder #(.LOGQ(N)) add11(.a(mr7_out), .b(nmr15_out), .sub(1'B0), .s(a7a15p));
    modred_adder #(.LOGQ(N)) add12(.a(a1), .b(mr9_out), .sub(1'B1), .s(a1a9m));
    modred_adder #(.LOGQ(N)) add13(.a(mr3_out), .b(mr11_out), .sub(1'B1), .s(a3a11m));
    modred_adder #(.LOGQ(N)) add14(.a(mr5_out), .b(mr13_out), .sub(1'B1), .s(a5a13m_temp));
    modred_adder #(.LOGQ(N)) add15(.a(mr6_out), .b(mr15_out), .sub(1'B1), .s(a7a15m_temp));

    modred_v2 #(.LOGQ(N)) mr16(.a({a4a12m_temp, 8'D0}), .s(a4a12m));
    modred_v2 #(.LOGQ(N)) mr17(.a({a6a14m_temp, 8'D0}), .s(a6a14m));
    modred_v2 #(.LOGQ(N)) mr18(.a({a5a13m_temp, 8'D0}), .s(a5a13m));
    modred_v2 #(.LOGQ(N)) mr19(.a({a7a15m_temp, 8'D0}), .s(a7a15m));

    modred_adder #(.LOGQ(N)) add16(.a(a0a8p), .b(a4a12p), .sub(1'B0), .s(a0a8pa4a12pp));
    modred_adder #(.LOGQ(N)) add17(.a(a0a8p), .b(a4a12p), .sub(1'B1), .s(a0a8pa4a12pn));
    modred_adder #(.LOGQ(N)) add18(.a(a2a10p), .b(a6a14p), .sub(1'B0), .s(a2a10pa6a14pp));
    modred_adder #(.LOGQ(N)) add19(.a(a2a10p), .b(a6a14p), .sub(1'B1), .s(a2a10pa6a14pn_temp));
    modred_adder #(.LOGQ(N)) add20(.a(a1a9p), .b(a5a13p), .sub(1'B0), .s(a1a9pa5a13pp));
    modred_adder #(.LOGQ(N)) add21(.a(a1a9p), .b(a5a13p), .sub(1'B1), .s(a1a9pa5a13pn));
    modred_adder #(.LOGQ(N)) add22(.a(a3a11p), .b(a7a15p), .sub(1'B0), .s(a3a11pa7a15pp));
    modred_adder #(.LOGQ(N)) add23(.a(a3a11p), .b(a7a15p), .sub(1'B1), .s(a3a11pa7a15pn_temp));

    modred_adder #(.LOGQ(N)) add24(.a(a0a8n), .b(a4a12n), .sub(1'B0), .s(a0a8na4a12np));
    modred_adder #(.LOGQ(N)) add25(.a(a0a8n), .b(a4a12n), .sub(1'B1), .s(a0a8na4a12nn));
    modred_adder #(.LOGQ(N)) add26(.a(a2a10n), .b(a6a14n), .sub(1'B0), .s(a2a10na6a14np_temp));
    modred_adder #(.LOGQ(N)) add27(.a(a2a10n), .b(a6a14n), .sub(1'B1), .s(a2a10na6a14nn_temp));
    modred_adder #(.LOGQ(N)) add28(.a(a1a9n), .b(a5a13n), .sub(1'B0), .s(a1a9na5a13np));
    modred_adder #(.LOGQ(N)) add29(.a(a1a9n), .b(a5a13n), .sub(1'B1), .s(a1a9na5a13nn));
    modred_adder #(.LOGQ(N)) add30(.a(a3a11n), .b(a7a15n), .sub(1'B0), .s(a3a11na7a15np_temp));
    modred_adder #(.LOGQ(N)) add31(.a(a3a11n), .b(a7a15n), .sub(1'B1), .s(a3a11na7a15nn_temp));

    modred_v2 #(.LOGQ(N)) mr20(.a({a2a10pa6a14pn_temp, 8'D0}), .s(a2a10pa6a14pn));
    modred_v2 #(.LOGQ(N)) mr21(.a({a3a11pa7a15pn_temp, 8'D0}), .s(a3a11pa7a15pn));
    modred_v2 #(.LOGQ(N)) mr22(.a({a2a10na6a14np_temp, 4'D0}), .s(a2a10na6a14np));
    modred_v2 #(.LOGQ(N)) mr23(.a({a3a11na7a15np_temp, 4'D0}), .s(a3a11na7a15np));
    modred_v2 #(.LOGQ(N)) mr24(.a({a2a10na6a14nn_temp, 12'D0}), .s(a2a10na6a14nn));
    modred_v2 #(.LOGQ(N)) mr25(.a({a3a11na7a15nn_temp, 12'D0}), .s(a3a11na7a15nn));

    modred_adder #(.LOGQ(N)) add32(.a(a0a8pa4a12pp), .b(a2a10pa6a14pp), .sub(1'B0), .s(a0a8pa4a12ppa2a10pa6a14ppp));
    modred_adder #(.LOGQ(N)) add33(.a(a1a9pa5a13pp), .b(a3a11pa7a15pp), .sub(1'B0), .s(a1a9pa5a13ppa3a11pa7a15ppp));
    modred_adder #(.LOGQ(N)) add34(.a(a0a8pa4a12pp), .b(a2a10pa6a14pp), .sub(1'B1), .s(a0a8pa4a12ppa2a10pa6a14ppn));
    modred_adder #(.LOGQ(N)) add35(.a(a1a9pa5a13pp), .b(a3a11pa7a15pp), .sub(1'B1), .s(a1a9pa5a13ppa3a11pa7a15ppn_temp));
    modred_adder #(.LOGQ(N)) add36(.a(a0a8pa4a12pn), .b(a2a10pa6a14pn), .sub(1'B0), .s(a0a8pa4a12pna2a10pa6a14pnp));
    modred_adder #(.LOGQ(N)) add37(.a(a1a9pa5a13pn), .b(a3a11pa7a15pn), .sub(1'B0), .s(a1a9pa5a13pna3a11pa7a15pnp_temp));
    modred_adder #(.LOGQ(N)) add38(.a(a0a8pa4a12pn), .b(a2a10pa6a14pn), .sub(1'B1), .s(a0a8pa4a12pna2a10pa6a14pnn));
    modred_adder #(.LOGQ(N)) add39(.a(a1a9pa5a13pn), .b(a3a11pa7a15pn), .sub(1'B1), .s(a1a9pa5a13pna3a11pa7a15pnn_temp));

    modred_adder #(.LOGQ(N)) add40(.a(a0a8na4a12np), .b(a2a10na6a14np), .sub(1'B0), .s(a0a8na4a12npa2a10na6a14npp));
    modred_adder #(.LOGQ(N)) add41(.a(a1a9na5a13np), .b(a3a11na7a15np), .sub(1'B0), .s(a1a9na5a13npa3a11na7a15npp_temp));
    modred_adder #(.LOGQ(N)) add42(.a(a0a8na4a12np), .b(a2a10na6a14np), .sub(1'B1), .s(a0a8na4a12npa2a10na6a14npn));
    modred_adder #(.LOGQ(N)) add43(.a(a1a9na5a13np), .b(a3a11na7a15np), .sub(1'B1), .s(a1a9na5a13npa3a11na7a15npn_temp));
    modred_adder #(.LOGQ(N)) add44(.a(a0a8na4a12nn), .b(a2a10na6a14nn), .sub(1'B0), .s(a0a8na4a12nna2a10na6a14nnp));
    modred_adder #(.LOGQ(N)) add45(.a(a1a9na5a13nn), .b(a3a11na7a15nn), .sub(1'B0), .s(a1a9na5a13nna3a11na7a15nnp_temp));
    modred_adder #(.LOGQ(N)) add46(.a(a0a8na4a12nn), .b(a2a10na6a14nn), .sub(1'B1), .s(a0a8na4a12nna2a10na6a14nnn));
    modred_adder #(.LOGQ(N)) add47(.a(a1a9na5a13nn), .b(a3a11na7a15nn), .sub(1'B1), .s(a1a9na5a13nna3a11na7a15nnn_temp));

    modred_v2 #(.LOGQ(N)) mr26(.a({a1a9pa5a13ppa3a11pa7a15ppn_temp, 8'D0}), .s(a1a9pa5a13ppa3a11pa7a15ppn));
    modred_v2 #(.LOGQ(N)) mr27(.a({a1a9pa5a13pna3a11pa7a15pnp_temp, 4'D0}), .s(a1a9pa5a13pna3a11pa7a15pnp));
    modred_v2 #(.LOGQ(N)) mr28(.a({a1a9pa5a13pna3a11pa7a15pnn_temp, 12'D0}), .s(a1a9pa5a13pna3a11pa7a15pnn));
    modred_v2 #(.LOGQ(N)) mr29(.a({a1a9na5a13npa3a11na7a15npp_temp, 2'D0}), .s(a1a9na5a13npa3a11na7a15npp));
    modred_v2 #(.LOGQ(N)) mr30(.a({a1a9na5a13npa3a11na7a15npn_temp, 10'D0}), .s(a1a9na5a13npa3a11na7a15npn));
    modred_v2 #(.LOGQ(N)) mr31(.a({a1a9na5a13nna3a11na7a15nnp_temp, 6'D0}), .s(a1a9na5a13nna3a11na7a15nnp));
    modred_v2 #(.LOGQ(N)) mr32(.a({a1a9na5a13nna3a11na7a15nnn_temp, 14'D0}), .s(a1a9na5a13nna3a11na7a15nnn));

    modred_adder #(.LOGQ(N)) add48(
        .a(a0a8pa4a12ppa2a10pa6a14ppp), 
        .b(a1a9pa5a13ppa3a11pa7a15ppp), 
        .sub(1'B0), .s(A0)
    );
    modred_adder #(.LOGQ(N)) add49(
        .a(a0a8pa4a12ppa2a10pa6a14ppp), 
        .b(a1a9pa5a13ppa3a11pa7a15ppp), 
        .sub(1'B1), .s(A1)
    );
    modred_adder #(.LOGQ(N)) add50(
        .a(a0a8pa4a12ppa2a10pa6a14ppn), 
        .b(a1a9pa5a13ppa3a11pa7a15ppn), 
        .sub(1'B0), .s(A2)
    );
    modred_adder #(.LOGQ(N)) add51(
        .a(a0a8pa4a12ppa2a10pa6a14ppn), 
        .b(a1a9pa5a13ppa3a11pa7a15ppn), 
        .sub(1'B1), .s(A3)
    );
    modred_adder #(.LOGQ(N)) add52(
        .a(a0a8pa4a12pna2a10pa6a14pnp), 
        .b(a1a9pa5a13pna3a11pa7a15pnp), 
        .sub(1'B0), .s(A4)
    );
    modred_adder #(.LOGQ(N)) add53(
        .a(a0a8pa4a12pna2a10pa6a14pnp), 
        .b(a1a9pa5a13pna3a11pa7a15pnp), 
        .sub(1'B1), .s(A5)
    );
    modred_adder #(.LOGQ(N)) add54(
        .a(a0a8pa4a12pna2a10pa6a14pnn), 
        .b(a1a9pa5a13pna3a11pa7a15pnn), 
        .sub(1'B0), .s(A6)
    );
    modred_adder #(.LOGQ(N)) add55(
        .a(a0a8pa4a12pna2a10pa6a14pnn), 
        .b(a1a9pa5a13pna3a11pa7a15pnn), 
        .sub(1'B1), .s(A7)
    );

    modred_adder #(.LOGQ(N)) add56(
        .a(a0a8na4a12npa2a10na6a14npp), 
        .b(a1a9na5a13npa3a11na7a15npp), 
        .sub(1'B0), .s(A8)
    );
    modred_adder #(.LOGQ(N)) add57(
        .a(a0a8na4a12npa2a10na6a14npp), 
        .b(a1a9na5a13npa3a11na7a15npp), 
        .sub(1'B1), .s(A9)
    );
    modred_adder #(.LOGQ(N)) add58(
        .a(a0a8na4a12npa2a10na6a14npn), 
        .b(a1a9na5a13npa3a11na7a15npn), 
        .sub(1'B0), .s(A10)
    );
    modred_adder #(.LOGQ(N)) add59(
        .a(a0a8na4a12npa2a10na6a14npn), 
        .b(a1a9na5a13npa3a11na7a15npn), 
        .sub(1'B1), .s(A11)
    );
    modred_adder #(.LOGQ(N)) add60(
        .a(a0a8na4a12nna2a10na6a14nnp), 
        .b(a1a9na5a13nna3a11na7a15nnp), 
        .sub(1'B0), .s(A12)
    );
    modred_adder #(.LOGQ(N)) add61(
        .a(a0a8na4a12nna2a10na6a14nnp), 
        .b(a1a9na5a13nna3a11na7a15nnp), 
        .sub(1'B1), .s(A13)
    );
    modred_adder #(.LOGQ(N)) add62(
        .a(a0a8na4a12nna2a10na6a14nnn), 
        .b(a1a9na5a13nna3a11na7a15nnn), 
        .sub(1'B0), .s(A14)
    );
    modred_adder #(.LOGQ(N)) add63(
        .a(a0a8na4a12nna2a10na6a14nnn), 
        .b(a1a9na5a13nna3a11na7a15nnn), 
        .sub(1'B1), .s(A15)
    );
endmodule
