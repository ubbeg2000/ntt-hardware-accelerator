`timescale 1ns / 1ps

//`include "full_adder.v"
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 19.07.2023 18:10:34
// Design Name: 
// Module Name: adder
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


module adder #(parameter N = 2) (
    input [N-1:0] a,
    input [N-1:0] b,
    input cin,
    output [N-1:0] s,
    output cout
    );
    
    wire cwire[N-2:0];
    
    genvar i;
    
    generate
    for (i = 0; i < N; i = i + 1) begin
        if (i == 0)
            full_adder fa(.a(a[i]), .b(b[i]), .cin(cin), .s(s[i]), .cout(cwire[i]));
        else if (i == N - 1)
            full_adder fa(.a(a[i]), .b(b[i]), .cin(cwire[i - 1]), .s(s[i]), .cout(cout));
        else
            full_adder fa(.a(a[i]), .b(b[i]), .cin(cwire[i - 1]), .s(s[i]), .cout(cwire[i]));
    end
    endgenerate
endmodule
