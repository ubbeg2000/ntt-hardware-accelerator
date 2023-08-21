`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 13.08.2023 14:22:54
// Design Name: 
// Module Name: counter
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


module counter_down #(parameter N = 2) (
    input clk,
    input rst,
    input down,
    output reg [N-1:0] count = {N{1'B1}}
    );
    
    reg [N-1:0] state; 
    initial state = {N{1'B1}};
    always @ (posedge clk) state = state - 1;
    always @ (negedge clk) count = state;
//    end
endmodule
