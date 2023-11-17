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
`include "designs/radix_2_intt_pe.v"
`include "designs/radix_2_ntt_pe.v"
`include "designs/radix_4_intt_pe.v"
`include "designs/radix_4_ntt_intt_pe_cell.v"
`include "designs/radix_4_ntt_pe.v"
`include "designs/twiddle_factor_generator.v"
`include "designs/verilog_mult.v"

`timescale 1ps/1ps

module radix_4_ntt_pe_tb ();
    parameter N = 17;
    reg [4*N-1+1:0] buffer;
    reg [N-1:0] a, b, tf;
    wire [N-1:0] p;
    reg inv = 1'B0;
    reg clk = 1'B0;

    integer testcase_file;
    integer actual_file;
    integer i = 0;

    reg [N-1:0] tf0, tf1, tf2;
    reg [N-1:0] a0, a1, a2, a3;
    wire [N-1:0] b0, b1, b2, b3;

    // [[4], [2, 8]]

    radix_4_ntt_pe #(.N(N)) uut(
        .a(a0),
        .b(a1),
        .c(a2),
        .d(a3),
        .tf(1),
        .an(b0),
        .bn(b1),
        .cn(b2),
        .dn(b3)
    );

    initial begin
        $dumpfile("radix_4_ntt_pe_tb.vcd");
        $dumpvars(0, radix_4_ntt_pe_tb);

        testcase_file = $fopen("./tests/radix_4_ntt_pe/testcase.txt", "r");
        actual_file = $fopen("./tests/radix_4_ntt_pe/actual.txt", "w");
    end
    
    always begin
        if (!$feof(testcase_file)) begin
            $fscanf(testcase_file, "%b\n", buffer);
            a3 = buffer[4*N-1+1:3*N+1];
            a2 = buffer[3*N-1+1:2*N+1];
            a1 = buffer[2*N-1+1:1*N+1];
            a0 = buffer[1*N-1+2:0*N+1];
            inv = buffer[0];
            #10;
            $fdisplay(actual_file,"%b%b%b%b", b3, b2, b1, b0);

        end else begin
            $finish;
            $fclose(testcase_file);
            $fclose(actual_file);
        end

        #10;
    end

    always #10 clk = ~clk;
endmodule