`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 19.07.2023 21:50:01
// Design Name: 
// Module Name: karatsuba_poly_mult_tb
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


module karatsuba_poly_mult_tb();
    parameter N = 8, D = 16;
    
    reg [D*N-1:0] a = 128'H01010101010101010101010101010101;
    reg [D*N-1:0] b = 128'H01010101010101010101010101010101;
    reg clk = 0;
    
    wire [(2*D-1)*N-1:0] p;
    
    karatsuba_poly_mult_preprocessor #(.D(D), .N(N)) kpm(.a(a), .b(b), .clk(clk), .p(p));
    
    always #(10) clk = ~clk;
    initial #(200) $stop;
endmodule
