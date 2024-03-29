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
