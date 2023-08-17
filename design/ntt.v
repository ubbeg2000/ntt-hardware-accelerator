`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 02.08.2023 11:31:46
// Design Name: 
// Module Name: ntt
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


module ntt #(parameter N = 17, D = 8) (
    input [D*N-1:0] a,
    input clk,
    output [D*N-1:0] an
    );
    
    integer psi_table [$clog2(D)-1:0][D/2-1:0];
    
    initial begin
        psi_table[0][0] = 65536;
        psi_table[1][0] = 256;
        psi_table[1][1] = 65281;
        psi_table[2][0] = 16;
        psi_table[2][1] = 65521;
        psi_table[2][2] = 64;
        psi_table[2][3] = 65473;
        psi_table[3][0] = 4;
        psi_table[3][1] = 65533;
        psi_table[3][2] = 16;
        psi_table[3][3] = 65521;
        psi_table[3][4] = 64;
        psi_table[3][5] = 65473;
        psi_table[3][6] = 256;
        psi_table[3][7] = 65281;
        psi_table[4][0] = 2;
        psi_table[4][1] = 65535;
        psi_table[4][2] = 8;
        psi_table[4][3] = 65529;
        psi_table[4][4] = 32;
        psi_table[4][5] = 65505;
        psi_table[4][6] = 128;
        psi_table[4][7] = 65409;
        psi_table[4][8] = 512;
        psi_table[4][9] = 65025;
        psi_table[4][10] = 2048;
        psi_table[4][11] = 63489;
        psi_table[4][12] = 8192;
        psi_table[4][13] = 57345;
        psi_table[4][14] = 32768;
        psi_table[4][15] = 32769;
    end
    
    wire [N-1:0] inter_stage [$clog2(D)-1:0][D-1:0];
    
    genvar i, j, k;
    generate
    for (i = 0; i < $clog2(D); i = i+1) begin
        for (j = 0; j < 2**i; j = j+1) begin
            for (k = 0; k < D/(2**(i+1)); k = k+1) begin
                if (i == 0) begin
                    ntt_pe #(.N(N)) pe0(
                        .a(a[(j*D/(2**i)+k+1)*N-1:(j*D/(2**i)+k)*N]), 
                        .b(a[(j*D/(2**i)+k+D/(2**(i+1))+1)*N-1:(j*D/(2**i)+k+D/(2**(i+1)))*N]), 
                        .c(psi_table[i][j]), 
                        .sub(0), 
                        .s(inter_stage[i][j*D/(2**i)+k])
                        );
                    ntt_pe #(.N(N)) pe1(
                        .a(a[(j*D/(2**i)+k+1)*N-1:(j*D/(2**i)+k)*N]), 
                        .b(a[(j*D/(2**i)+k+D/(2**(i+1))+1)*N-1:(j*D/(2**i)+k+D/(2**(i+1)))*N]), 
                        .c(psi_table[i][j]), 
                        .sub(1), 
                        .s(inter_stage[i][j*D/(2**i)+k+D/(2**(i+1))])
                        );
                end else begin
                    ntt_pe #(.N(N)) pe0(
                        .a(inter_stage[i-1][j*D/(2**i)+k]), 
                        .b(inter_stage[i-1][j*D/(2**i)+k+D/(2**(i+1))]), 
                        .c(psi_table[i][j]), 
                        .sub(0), 
                        .s(inter_stage[i][j*D/(2**i)+k])
                        );
                    ntt_pe #(.N(N)) pe1(
                        .a(inter_stage[i-1][j*D/(2**i)+k]), 
                        .b(inter_stage[i-1][j*D/(2**i)+k+D/(2**(i+1))]), 
                        .c(psi_table[i][j]), 
                        .sub(1), 
                        .s(inter_stage[i][j*D/(2**i)+k+D/(2**(i+1))])
                        );
                end
            end
        end
    end
    
    for (i = 0; i < D; i = i+1) begin
        assign an[N*(i+1)-1:N*i] = inter_stage[$clog2(D)-1][i];
    end
    
    endgenerate
endmodule
