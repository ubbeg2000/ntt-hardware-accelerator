`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 19.07.2023 20:13:59
// Design Name: 
// Module Name: karatsuba_poly_mult
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


module karatsuba_poly_mult #(parameter N = 2, D = 4) (
    input [D*N-1:0] a,
    input [D*N-1:0] b,
    output [(2*D-1)*2*N-1:0] p
    );
    
//    parameter N_OUT = 2*N;
//    wire [N_OUT-1:0] a_mid, b_mid;
//    wire [3*N_OUT-1:0] ab_high, ab_low, ab_mid, ab_low_high, ab_new_mid;
    
//    poly_add #(.DEG(2), .N(N)) pa_a_mid(.a(a[4*N-1:2*N]), .b(a[2*N-1:0]), .s(a_mid));
//    poly_add #(.DEG(2), .N(N)) pa_b_mid(.a(b[4*N-1:2*N]), .b(b[2*N-1:0]), .s(b_mid));
//    poly_add #(.DEG(3), .N(N_OUT)) pa_ab(.a(ab_low), .b(ab_high), .s(ab_low_high));
//    poly_sub #(.DEG(3), .N(N_OUT)) pa_ab_mid(.a(ab_mid), .b(ab_low_high), .s(ab_new_mid));
    
//    poly_mult #(.N(N)) pm_high(.a(a[4*N-1:2*N]), .b(b[4*N-1:2*N]), .p(ab_high));
//    poly_mult #(.N(N)) pm_low(.a(a[2*N-1:0]), .b(b[2*N-1:0]), .p(ab_low));
//    poly_mult #(.N(N)) pm_mid(.a(a_mid), .b(b_mid), .p(ab_mid));
    
//    poly_add #(.DEG(7), .N(N_OUT)) pa_out(.a({ab_high, {N_OUT{1'B0}}, ab_low}), .b({0, ab_new_mid} << (2*N_OUT)), .s(p));

    karatsuba_poly_mult_preprocessor #(.N(N), .D(D)) kpmp(.a(a), .b(b), .p(p));
endmodule
