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


module ntt_intt_pu_tb();
    parameter N = 17, D = 16;
    
    reg [D*N:0] buffer;
    reg clk = 0, mode = 0;
    reg [D*N-1:0] a;
    reg inv;
    reg rst = 1'B0;
    wire [D*N-1:0] b;
    wire [N-1:0] bs [D-1:0];

    reg [N*D-1:0] tf = 272'B01000000000000000000000000100000000000010000000000000000000000001000000100000000000000000000000010000000000001000000000000000000000000100010000000000000000000000001000000000000100000000000000000000000010000001000000000000000000000000100000000000010000000000000000000000000;
    reg [N*D-1:0] tf_inv = 272'B01111111111111111011111110000000010111111111110000101110000000000001011111111111110010111110000000000101111111110000001010000000000000010111111111111110101111110000000001011111111110000010110000000000000101111111111110001011110000000000010111111110000000100000000000000000;

    genvar k;
    generate
    for (k=0;k<D;k=k+1) begin
        assign bs[k] = b[N*(k+1)-1:N*k];
    end
    endgenerate
    
    integer testcase_file;
    integer actual_file;
    integer i;

    ntt_intt_pu #(.N(N), .D(D)) uut(.clk(clk), .a(a), .an(b), .twiddle_factor(tf), .inverse_twiddle_factor(tf_inv), .inv(inv), .rst(rst));

    initial begin
        $dumpfile("ntt_intt_pu_tb.vcd");
        $dumpvars(0, ntt_intt_pu_tb);
        for (i=0;i<D;i=i+1) begin
            $dumpvars(1, bs[i]);
        end

        testcase_file = $fopen("./tests/ntt_intt_pu/testcase.txt", "r");
        actual_file = $fopen("./tests/ntt_intt_pu/actual.txt", "w");
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
