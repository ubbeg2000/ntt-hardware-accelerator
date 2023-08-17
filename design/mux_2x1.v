`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 19.07.2023 18:27:50
// Design Name: 
// Module Name: mux_2x1
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


module mux_2x1 #(parameter N = 1)(
    input [N-1:0] a,
    input [N-1:0] b,
    input sel,
    output reg [N-1:0] s
    );
    
    always @(sel or a or b) begin
        case (sel)
            1'B0: s <= a;
            1'B1: s <= b;
        endcase
    end
endmodule
