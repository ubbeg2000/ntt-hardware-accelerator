`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 02.08.2023 14:14:29
// Design Name: 
// Module Name: intt
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


module intt #(parameter N = 9, D = 8) (
    input [N*D-1:0] an,
    input clk,
    output [N*D-1:0] a
    );
    
    integer NINV = 63489;
    integer psi_table [$clog2(D)-1:0][D/2-1:0];
    
//    [[241], [193, 253], [129, 249, 225, 255]]
    
    initial begin
        psi_table[0][0] = 65536;
        psi_table[1][0] = 65281;
        psi_table[1][1] = 256;
        psi_table[2][0] = 61441;
        psi_table[2][1] = 4096;
        psi_table[2][2] = 64513;
        psi_table[2][3] = 1024;
        psi_table[3][0] = 49153;
        psi_table[3][1] = 16384;
        psi_table[3][2] = 61441;
        psi_table[3][3] = 4096;
        psi_table[3][4] = 64513;
        psi_table[3][5] = 1024;
        psi_table[3][6] = 65281;
        psi_table[3][7] = 256;
        psi_table[4][0] = 32769;
        psi_table[4][1] = 32768;
        psi_table[4][2] = 57345;
        psi_table[4][3] = 8192;
        psi_table[4][4] = 63489;
        psi_table[4][5] = 2048;
        psi_table[4][6] = 65025;
        psi_table[4][7] = 512;
        psi_table[4][8] = 65409;
        psi_table[4][9] = 128;
        psi_table[4][10] = 65505;
        psi_table[4][11] = 32;
        psi_table[4][12] = 65529;
        psi_table[4][13] = 8;
        psi_table[4][14] = 65535;
        psi_table[4][15] = 2;
    end
    
    wire [N-1:0] inter_stage [$clog2(D)-1:0][D-1:0];
    
    genvar i, j, k;
    generate
//    for i in range(int(log2(n)) - 1, -1, -1):
    for (i = $clog2(D) - 1; i > -1; i = i-1) begin
        for (j = 0; j < 2**i; j = j+1) begin
            for (k = 0; k < D/(2**(i+1)); k = k+1) begin
                if (i == $clog2(D) - 1) begin
                    intt_pe #(.N(N)) pe0(
                        .a(an[(j*D/(2**i)+k+1)*N-1:(j*D/(2**i)+k)*N]), 
                        .b(an[(j*D/(2**i)+k+D/(2**(i+1))+1)*N-1:(j*D/(2**i)+k+D/(2**(i+1)))*N]), 
                        .c(1), 
                        .sub(0), 
                        .s(inter_stage[i][j*D/(2**i)+k])
                        );
                    intt_pe #(.N(N)) pe1(
                        .a(an[(j*D/(2**i)+k+1)*N-1:(j*D/(2**i)+k)*N]), 
                        .b(an[(j*D/(2**i)+k+D/(2**(i+1))+1)*N-1:(j*D/(2**i)+k+D/(2**(i+1)))*N]), 
                        .c(psi_table[i][j]), 
                        .sub(1), 
                        .s(inter_stage[i][j*D/(2**i)+k+D/(2**(i+1))])
                        );
                end else begin
                    intt_pe #(.N(N)) pe0(
                        .a(inter_stage[i+1][j*D/(2**i)+k]), 
                        .b(inter_stage[i+1][j*D/(2**i)+k+D/(2**(i+1))]), 
                        .c(1), 
                        .sub(0), 
                        .s(inter_stage[i][j*D/(2**i)+k])
                        );
                    intt_pe #(.N(N)) pe1(
                        .a(inter_stage[i+1][j*D/(2**i)+k]), 
                        .b(inter_stage[i+1][j*D/(2**i)+k+D/(2**(i+1))]), 
                        .c(psi_table[i][j]), 
                        .sub(1), 
                        .s(inter_stage[i][j*D/(2**i)+k+D/(2**(i+1))])
                        );
                end
            end
        end
    end
    
    for (i = 0; i < D; i = i+1) begin
        modred_multiplier #(.LOGQ(N)) mul(.a(inter_stage[0][i]), .b(NINV), .p(a[N*(i+1)-1:N*i]));
//        assign a[N*(i+1)-1:N*i] = inter_stage[$clog2(D)-1][i];
    end
    
    endgenerate
endmodule
