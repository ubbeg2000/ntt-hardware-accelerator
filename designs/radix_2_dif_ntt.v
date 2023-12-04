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

module radix_2_dif_ntt #(parameter N = 17, Q = 65537, TWOINV = 32769) (
    input signed [N-1:0] a0,
    input signed [N-1:0] a1,
    input signed [N-1:0] tf0,
    input signed [N-1:0] tf1,
    output [N-1:0] A0,
    output [N-1:0] A1
    );

    wire [N-1:0] a0a1p, a0a1m;
    
    modred_adder #(.LOGQ(N)) add0(.a(a0), .b(a1), .sub(1'B0), .s(a0a1p));
    modred_adder #(.LOGQ(N)) add1(.a(a0), .b({a1, 8'D0}), .sub(1'B1), .s(a0a1m));
    
    modred_multiplier_v2 #(.LOGQ(N)) mr0(a0a1p, tf0, A0);
    modred_multiplier_v2 #(.LOGQ(N)) mr1(a0a1m, tf1, A1);

endmodule
