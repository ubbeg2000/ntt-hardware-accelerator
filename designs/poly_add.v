`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 19.07.2023 19:52:51
// Design Name: 
// Module Name: poly_add
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


module poly_add #(parameter D = 2, parameter N = 2) (
    input [D*N-1:0] a,
    input [D*N-1:0] b,
    output [D*N-1:0] s
    );
    
    genvar i;
    
    generate
    for (i = 0; i < D; i = i + 1) begin
        adder #(.N(N)) add(.a(a[(i+1)*N-1:i*N]), .b(b[(i+1)*N-1:i*N]), .cin(0), .s(s[(i+1)*N-1:i*N]));
    end
    endgenerate
endmodule
