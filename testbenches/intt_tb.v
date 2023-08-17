`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 02.08.2023 14:22:19
// Design Name: 
// Module Name: intt_tb
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


module intt_tb();
    parameter N = 9;
    parameter D = 8;
    
    wire [D*N-1:0] an, a, a_out;
    wire [N-1:0] ans [D-1:0], as [D-1:0];
    
    genvar i;
    generate
    for (i = 0; i < D; i = i+1) begin
        assign a[N*(i+1)-1:N*i] = i + 1;
    end
    
    ntt #(.N(N), .D(D)) ft(.a(a), .an(an));
    intt #(.N(N), .D(D)) uut(.an(an), .a(a_out));
    
    for (i = 0; i < D; i = i+1) begin
        assign ans[i] = an[N*(i+1)-1:N*i];
        assign as[i] = a_out[N*(i+1)-1:N*i];
    end
    endgenerate
    
    initial #(100) $stop;
endmodule
