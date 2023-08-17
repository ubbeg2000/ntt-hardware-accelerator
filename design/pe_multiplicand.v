`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 11.08.2023 12:05:08
// Design Name: 
// Module Name: pe_multiplicand
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


module pe_multiplicand #(parameter N = 17, D = 32) (
    input [$clog2(D)-1:0] power,
    input inv,
    output [N-1:0] psi
    );
    
    wire [N-1:0] p, p_inv;
    
    psi_table pt(.addr(power), .value(p));
    psi_inv_table pit(.addr(power), .value(p_inv));
    mux_2x1 #(.N(N)) m(.a(p), .b(p_inv), .sel(inv), .s(psi));
endmodule
