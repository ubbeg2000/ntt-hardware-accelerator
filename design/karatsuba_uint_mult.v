`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 25.07.2023 13:09:32
// Design Name: 
// Module Name: karatsuba_uint_mult
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


module karatsuba_uint_mult #(parameter N = 4) (
    input [N-1:0] a,
    input [N-1:0] b,
    output [2*N-1:0] p
    );
    
    wire [N-1:0] ab_high, ab_low, ab_mid, ab_mid_temp_0, ab_mid_temp_1;
    wire [N/2-1:0] a_mid, b_mid;
    wire addamid_cout, addbmid_cout;
    
    adder #(.N(N/2)) addamid(.a(a[N-1:N/2]), .b(a[N/2-1:0]), .cin(0), .s(a_mid), .cout(addamid_cout));
    adder #(.N(N/2)) addbmid(.a(b[N-1:N/2]), .b(b[N/2-1:0]), .cin(0), .s(b_mid), .cout(addbmid_cout));
    
    generate
    if (N == 4) begin
        multiplier #(.N(N/2)) multhigh(.a(a[N-1:N/2]), .b(b[N-1:N/2]), .p(ab_high));
        multiplier #(.N(N)) multmid(.a({0, addamid_cout, a_mid}), .b({0, addbmid_cout, b_mid}), .p(ab_mid_temp_0));
        multiplier #(.N(N/2)) multlow(.a(a[N/2-1:0]), .b(b[N/2-1:0]), .p(ab_low));
    end else begin
       karatsuba_uint_mult #(.N(N/2)) multhigh(.a(a[N-1:N/2]), .b(b[N-1:N/2]), .p(ab_high));
       karatsuba_uint_mult #(.N(N/2)) multmid(.a(a_mid), .b(b_mid), .p(ab_mid_temp_0));
       karatsuba_uint_mult #(.N(N/2)) multlow(.a(a[N/2-1:0]), .b(b[N/2-1:0]), .p(ab_low)); 
    end
    endgenerate
    
    adder #(.N(N)) sub0(.a(ab_mid_temp_0), .b(~ab_low), .cin(1), .s(ab_mid_temp_1));
    adder #(.N(N)) sub1(.a(ab_mid_temp_1), .b(~ab_high), .cin(1), .s(ab_mid));
    adder #(.N(2*N)) addp(.a({ab_high, ab_low}), .b({{(N/2){1'B0}}, ab_mid, {{(N/2){1'B0}}}}), .cin(0), .s(p));
endmodule
