`timescale 1ns / 1ns

//`include "ntt.v"
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 02.08.2023 12:03:27
// Design Name: 
// Module Name: ntt_tb
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

module ntt_tb();
    parameter N = 9;
    parameter D = 8;
    
    wire [D*N-1:0] a;
    wire [D*N-1:0] an;
    wire [N-1:0] ans [D-1:0];
    
    genvar i;
    generate
    for (i = 0; i < D; i = i+1) begin
        assign a[N*(i+1)-1:N*i] = 9'D1;
    end
    
    ntt #(.N(N), .D(D)) uut(.a(a), .an(an));
    
    
    for (i = 0; i < D; i = i+1) begin
        assign ans[i] = an[N*(i+1)-1:N*i];
    end
    endgenerate
    
    initial begin
        $dumpfile("ntt_tb.vcd");
        $dumpvars(0, ntt_tb);
        #(10) $finish;
    end
endmodule
