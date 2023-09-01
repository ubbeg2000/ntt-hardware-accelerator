`timescale 1ps/1ps

module twiddle_factor_generator #(parameter N = 17, D = 16) (
    input [D*N-1:0] tf_in,
    input [D*N-1:0] tf_in_inv,
    input inv,
    input [$clog2($clog2(D))-1:0] stage,
    output [D*N-1:0] tf
    );

    wire [D*N-1:0] tf_temp;
    wire [$clog2(D)-1:0] stage_enb = 1 << stage;

    genvar i, j, k;
    generate
    for (i=0;i<D;i=i+1) begin
        mux_2x1 #(.N(N)) m(.a(tf_in[N*(i+1)-1:N*i]), .b(tf_in_inv[N*(i+1)-1:N*i]), .sel(inv), .s(tf_temp[N*(i+1)-1:N*i]));
    end

    for (i=0;i<$clog2(D);i=i+1) begin
        for (j=0;j<2**i;j=j+1) begin
            for (k=0;k<D/2**i;k=k+1) begin
                tri_state_buffer #(.N(N)) tsb(.a(tf_temp[N*(2**i+j+1)-1:N*(2**i+j)]), .en(stage_enb[i]), .b(tf[N*((D/(2**i)*j+k+1))-1:N*(D/(2**i)*j+k)]));
            end
        end
    end
    endgenerate
endmodule