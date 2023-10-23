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
`include "designs/radix_4_ntt_intt_pe_cell.v"
`include "designs/twiddle_factor_generator.v"
`include "designs/verilog_mult.v"

`timescale 1ns / 100ps

// `include "designs/ntt_intt.v"
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 11.08.2023 14:55:22
// Design Name: 
// Module Name: ntt_intt_tb
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


module ntt_intt_pu_v2_tb();
    parameter N = 17, D = 32;
    
    reg [D*N:0] buffer;
    reg clk = 0, mode = 0;
    reg [D*N-1:0] a;
    reg inv;
    reg rst = 1'B0;
    wire [D*N-1:0] b;
    wire [N-1:0] bs [D-1:0];

    reg [N*D-1:0] tf = 544'B0010100001000111101111000110010001011111101000000110000010001000101100000110110100011010110011111110010011011101001010100000000000011011001111010101110110010100111011101101110001100111010000000000111100110111001010001001100100110011100011001111110000100010000000000000001100111000000110000011111011001100010101010011010110000000001011011001010101111001101110111001101010100100111101000110010000000000000010010001010001110100100001101111101001001001011101111100000000000101000101111011100000111000011001101000010110101001011000100000000000000000;
    reg [N*D-1:0] tf_inv = 544'B0101011010111100101001010010001010011011000101111000110101011110110001110001100010011011111111011111000100100110011100001010111101101001000011001001110110001110001101010101001111010010101010000101010001010111110111010010001111101101010100000101100111100110001010101010101100000100001101001010111101100111010100010100011001001000000111000010010101001001101110111111100111001001011100110100111000001110001110010010010111011000101010101001111111011011011101111100100011111100111001111001011101010011110001111110100100001101101100100000000000000000;

    genvar k;
    generate
    for (k=0;k<D;k=k+1) begin
        assign bs[k] = b[N*(k+1)-1:N*k];
    end
    endgenerate
    
    integer testcase_file;
    integer actual_file;
    integer i;

    ntt_intt_pu_v2 #(.N(N), .D(D)) uut(.clk(clk), .a(a), .an(b), .twiddle_factor(tf), .inverse_twiddle_factor(tf_inv), .inv(inv), .rst(rst));

    initial begin
        $dumpfile("ntt_intt_pu_v2_tb.vcd");
        $dumpvars(0, ntt_intt_pu_v2_tb);
        for (i=0;i<D;i=i+1) begin
            $dumpvars(1, bs[i]);
        end

        testcase_file = $fopen("./tests/ntt_intt_pu_v2/testcase.txt", "r");
        actual_file = $fopen("./tests/ntt_intt_pu_v2/actual.txt", "w");
    end

    always begin
        if (!$feof(testcase_file)) begin
            $fscanf(testcase_file, "%b\n", buffer);
            a = buffer[D*N:1];
            inv = buffer[0];

            for (i=0;i<D;i=i+1) begin
                #10;
                if (i==D-1) begin
                    $fdisplay(actual_file,"%b", b);
                end
            end

        end else begin
            $finish;
            $fclose(testcase_file);
            $fclose(actual_file);
        end

    end

    always #10 clk = ~clk;
endmodule
