`timescale 1ps/1ps

module tff (
    input t,
    input clk,
    output reg q
    );

    // initial q <= 1'B0;
    
    always @ (posedge clk)
    begin
      q <= t ^ q;
    end
endmodule