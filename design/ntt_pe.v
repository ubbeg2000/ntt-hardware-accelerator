`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 27.07.2023 10:52:40
// Design Name: 
// Module Name: ntt_pe
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


module ntt_pe #(parameter N = 2) (
    input signed [N-1:0] a,
    input signed [N-1:0] b,
    input signed [N-1:0] c,
    input sub,
    output [N-1:0] s
    );
    
    wire [2*N-1:0] multp;
    wire [2*N-1:0] adds;
    wire [N-1:0] mr0out;
    
    multiplier #(.N(N)) mult(.a(b), .b(c), .p(multp));
    adder #(.N(2*N)) add(.a({0, a}), .b(sub ? ~multp : multp), .cin(sub), .s(adds));
    modred #(.LOGQ(N)) mr(.a(adds), .s(s));

//    always @(a, b, offset, sub) begin
//    if (sub == 1)
//        s = (offset - ((a * b) % 257)) % 257;
//    else
//        s = (offset + ((a * b) % 257)) % 257;
//    end
    
//    assign s = (offset + (sub ? -((a * b) % 257) : ((a * b) % 257))) % 257;
endmodule
