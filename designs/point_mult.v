`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03.08.2023 11:41:24
// Design Name: 
// Module Name: point_mod_mult
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


module point_mod_mult #(parameter N = 19, D = 8) (
    input [D*N-1:0] a,
    input [D*N-1:0] b,
    output [D*N-1:0] p
    );
    
    genvar i;
    generate
    for (i = 0; i < D; i = i+1) begin
        modred_multiplier #(.LOGQ(N)) mul(
            .a(a[(i+1)*N-1:i*N]), 
            .b(b[(i+1)*N-1:i*N]), 
            .p(p[(i+1)*N-1:i*N])
            );
    end
    endgenerate
endmodule
