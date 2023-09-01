`timescale 1ps/1ps

module tri_state_buffer #(parameter N = 17) (
    input [N-1:0] a,
    input en,
    output [N-1:0] b
);
    assign b = en ? a : {N{1'BZ}};
    
endmodule