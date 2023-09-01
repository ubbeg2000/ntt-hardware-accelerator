`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03.08.2023 12:46:21
// Design Name: 
// Module Name: ntt_intt_poly_mult_tb
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


module ntt_intt_poly_mult_tb();
    parameter N = 17, D = 32;
    wire [N*D-1:0] a, b, a_out, b_out;
    wire [N*D-1:0] c;
    wire [N-1:0] cs [D-1:0], as [D-1:0], bs [D-1:0];
    
    genvar i;
    generate
    for (i = 0; i < D; i = i+1) begin
        assign a[N*(i+1)-1:N*i] = i + 1;
        assign b[N*(i+1)-1:N*i] = D - i;
    end
    
    ntt #(.N(N), .D(D)) fta(.a(a), .an(a_out));
    ntt #(.N(N), .D(D)) ftb(.a(b), .an(b_out));
    ntt_intt_poly_mult #(.N(N), .D(D)) uut(.a(a), .b(b), .c(c));
    
    for (i = 0; i < D; i = i+1) begin
        assign cs[i] = c[N*(i+1)-1:N*i];
        assign as[i] = a_out[N*(i+1)-1:N*i];
        assign bs[i] = b_out[N*(i+1)-1:N*i];
    end
    endgenerate
    
    initial #(100) $stop;
endmodule
