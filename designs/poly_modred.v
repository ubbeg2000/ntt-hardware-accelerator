`timescale 1ps/1ps

module poly_modred #(parameter N = 17, D = 8) (
    input [D*N-1:0] a,
    output [D*N-1:0] b
    );

    genvar i;
    generate
    for (i=0;i<D;i=i+1) begin
        modred #(.LOGQ(N)) mr(.a({{N{a[N*(i+1)-1]}}, a[N*(i+1)-1:N*i]}), .s(b[N*(i+1)-1:N*i]));
    end
    endgenerate
    
endmodule