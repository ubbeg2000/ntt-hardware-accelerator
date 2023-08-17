`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 24.07.2023 11:58:52
// Design Name: 
// Module Name: poly_mult_systolic_array_tb
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


module poly_mult_systolic_array_tb();
    parameter D = 16, N = 16;
    
    reg [D*N-1:0] a = {D{16'D1}};
    reg [D*N-1:0] b = {D{16'D1}};
    reg clk = 0;
    
    wire [2*N*(2*D-1)-1:0] p;
    
    poly_mult_systolic_array #(.D(D), .N(N)) arr(.vert(a), .horz(b), .clk(clk), .rst(0), .p(p));
    
    always #(10) clk = ~clk;
    
    initial #((2*D+1)*10) $stop;
endmodule
