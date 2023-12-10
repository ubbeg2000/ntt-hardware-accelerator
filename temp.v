`include "designs/bit_reverse_order.v"
`include "designs/intt.v"
`include "designs/intt_4.v"
`include "designs/intt_flat.v"
`include "designs/intt_pe.v"
`include "designs/karatsuba_negacyclic_conv.v"
`include "designs/karatsuba_poly_mult.v"
`include "designs/karatsuba_poly_mult_preprocessor.v"
`include "designs/karatsuba_uint_mult.v"
`include "designs/lib"
`include "designs/lib/modred.v"
`include "designs/lib/mux_2x1.v"
`include "designs/lib/poly_add.v"
`include "designs/lib/demux.v"
`include "designs/lib/poly_sub.v"
`include "designs/lib/adder.v"
`include "designs/lib/poly_mult.v"
`include "designs/lib/modred_adder.v"
`include "designs/lib/barret_multiplier.v"
`include "designs/lib/up_down_counter.v"
`include "designs/lib/master_slave_dff.v"
`include "designs/lib/poly_modred.v"
`include "designs/lib/multiplier.v"
`include "designs/lib/point_mult_v2.v"
`include "designs/lib/poly_add_tb.v"
`include "designs/lib/multiplier_signed.v"
`include "designs/lib/tff.v"
`include "designs/lib/counter_down.v"
`include "designs/lib/modred_v2.v"
`include "designs/lib/full_adder.v"
`include "designs/lib/mux.v"
`include "designs/lib/dff.v"
`include "designs/lib/counter.v"
`include "designs/lib/tri_state_buffer.v"
`include "designs/lib/modred_multiplier_v2.v"
`include "designs/lib/point_mult.v"
`include "designs/lib/modred_multiplier.v"
`include "designs/ntt.v"
`include "designs/ntt_4.v"
`include "designs/ntt_flat.v"
`include "designs/ntt_intt_cu.v"
`include "designs/ntt_intt_pe_cell.v"
`include "designs/ntt_intt_pe_cell_v2.v"
`include "designs/ntt_intt_poly_mult.v"
`include "designs/ntt_intt_pu.v"
`include "designs/ntt_intt_pu_v2.v"
`include "designs/ntt_pe.v"
`include "designs/pe_multiplicand.v"
`include "designs/poly_mult_mod.v"
`include "designs/poly_mult_pe_cell.v"
`include "designs/poly_mult_systolic_array.v"
`include "designs/psi_inv_table.v"
`include "designs/psi_table.v"
`include "designs/radix_16_dit_ntt.v"
`include "designs/radix_2_dif_ntt.v"
`include "designs/radix_2_dit_ntt.v"
`include "designs/radix_2_intt_pe.v"
`include "designs/radix_2_ntt_pe.v"
`include "designs/radix_4_dif_ntt.v"
`include "designs/radix_4_dit_ntt.v"
`include "designs/radix_4_intt_pe.v"
`include "designs/radix_4_ntt_intt_pe_cell.v"
`include "designs/radix_4_ntt_pe.v"
`include "designs/radix_8_dif_ntt.v"
`include "designs/radix_8_dit_ntt.v"
`include "designs/twiddle_factor_generator.v"
`include "designs/verilog_mult.v"

`timescale 1ps/1ps

module top();
    parameter N = 17;
    reg [N-1:0] tf1, tf2, tf3, tf4, tf5, tf6, tf7;
    reg [N-1:0] a0, a1, a2, a3, a4, a5, a6, a7;
    wire [N-1:0] A0, A1, A2, A3, A4, A5, A6, A7;

    radix_8_dit_ntt #(.N(17), .Q(65537)) top(
        .a0(a0),
        .a1(a1),
        .a2(a2),
        .a3(a3),
        .a4(a4),
        .a5(a5),
        .a6(a6),
        .a7(a7),
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