`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03.08.2023 14:07:52
// Design Name: 
// Module Name: ntt_intt
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module ntt_flat #(parameter N = 17, D = 8) (
    input [D*N-1:0] a,
    input clk,
    output [D*N-1:0] b
    );
    
    wor [N-1:0] pe_b [D-1:0];
    wire [D-1:0] sub_mux_out;
    wire [D*N-1:0] b_temp;
    wire [N-1:0] reg_in [D-1:0], reg_out [D-1:0];
    wire [$clog2($clog2(D))-1:0] cnt_reg_val = 0, cnt_out = 0;
    wire [$clog2(D)*D-1:0] sub_mux_in;
    wire [$clog2($clog2(D))-1:0] count_q;
    
    counter #(.N($clog2($clog2(D)))) stage_counter(.clk(clk), .rst(0), .down(0), .count(count_q));
    mux #(.N(D), .S($clog2(D))) sub_mux(.a(sub_mux_in), .sel(count_q), .s(sub_mux_out));
    
    genvar i, j;
    generate
    for (i = 0; i < $clog2(D); i=i+1) begin
        for (j = 0; j < D; j=j+1) begin
            assign sub_mux_in[D*i+j] = j/(2**($clog2(D)-i-1))%2;
        end
    end
    
    for (i = 0; i < D; i = i+1) begin
        wor [$clog2(D)*N-1:0] demux_out; 
        wire [$clog2(D)*N-1:0] mux_in;
        wire [N-1:0] c_in, c_out;
        
        for (j = 0; j < $clog2(D); j=j+1) begin
            localparam mult_index = i/(2**($clog2(D)-j));
            assign mux_in[N*(j+1)-1:N*j] = mult_index+(1<<j);
            
            localparam jump = 1<<($clog2(D)-j-1);
            if ((i/jump)%2)
                assign pe_b[i-jump] = demux_out[N*(j+1)-1:N*j];
            else
                assign pe_b[i+jump] = demux_out[N*(j+1)-1:N*j];
        end
        
        master_slave_dff #(.N(N)) msdff(
            .clk(clk), 
            .rst(0), 
            .d(count_q == $clog2(D) ? a[N*(i+1)-1:N*i] : reg_in[i]), 
            .q(reg_out[i])
            );
        demux #(.N(N), .S($clog2(D))) dem(
            .a(reg_out[i]), 
            .sel(count_q), 
            .s(demux_out)
            );
        mux #(.N(N), .S($clog2(D))) m(
            .a(mux_in),
            .sel(count_q),
            .s(c_in)
            );
        psi_table pt(
            .addr(c_in), 
            .value(c_out)
            );
        ntt_pe #(.N(N)) pe(
            .a(reg_out[i]), 
            .b(pe_b[i]), 
            .c(c_out),
            .sub(sub_mux_out[i]), 
            .s(reg_in[i])
            );
            
        assign b_temp[N*(i+1)-1:N*i] = reg_in[i];
    end
    endgenerate
endmodule
