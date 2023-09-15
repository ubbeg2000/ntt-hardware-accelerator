`timescale 1ps/1ps

module up_down_counter #(parameter N = 3) (
    input down,
    input clk,
    output [N-1:0] count
    );

    wire [N-1:0] t_in;
    wire [N-1:0] q;
    wire [N-1:0] q_inv;
    wire [N-1:0] qp_out;
    wire [N-1:0] qp_inv_out;

    genvar i;
    generate
    for (i=0;i<N;i=i+1) begin
        if (i==0) begin
            tff t(.clk(clk), .t(1'B1), .q(q[i]), .q_inv(q_inv[i]));
            assign qp_out[i] = q[i] & ~down;
            assign qp_inv_out[i] = q_inv[i] & down;
        end else begin
            tff t(.clk(clk), .t(qp_out[i-1] | qp_inv_out[i-1]), .q(q[i]), .q_inv(q_inv[i]));
            assign qp_out[i] = q[i] & qp_out[i-1];
            assign qp_inv_out[i] = q_inv[i] & qp_inv_out[i-1];
        end

        assign count[i] = q[i];
    end
    endgenerate
endmodule