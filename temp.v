`include "designs/bit_reverse_order.v"
`include "designs/dff.v"
`include "designs/intt.v"
`include "designs/intt_4.v"
`include "designs/intt_flat.v"
`include "designs/intt_pe.v"
`include "designs/karatsuba_poly_mult.v"
`include "designs/karatsuba_poly_mult_preprocessor.v"
`include "designs/karatsuba_uint_mult.v"
`include "designs/lib"
`include "designs/lib/modred.v"
`include "designs/lib/mux_2x1.v"
`include "designs/lib/demux.v"
`include "designs/lib/adder.v"
`include "designs/lib/barret_multiplier.v"
`include "designs/lib/master_slave_dff.v"
`include "designs/lib/multiplier.v"
`include "designs/lib/counter_down.v"
`include "designs/lib/full_adder.v"
`include "designs/lib/mux.v"
`include "designs/lib/counter.v"
`include "designs/lib/modred_multiplier.v"
`include "designs/ntt.v"
`include "designs/ntt_4.v"
`include "designs/ntt_flat.v"
`include "designs/ntt_intt_poly_mult.v"
`include "designs/ntt_pe.v"
`include "designs/pe_multiplicand.v"
`include "designs/point_mult.v"
`include "designs/poly_add.v"
`include "designs/poly_add_tb.v"
`include "designs/poly_mult.v"
`include "designs/poly_mult_pe_cell.v"
`include "designs/poly_mult_systolic_array.v"
`include "designs/poly_sub.v"
`include "designs/psi_inv_table.v"
`include "designs/psi_table.v"
`include "designs/top.v"
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


module ntt_intt_tb();
    parameter N = 17, D = 128;
    
    reg clk = 0, mode = 0;
    reg [D*N-1:0] a;
    wire [D*N-1:0] b;
    wire [N-1:0] bs [D-1:0];

    genvar k;
    generate
    for (k=0;k<D;k=k+1) begin
        assign bs[k] = b[N*(k+1)-1:N*k];
    end
    endgenerate
    
    integer testcase_file;
    integer actual_file;
    integer i;

    ntt_flat #(.N(N), .D(D)) uut(.clk(clk), .a(a), .b(b));

    initial begin
        $dumpfile("ntt_intt_tb.vcd");
        $dumpvars(0, ntt_intt_tb);
        for (i=0;i<D;i=i+1) begin
            $dumpvars(1, bs[i]);
        end

        testcase_file = $fopen("./tests/ntt_intt/testcase.txt", "r");
        actual_file = $fopen("./tests/ntt_intt/actual.txt", "w");
    end

    always begin
        if (!$feof(testcase_file)) begin
            $fscanf(testcase_file, "%b\n", a);

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
