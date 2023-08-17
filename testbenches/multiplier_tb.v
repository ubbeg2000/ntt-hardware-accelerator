`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 19.07.2023 19:34:39
// Design Name: 
// Module Name: multiplier_tb
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


module multiplier_tb();
    parameter N = 4;
    
    reg [N-1:0] a = 0;
    reg [N-1:0] b = 0;
    wire [2*N-1:0] p;
    
    multiplier #(.N(N)) uut(.a(a), .b(b), .p(p));
    
    always #(1) a = a + 1;
    always #(1 * (1 << N)) b = b + 1;
    
    initial begin
        #(10 * (2 << N)) $stop;
    end
endmodule
