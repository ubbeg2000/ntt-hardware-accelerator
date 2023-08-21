`timescale 1ns / 1ps
//`include "master_slave_dff.v"
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 24.07.2023 16:58:23
// Design Name: 
// Module Name: karatsuba_poly_mult_preprocessor
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


module karatsuba_poly_mult_preprocessor #(parameter N = 4, D = 4) (
    input [D*N-1:0] a,
    input [D*N-1:0] b,
    input clk,
    output [(2*D-1)*N-1:0] p
    );
    
    wire [(D-1)*N-1:0] ab_low;
    wire [(D-1)*N-1:0] ab_mid;
    wire [(D-1)*N-1:0] ab_high;
    
    wire [D*N/2-1:0] a_mid, b_mid;
    wire [(D-1)*N-1:0] ab_mid_temp_0, ab_mid_temp_1;
    wire [(2*D-1)*N-1:0] ab_full;
    
    poly_add #(.D(D/2), .N(N)) adda(.a(a[D*N/2-1:0]), .b(a[D*N-1:D*N/2]), .s(a_mid));
    poly_add #(.D(D/2), .N(N)) addb(.a(b[D*N/2-1:0]), .b(b[D*N-1:D*N/2]), .s(b_mid));
    
    genvar i;
        
    generate
    if (D == 4) begin
        poly_mult #(.N(N)) multlow(.a(a[D*N/2-1:0]), .b(b[D*N/2-1:0]), .p(ab_low));
        poly_mult #(.N(N)) multmid(.a(a_mid), .b(b_mid), .p(ab_mid_temp_0));
        poly_mult #(.N(N)) multhigh(.a(a[D*N-1:D*N/2]), .b(b[D*N-1:D*N/2]), .p(ab_high));
    
//        for (i = 0; i < D-1; i = i + 1) begin
//            assign ab_mid[(i+1)*N-1:i*N] = ab_mid_temp_2[i*2*(N+1)+N-1:i*2*(N+1)];
//        end
    end else begin
       karatsuba_poly_mult_preprocessor #(.N(N), .D(D/2)) kpmphigh(.a(a[D*N-1:D*N/2]), .b(b[D*N-1:D*N/2]), .clk(clk), .p(ab_high));
       karatsuba_poly_mult_preprocessor #(.N(N), .D(D/2)) kpmpmid(.a(a_mid), .b(b_mid), .clk(clk), .p(ab_mid_temp_0));
       karatsuba_poly_mult_preprocessor #(.N(N), .D(D/2)) kpmplow(.a(a[D*N/2-1:0]), .b(b[D*N/2-1:0]), .clk(clk), .p(ab_low)); 
    end
    endgenerate
    
    poly_sub #(.D(D-1), .N(N)) submid1(.a(ab_mid_temp_0), .b(ab_low), .s(ab_mid_temp_1));
    poly_sub #(.D(D-1), .N(N)) submid2(.a(ab_mid_temp_1), .b(ab_high), .s(ab_mid));
    poly_add #(.D(2*D-1), .N(N)) pa_out(.a({ab_high, {(N){1'B0}}, ab_low}), .b({128'D0, ab_mid} << (D*N/2)), .s(ab_full));

    master_slave_dff #(.N((2*D-1)*N)) msdff(.d(ab_full), .rst(1'B0), .clk(clk), .q(p));
endmodule
