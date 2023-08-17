`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 14.08.2023 09:34:13
// Design Name: 
// Module Name: bit_reverse_order
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


module bit_reverse_order #(parameter N = 17, D = 8) (
    input [D*N-1:0] a,
    output [D*N-1:0] b
    );
    
    assign b[8:0] = a[8:0];
    assign b[44:36] = a[17:9];
    assign b[26:18] = a[26:18];
    assign b[62:54] = a[35:27];
    assign b[17:9] = a[44:36];
    assign b[53:45] = a[53:45];
    assign b[35:27] = a[62:54];
    assign b[71:63] = a[71:63];
endmodule
