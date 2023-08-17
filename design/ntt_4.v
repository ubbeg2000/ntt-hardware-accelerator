`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 27.07.2023 11:00:03
// Design Name: 
// Module Name: ntt_4
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

// q = 257, psi = 64
module ntt_4(
    input [35:0] a,
    output [35:0] an
    );
    
    wire [35:0] antemp;
    
    ntt_pe #(.N(9)) pe0(.a(241), .b(a[26:18]), .offset(a[8:0]), .sub(0), .s(antemp[8:0]));
    ntt_pe #(.N(9)) pe1(.a(241), .b(a[35:27]), .offset(a[17:9]), .sub(0), .s(antemp[17:9]));
    ntt_pe #(.N(9)) pe2(.a(241), .b(a[26:18]), .offset(a[8:0]), .sub(1), .s(antemp[26:18]));
    ntt_pe #(.N(9)) pe3(.a(241), .b(a[35:27]), .offset(a[17:9]), .sub(1), .s(antemp[35:27]));
    
    ntt_pe #(.N(9)) pe4(.a(64), .b(antemp[17:9]), .offset(antemp[8:0]), .sub(0), .s(an[8:0]));
    ntt_pe #(.N(9)) pe5(.a(64), .b(antemp[17:9]), .offset(antemp[8:0]), .sub(1), .s(an[17:9]));
    ntt_pe #(.N(9)) pe6(.a(4), .b(antemp[35:27]), .offset(antemp[26:18]), .sub(0), .s(an[26:18]));
    ntt_pe #(.N(9)) pe7(.a(4), .b(antemp[35:27]), .offset(antemp[26:18]), .sub(1), .s(an[35:27]));
endmodule
