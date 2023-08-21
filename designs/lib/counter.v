`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 13.08.2023 14:22:54
// Design Name: 
// Module Name: counter
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


module counter #(parameter N = 2) (
    input clk,
    input rst,
    input down,
    output reg [N-1:0] count = 0
    );
    
//    wire [N-1:0] dq, dnq;
    
//    genvar i;
//    generate
//    for (i=0;i<N;i=i+1) begin
//        if (i==0) begin
//            dff dm(.clk(clk), .rst(rst), .d(dnq[i]), .q(dq[i]), .nq(dnq[i]));
//            dff ds(.clk(~clk), .rst(rst), .d(dq[i]), .q(count[i]));
//        end else begin
//            dff dm(.clk(dnq[i-1]), .rst(rst), .d(dnq[i]), .q(dq[i]), .nq(dnq[i]));
//            dff ds(.clk(~clk), .rst(rst), .d(dq[i]), .q(count[i]));
//        end
//    end
//    endgenerate
//    initial begin
    reg [N-1:0] state; 
    initial state = 32'D0;
    always @ (posedge clk) state = state + 1;
    always @ (negedge clk) count = state;
//    end
endmodule