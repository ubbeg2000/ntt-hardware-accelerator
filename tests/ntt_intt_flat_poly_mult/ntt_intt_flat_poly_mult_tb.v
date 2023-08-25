`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03.08.2023 12:46:21
// Design Name: 
// Module Name: ntt_intt_flat_poly_mult_tb
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


module ntt_intt_flat_poly_mult_tb();
    parameter N = 17, D = 16;
    reg [2*N*D-1:0] a;
    wire [N*D-1:0] b1, b2, b3, c;
    wire [N-1:0] cs [D-1:0], as [D-1:0], bs [D-1:0];

    reg clk = 0;

    integer testcase_file;
    integer actual_file;
    integer j = 0;
    
    genvar i;
    generate
    // for (i = 0; i < D; i = i+1) begin
    //     assign a[N*(i+1)-1:N*i] = i + 1;
    //     assign b[N*(i+1)-1:N*i] = D - i;
    // end
    
    // ntt #(.N(N), .D(D)) fta(.a(a), .an(a_out));
    // ntt #(.N(N), .D(D)) ftb(.a(b), .an(b_out));
    
    for (i = 0; i < D; i = i+1) begin
        assign cs[i] = c[N*(i+1)-1:N*i];
        assign as[i] = b1[N*(i+1)-1:N*i];
        assign bs[i] = b2[N*(i+1)-1:N*i];
    end
    endgenerate

    ntt_flat #(.N(N), .D(D)) ntt1(.a(a[2*D*N-1:D*N]), .b(b1), .clk(j > D - 2 ? 0 : clk));
    ntt_flat #(.N(N), .D(D)) ntt2(.a(a[D*N-1:0]), .b(b2), .clk(j > D - 2 ? 0 : clk));
    point_mod_mult #(.N(N), .D(D)) pm(.a(b1), .b(b2), .p(b3));
    intt_flat #(.N(N), .D(D)) intt1(.a(b3), .b(c), .clk(clk));
    // ntt_intt_flat_poly_mult #(.N(N), .D(D)) uut(.a(a[2*D*N-1:D*N]), .b(a[D*N-1:0]), .c(c));

    initial begin
        $dumpfile("ntt_intt_flat_poly_mult_tb.vcd");
        $dumpvars(0, ntt_intt_flat_poly_mult_tb);
        for (j=0;j<D;j=j+1) begin
            $dumpvars(1, cs[j]);
            $dumpvars(2, as[j]);
            $dumpvars(3, bs[j]);
        end

        testcase_file = $fopen("./tests/ntt_intt_flat_poly_mult/testcase.txt", "r");
        actual_file = $fopen("./tests/ntt_intt_flat_poly_mult/actual.txt", "w");
    end
    
    always begin
        if (!$feof(testcase_file)) begin
            $fscanf(testcase_file, "%b\n", a);

            for (j=0;j<2*D;j=j+1) begin
                #10;
                if (j==2*D-1) begin
                    $fdisplay(actual_file,"%b", c);
                end
            end

        end else begin
            $finish;
            $fclose(testcase_file);
            $fclose(actual_file);
        end
    end

    always #10 clk = ~clk;
endmodule
