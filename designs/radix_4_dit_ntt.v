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

module radix_4_dit_ntt #(parameter N = 17, Q = 65537, TWOINV = 32769) (
    input signed [N-1:0] a0,
    input signed [N-1:0] a1,
    input signed [N-1:0] a2,
    input signed [N-1:0] a3,
    input signed [N-1:0] tf1,
    input signed [N-1:0] tf2,
    input signed [N-1:0] tf3,
    output [N-1:0] A0,
    output [N-1:0] A1,
    output [N-1:0] A2,
    output [N-1:0] A3
    );

    wire [N-1:0] mr1_out, mr2_out, mr3_out;
    wire [N-1:0] a0a2p, a0a2m, a1a3p, a1a3m;
    wire [N-1:0] a1a3p_temp, a1a3m_temp;

    modred_multiplier_v2 #(.LOGQ(N)) mr1(a1, tf1, mr1_out);
    modred_multiplier_v2 #(.LOGQ(N)) mr2(a2, tf2, mr2_out);
    modred_multiplier_v2 #(.LOGQ(N)) mr3(a3, tf3, mr3_out);

    modred_adder #(.LOGQ(N)) add0(.a(mr1_out), .b(mr3_out), .sub(1'B0), .s(a1a3p_temp));
    modred_adder #(.LOGQ(N)) add1(.a(mr1_out), .b(mr3_out), .sub(1'B1), .s(a1a3m_temp));
    modred_v2 #(.LOGQ(N)) mr4(.a({a1a3p_temp, 8'D0}), .s(a1a3p));
    modred_v2 #(.LOGQ(N)) mr5(.a({a1a3m_temp, 8'D0}), .s(a1a3m));
    modred_adder #(.LOGQ(N)) add2(.a(a0), .b(mr2_out), .sub(1'B0), .s(a0a2p));
    modred_adder #(.LOGQ(N)) add3(.a(a0), .b(mr2_out), .sub(1'B1), .s(a0a2m));
    
    modred_adder #(.LOGQ(N)) add4(.a(a0a2p), .b(a1a3p), .sub(1'B0), .s(A0));
    modred_adder #(.LOGQ(N)) add5(.a(a0a2p), .b(a1a3p), .sub(1'B1), .s(A1));
    modred_adder #(.LOGQ(N)) add6(.a(a0a2m), .b(a1a3m), .sub(1'B0), .s(A2));
    modred_adder #(.LOGQ(N)) add7(.a(a0a2m), .b(a1a3m), .sub(1'B1), .s(A3));
endmodule
