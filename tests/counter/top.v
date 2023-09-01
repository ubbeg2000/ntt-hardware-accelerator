`timescale 1ps/1ps

module top (
    input clk,
    input rst,
    input down,
    output [3:0] count
    );

    counter #(.N(4)) uut (
        .clk(clk),
        .rst(rst),
        .down(down),
        .count(count)
    );

endmodule