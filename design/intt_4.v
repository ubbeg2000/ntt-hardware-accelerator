`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 27.07.2023 12:09:25
// Design Name: 
// Module Name: intt_4
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


module intt_4(
    input [35:0] an,
    output [35:0] a
    );
    
    wire [35:0] atemp, at;
    
    intt_pe #(.N(9)) pe0 (.a(an[8:0]), .b(an[17:9]), .c(1), .sub(0), .s(atemp[8:0]));
    intt_pe #(.N(9)) pe1 (.a(an[8:0]), .b(an[17:9]), .c(253), .sub(1), .s(atemp[17:9]));
    intt_pe #(.N(9)) pe2 (.a(an[26:18]), .b(an[35:27]), .c(1), .sub(0), .s(atemp[26:18]));
    intt_pe #(.N(9)) pe3 (.a(an[26:18]), .b(an[35:27]), .c(193), .sub(1), .s(atemp[35:27]));
    
    intt_pe #(.N(9)) pe4 (.a(atemp[8:0]), .b(atemp[26:18]), .c(1), .sub(0), .s(at[8:0]));
    intt_pe #(.N(9)) pe5 (.a(atemp[17:9]), .b(atemp[35:27]), .c(1), .sub(0), .s(at[17:9]));
    intt_pe #(.N(9)) pe6 (.a(atemp[8:0]), .b(atemp[26:18]), .c(16), .sub(1), .s(at[26:18]));
    intt_pe #(.N(9)) pe7 (.a(atemp[17:9]), .b(atemp[35:27]), .c(16), .sub(1), .s(at[35:27]));
    
    modred_multiplier #(.LOGQ(9)) mr0(.a(at[8:0]), .b(193), .p(a[8:0]));
    modred_multiplier #(.LOGQ(9)) mr1(.a(at[17:9]), .b(193), .p(a[17:9]));
    modred_multiplier #(.LOGQ(9)) mr2(.a(at[26:18]), .b(193), .p(a[26:18]));
    modred_multiplier #(.LOGQ(9)) mr3(.a(at[35:27]), .b(193), .p(a[35:27]));
endmodule
