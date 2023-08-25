`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 27.07.2023 12:01:58
// Design Name: 
// Module Name: intt_pe
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


module intt_pe #(parameter N = 9) (
    input signed [N-1:0] a,
    input signed [N-1:0] b,
    input signed [N-1:0] c,
    input sub,
    output [N-1:0] s
    );
    
    wire [N:0] addout;
    wire [N-1:0] mr0out, addoutred;
    wire [2*N-1:0] multout;
    
//    always @(a, b, c, sub) begin
//    if (sub == 1)
//        s = (((a - b) % 257) * c) % 257;
//    else
//        s = (((a + b) % 257) * c) % 257;
//    end
    
    adder #(.N(N+1)) add(.a(sub ? {1'B0, b} : {1'B0, a}), .b({sub ? 1'B1 : 1'B0, sub ? ~a : b}), .cin(sub), .s(addout));
    modred #(.LOGQ(N)) mr0(.a({{(N-1){addout[N]}}, addout}), .s(addoutred));
    multiplier #(.N(N)) mult(.b(addoutred), .a(c), .p(multout));
    modred #(.LOGQ(N)) mr1(.a(multout), .s(s)); 
endmodule
