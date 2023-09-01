`timescale 1ps/1ps

module top(
    input clk,
    input inv,
    output [2:0] state
);
    ntt_intt_cu cu(
    .clk(clk),
    .inv(inv),
    .state(state)
    );
    
endmodule