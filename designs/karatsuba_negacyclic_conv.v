`timescale 1ps/1ps

module karatsuba_negacyclic_conv #(parameter N = 17, D = 32) (
    input [D*N-1:0] a,
    input [D*N-1:0] b,
    output [D*N-1:0] p,
    input clk
    );

    wire [(2*D-1)*N-1:0] temp;
    wire [D*N-1:0] temp2;

    karatsuba_poly_mult_preprocessor #(.N(N), .D(D)) pm(.a(a), .b(b), .p(temp), .clk(clk));
    poly_sub #(.N(N), .D(D)) ps(.a(temp[D*N-1:0]), .b({{N{1'B0}}, temp[(2*D-1)*N-1:D*N]}), .s(temp2));
    poly_modred #(.N(N), .D(D)) pmr(.a(temp2), .b(p));
    
endmodule