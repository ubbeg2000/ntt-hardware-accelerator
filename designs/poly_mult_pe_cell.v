`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 24.07.2023 11:26:44
// Design Name: 
// Module Name: poly_mult_pe_cell
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


module poly_mult_pe_cell #(parameter N = 4) (
    input [N-1:0] horz,
    input [N-1:0] vert,
    input [2*N-1:0] offset,
    input clk,
    input rst,
    output [N-1:0] horz_out,
    output [2*N-1:0] diag_out
    );
    
    wire [2*N-1:0] mult_out, add_out;
    
    master_slave_dff #(.N(N)) d0(.d(horz), .clk(clk), .rst(rst), .q(horz_out));
    master_slave_dff #(.N(2*N)) d1(.d(add_out), .clk(clk), .rst(rst), .q(diag_out));    
    multiplier #(.N(N)) mult(.a(vert), .b(horz), .p(mult_out));
    adder #(.N(2*N)) add(.a(mult_out), .b(offset), .cin(0), .s(add_out));
endmodule
