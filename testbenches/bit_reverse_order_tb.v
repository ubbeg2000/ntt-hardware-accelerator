`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 14.08.2023 09:39:16
// Design Name: 
// Module Name: bit_reverse_order_tb
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


module bit_reverse_order_tb();
    parameter N = 9, D = 8;
    wire [N*D-1:0] a;
    wire [N*D-1:0] b;
    wire [N-1:0] bs [D-1:0], as [D-1:0];
    
    genvar i;
    generate
    for (i=0;i<D;i=i+1) begin
        assign a[N*(i+1)-1:N*i] = i;
        assign bs[i] = b[N*(i+1)-1:N*i];
        assign as[i] = a[N*(i+1)-1:N*i];
    end
    endgenerate
    
    bit_reverse_order #(.N(N), .D(D)) uut(.a(a), .b(b));
    
    initial #(100) $stop;
endmodule
