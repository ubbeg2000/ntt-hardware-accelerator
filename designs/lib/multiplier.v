`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 19.07.2023 18:26:19
// Design Name: 
// Module Name: multiplier
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


module multiplier #(parameter N = 1) (
    input [N-1:0] a,
    input [N-1:0] b,
    output [2*N-1:0] p
    );
    
    genvar i;
    
    wire [2*N-1:0] adder_out [N-1:0];
    wire [N-1:0] mux_out [N-1:0];
    
    generate
    for (i = 0; i < N; i = i + 1) begin
        mux_2x1 #(.N(N)) mux(.a({N{1'B0}}), .b(b), .sel(a[i]), .s(mux_out[i]));
        if (i == 0)
            adder #(.N(2*N)) add(.a({(2*N){1'B0}}), .b({{N{1'B0}}, mux_out[i]}), .cin(1'B0), .s(adder_out[i]));
        else
            adder #(.N(2*N)) add(.a(adder_out[i-1]), .b({{N{1'B0}}, mux_out[i]} << i), .cin(1'B0), .s(adder_out[i]));
    end
    endgenerate
    
    assign p = adder_out[N-1];
endmodule
