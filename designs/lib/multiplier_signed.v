`timescale 1ps/1ps

module multiplier_signed #(parameter N = 17) (
    input signed [N-1:0] a,
    input signed [N-1:0] b,
    output [2*N-1:0] p
    );

    genvar i;
    
    wire [2*N-1:0] adder_out [N-1:0];
    // wire [N-1:0] mux_out [N-1:0];
    
    generate
    for (i = 0; i < N; i = i + 1) begin
        // mux_2x1 #(.N(N)) mux(.a({N{1'B0}}), .b(b), .sel(a[i]), .s(mux_out[i]));
        if (i == 0)
            adder #(.N(2*N)) add(
                .a({(2*N){1'B0}}), 
                .b({{N{1'B0}}, b} & {(2*N){a[i]}}), 
                .cin(1'B0), 
                .s(adder_out[i])
            );
        else if (i == N-1)
            adder #(.N(2*N)) add(
                .a(adder_out[i-1]), 
                .b(~{{{{N{1'B0}}, b} << i} & {(2*N){a[i]}}}), 
                .cin(1'B1), 
                .s(adder_out[i])
            );
        else
            adder #(.N(2*N)) add(
                .a(adder_out[i-1]), 
                .b({{{N{1'B0}}, b} << i} & {(2*N){a[i]}}), 
                .cin(1'B0), 
                .s(adder_out[i])
            );
    end
    endgenerate
    
    assign p = adder_out[N-1];

    // assign p = a * b;
endmodule