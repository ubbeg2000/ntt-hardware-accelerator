`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 25.07.2023 11:43:16
// Design Name: 
// Module Name: dff
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

module dff (
    input d,
    input clk,
    input rst,
    output reg q
    );
    
    always @ (posedge clk)
    begin
     if (rst)
      q <= 0;
     else
      q <= d;
    end
endmodule

