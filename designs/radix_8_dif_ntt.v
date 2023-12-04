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

module radix_8_dif_ntt #(parameter N = 17, Q = 65537, TWOINV = 32769) (
    input signed [N-1:0] a0,
    input signed [N-1:0] a1,
    input signed [N-1:0] a2,
    input signed [N-1:0] a3,
    input signed [N-1:0] a4,
    input signed [N-1:0] a5,
    input signed [N-1:0] a6,
    input signed [N-1:0] a7,
    input signed [N-1:0] tf0,
    input signed [N-1:0] tf1,
    input signed [N-1:0] tf2,
    input signed [N-1:0] tf3,
    input signed [N-1:0] tf4,
    input signed [N-1:0] tf5,
    input signed [N-1:0] tf6,
    input signed [N-1:0] tf7,
    output [N-1:0] A0,
    output [N-1:0] A1,
    output [N-1:0] A2,
    output [N-1:0] A3,
    output [N-1:0] A4,
    output [N-1:0] A5,
    output [N-1:0] A6,
    output [N-1:0] A7
    );
    
    wire [N-1:0] a0a4p, a0a4m, a2a6p, a2a6m, a1a5p, a1a5m, a3a7p, a3a7m;
    wire [N-1:0] a0a4pa2a6pp, a0a4pa2a6pm, a0a4ma2a6mp, a0a4ma2a6mm;
    wire [N-1:0] a1a5pa3a7pp, a1a5pa3a7pm, a1a5ma3a7mp, a1a5ma3a7mm;

    modred_adder #(.LOGQ(N)) add2(.a(a0), .b({a4, 8'D0}), .sub(1'B0), .s(a0a4p));
    modred_adder #(.LOGQ(N)) add3(.a(a0), .b({a4, 8'D0}), .sub(1'B1), .s(a0a4m));
    modred_adder #(.LOGQ(N)) add4(.a(a1), .b({a5, 8'D0}), .sub(1'B0), .s(a1a5p));
    modred_adder #(.LOGQ(N)) add5(.a(a1), .b({a5, 8'D0}), .sub(1'B1), .s(a1a5m));
    modred_adder #(.LOGQ(N)) add6(.a(a2), .b({a6, 8'D0}), .sub(1'B0), .s(a2a6p));
    modred_adder #(.LOGQ(N)) add0(.a(a2), .b({a6, 8'D0}), .sub(1'B1), .s(a2a6m));
    modred_adder #(.LOGQ(N)) add7(.a(a3), .b({a7, 8'D0}), .sub(1'B0), .s(a3a7p));
    modred_adder #(.LOGQ(N)) add1(.a(a3), .b({a7, 8'D0}), .sub(1'B1), .s(a3a7m));

    modred_adder #(.LOGQ(N)) add8(.a(a1a5p), .b({a3a7p, 4'D0}), .sub(1'B1), .s(a1a5pa3a7pm));
    modred_adder #(.LOGQ(N)) add9(.a(a1a5m), .b({a3a7m, 4'D0}), .sub(1'B0), .s(a1a5ma3a7mp));
    modred_adder #(.LOGQ(N)) add10(.a(a1a5m), .b({a3a7m, 4'D0}), .sub(1'B1), .s(a1a5ma3a7mm));
    modred_adder #(.LOGQ(N)) add11(.a(a0a4p), .b({a2a6p, 4'D0}), .sub(1'B0), .s(a0a4pa2a6pp));
    modred_adder #(.LOGQ(N)) add12(.a(a0a4p), .b({a2a6p, 12'D0}), .sub(1'B1), .s(a0a4pa2a6pm));
    modred_adder #(.LOGQ(N)) add13(.a(a0a4m), .b({a2a6m, 12'D0}), .sub(1'B0), .s(a0a4ma2a6mp));
    modred_adder #(.LOGQ(N)) add14(.a(a0a4m), .b({a2a6m, 12'D0}), .sub(1'B1), .s(a0a4ma2a6mm));
    modred_adder #(.LOGQ(N)) add15(.a(a1a5p), .b({a3a7p, 12'D0}), .sub(1'B0), .s(a1a5pa3a7pp));
    
    modred_adder #(.LOGQ(N)) add16(.a(a0a4pa2a6pp), .b({a1a5pa3a7pp, 2'D0}), .sub(1'B0), .s(A0_temp));
    modred_adder #(.LOGQ(N)) add17(.a(a0a4pa2a6pp), .b({a1a5pa3a7pp, 2'D0}), .sub(1'B1), .s(A1_temp));
    modred_adder #(.LOGQ(N)) add18(.a(a0a4pa2a6pm), .b({a1a5pa3a7pm, 6'D0}), .sub(1'B0), .s(A2_temp));
    modred_adder #(.LOGQ(N)) add19(.a(a0a4pa2a6pm), .b({a1a5pa3a7pm, 6'D0}), .sub(1'B1), .s(A3_temp));
    modred_adder #(.LOGQ(N)) add20(.a(a0a4ma2a6mp), .b({a1a5ma3a7mp, 10'D0}), .sub(1'B0), .s(A4_temp));
    modred_adder #(.LOGQ(N)) add21(.a(a0a4ma2a6mp), .b({a1a5ma3a7mp, 10'D0}), .sub(1'B1), .s(A5_temp));
    modred_adder #(.LOGQ(N)) add22(.a(a0a4ma2a6mm), .b({a1a5ma3a7mm, 14'D0}), .sub(1'B0), .s(A6_temp));
    modred_adder #(.LOGQ(N)) add23(.a(a0a4ma2a6mm), .b({a1a5ma3a7mm, 14'D0}), .sub(1'B1), .s(A7_temp));

    modred_multiplier_v2 #(.LOGQ(N)) mr0(A0_temp, tf0, A0);
    modred_multiplier_v2 #(.LOGQ(N)) mr1(A1_temp, tf1, A1);
    modred_multiplier_v2 #(.LOGQ(N)) mr2(A2_temp, tf2, A2);
    modred_multiplier_v2 #(.LOGQ(N)) mr3(A3_temp, tf3, A3);
    modred_multiplier_v2 #(.LOGQ(N)) mr4(A4_temp, tf4, A4);
    modred_multiplier_v2 #(.LOGQ(N)) mr5(A5_temp, tf5, A5);
    modred_multiplier_v2 #(.LOGQ(N)) mr6(A6_temp, tf6, A6);
    modred_multiplier_v2 #(.LOGQ(N)) mr7(A7_temp, tf7, A7);
endmodule
