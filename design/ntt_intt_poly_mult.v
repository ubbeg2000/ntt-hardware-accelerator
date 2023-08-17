`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03.08.2023 12:43:41
// Design Name: 
// Module Name: ntt_intt_poly_mult
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


module ntt_intt_poly_mult #(parameter N = 17, D = 8) (
    input [D*N-1:0] a,
    input [D*N-1:0] b,
    output [D*N-1:0] c
    );
    
    wire [D*N-1:0] an, bn, cn;
    
    ntt #(.N(N), .D(D)) ntt0(.a(a), .an(an));
    ntt #(.N(N), .D(D)) ntt1(.a(b), .an(bn));
    point_mod_mult #(.N(N), .D(D)) mul(.a(an), .b(bn), .p(cn));
    intt #(.N(N), .D(D)) intt0(.an(cn), .a(c));
endmodule
