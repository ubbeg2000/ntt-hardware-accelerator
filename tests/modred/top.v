`timescale 1ps/1ps

module top (
    input [16:0] a,
    output [16:0] s
    );

    modred #(.LOGQ(17)) uut(.a(a), .s(s));
    
endmodule