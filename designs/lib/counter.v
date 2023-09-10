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
    output [N-1:0] count
    );

    // wire [N-1:0] t_out;

    // genvar i;
    // generate
    // for (i=0;i<N;i=i+1) begin
    //     if (i == 0)
    //         tff t(.t(1'B1), .clk(clk), .q(t_out[i]));
    //     else
    //         tff t(.t(1'B1), .clk(t_out[i-1]), .q(t_out[i]));
    // end
    // endgenerate

    // assign count = t_out;

    reg [N-1:0] state;

    // initial state = {N{1'B0}};

    always @ (negedge clk) begin
        if (rst == 1'B1) begin
            if (down)
                state <= {N{1'B0}};
            else
                state <= {N{1'B1}};
        end else begin
            if (down)
                state <= state - {{(N-1){1'B0}}, 1'B1};
            else
                state <= state + {{(N-1){1'B0}}, 1'B1};
        end
    end

    assign count = state;
endmodule
