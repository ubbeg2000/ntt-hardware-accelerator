`timescale 1ns / 1ps
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
    parameter N = 65537, D = 16;
    
    reg clk = 0, mode = 1;
    wire [D*N-1:0] a;
    wire [D*N-1:0] b;
    wire [N-1:0] bs [D-1:0];
    
    reg [N-1:0] val [D-1:0];
//    initial begin
//    val[7] = 4;
//    val[6] = 87;
//    val[5] = 143;
//    val[4] = 220;
//    val[3] = 39;
//    val[2] = 116;
//    val[1] = 172;
//    val[0] = 255;
//    end
    
    genvar i;
    generate
    for (i = 0; i < D; i = i+1) begin
        assign a[N*(i+1)-1:N*i] = 1;// val[i];
        assign bs[i] = b[N*(i+1)-1:N*i];
    end
    endgenerate
    
    intt_flat #(.N(N), .D(D)) uut(.clk(clk), .a(a), .b(b));

    always #(10) clk = ~clk;
endmodule
