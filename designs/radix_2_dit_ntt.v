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

module radix_2_dit_ntt #(parameter N = 17, Q = 65537, TWOINV = 32769) (
    input signed [N-1:0] a0,
    input signed [N-1:0] a1,
    input signed [N-1:0] tf,
    output [N-1:0] A0,
    output [N-1:0] A1
    );

    wire [N-1:0] mr_out;
    modred_multiplier_v2 #(.LOGQ(N)) mr(a1, tf, mr_out);
    
    modred_adder #(.LOGQ(N)) add0(.a(a0), .b(mr_out), .sub(1'B0), .s(A0));
    modred_adder #(.LOGQ(N)) add1(.a(a0), .b(mr_out), .sub(1'B1), .s(A1));

endmodule
