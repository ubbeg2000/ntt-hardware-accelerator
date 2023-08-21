`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 24.07.2023 11:32:55
// Design Name: 
// Module Name: poly_mult_systolic_array
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


module poly_mult_systolic_array #(parameter D = 4, N = 4) (
    input [D*N-1:0] horz,
    input [D*N-1:0] vert,
    input clk,
    input rst,
    output [2*N*(2*D-1)-1:0] p
    );
    
    parameter N_OUT = 2 * N;
    
    wire [N-1:0] horz_out [D-1:0][D-1:0];
    wire [N_OUT-1:0] diag_out [D-1:0][D-1:0];
    
    genvar i, j;
    
    generate
    for (i = 0; i < D; i = i + 1) begin
        for (j = 0; j < 1; j = j + 1) begin
            poly_mult_pe_cell #(.N(N)) pe(
                .horz(horz[N*(D-i)-1:N*(D-1-i)]), 
                .vert(vert[N*(j+1)-1:N*j]), 
                .offset({N_OUT{0}}), 
                .clk(clk),  
                .rst(rst),
                .horz_out(horz_out[i][j]), 
                .diag_out(diag_out[i][j])
                );
        end
    end
    endgenerate
    
    generate
    for (i = 1; i < D; i = i + 1) begin
        for (j = 1; j < D; j = j + 1) begin
            poly_mult_pe_cell #(.N(N)) pe (
                .horz(horz_out[i][j-1]), 
                .vert(vert[N*(j+1)-1:N*j]), 
                .offset(diag_out[i-1][j-1]), 
                .clk(clk),  
                .rst(rst),
                .horz_out(horz_out[i][j]), 
                .diag_out(diag_out[i][j])
                );
        end
    end    
    endgenerate
    
    generate
    for (i = 0; i < 1; i = i + 1) begin
        for (j = 1; j < D; j = j + 1) begin
            poly_mult_pe_cell #(.N(N)) pe(
                .horz(horz_out[i][j-1]), 
                .vert(vert[N*(j+1)-1:N*j]), 
                .offset({N_OUT{0}}), 
                .clk(clk), 
                .rst(rst),
                .horz_out(horz_out[i][j]), 
                .diag_out(diag_out[i][j])
                );
        end
    end
    endgenerate
    
    generate
    for (j = 0; j < D; j = j + 1) begin
        assign p[N_OUT*(j+1)-1:N_OUT*j] = diag_out[D-1][j];
    end
    endgenerate
    
    generate
    for (i = D - 2; i >= 0; i = i - 1) begin
        assign p[N_OUT*D+N_OUT*(D-1-i)-1:N_OUT*D+N_OUT*(D-2-i)] = diag_out[i][D-1];
    end
    endgenerate
endmodule
