`timescale 1ns / 1ps

//`include "adder.v"
//`include "multiplier.v"
//`include "modred.v"
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

module radix_4_intt_pe #(parameter N = 17, Q = 65537, TWOINV = 32769) (
    input signed [N-1:0] an,
    input signed [N-1:0] bn,
    input signed [N-1:0] cn,
    input signed [N-1:0] dn,
    input signed [N-1:0] tf,
    output [N-1:0] a,
    output [N-1:0] b,
    output [N-1:0] c,
    output [N-1:0] d
    );

    wire [N-1:0] ac_plus, ac_minus; 
    wire [N-1:0] bd_plus, bd_minus; 
    wire [N-1:0] ma4_out, ma5_out, ma6_out, ma7_out; 

    modred_adder #(.LOGQ(N)) ma0(.a(an), .b(cn), .sub(1'B0), .s(ac_plus));
    modred_adder #(.LOGQ(N)) ma1(.a(bn), .b(dn), .sub(1'B0), .s(bd_plus));
    modred_adder #(.LOGQ(N)) ma2(.a(an), .b(cn), .sub(1'B1), .s(ac_minus));
    modred_adder #(.LOGQ(N)) ma3(.a(bn), .b(dn), .sub(1'B1), .s(bd_minus));

    modred_adder #(.LOGQ(N)) ma4(.a(ac_plus), .b(bd_plus), .sub(1'B0), .s(ma4_out));
    modred_adder #(.LOGQ(N)) ma5(.a(ac_minus), .b({{N{1'B0}}, bd_minus} << 2), .sub(1'B1), .s(ma5_out));
    modred_adder #(.LOGQ(N)) ma6(.a(ac_plus), .b(bd_plus), .sub(1'B1), .s(ma6_out));
    modred_adder #(.LOGQ(N)) ma7(.a(ac_minus), .b({{N{1'B0}}, bd_minus} << 2), .sub(1'B0), .s(ma7_out));

    modred_multiplier #(.LOGQ(N)) m0(.a(ma4_out), .b(tf), .p(a));
    modred_multiplier #(.LOGQ(N)) m1(.a(ma5_out), .b(tf), .p(b));
    modred_multiplier #(.LOGQ(N)) m2(.a(ma6_out), .b(tf), .p(c));
    modred_multiplier #(.LOGQ(N)) m3(.a(ma7_out), .b(tf), .p(d));

endmodule
