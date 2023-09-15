`timescale 1ps/1ps

module tff (
    input t,
    input clk,
    output reg q,
    output q_inv
    );

    initial q <= 1'B0;
    
    always @ (posedge clk)
    begin
      q <= t ^ q;
    end

    assign q_inv = ~q;
endmodule