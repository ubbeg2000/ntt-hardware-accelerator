`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 25.07.2023 11:41:37
// Design Name: 
// Module Name: master_slave_dff
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

module master_slave_dff #(parameter N = 2) (
    input [N-1:0] d,
    input clk,
    input rst,
    output [N-1:0] q
    );
    
    wire [N-1:0] q_master;
    
    genvar i;
    generate
    for (i = 0; i < N; i = i + 1) begin
        dff master(.d(d[i]), .clk(clk), .rst(rst), .q(q_master[i]));
        dff slave(.d(q_master[i]), .clk(~clk), .rst(rst), .q(q[i]));
    end
    endgenerate
endmodule
