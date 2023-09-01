`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 24.07.2023 11:58:52
// Design Name: 
// Module Name: poly_mult_systolic_array_tb
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


module poly_mult_systolic_array_tb();
    parameter N = 17, D = 16;

    reg [2*N*D-1:0] buffer;
    reg [N*D-1:0] a, b;
    wire [N*D-1:0] c;
    wire [N-1:0] cs [D-1:0], as [D-1:0], bs [D-1:0];

    reg clk = 1'B0;

    integer testcase_file;
    integer actual_file;
    integer j = 0;
    
    genvar i;
    generate
    for (i = 0; i < D; i = i+1) begin
        assign cs[i] = c[N*(i+1)-1:N*i];
        assign as[i] = a[N*(i+1)-1:N*i];
        assign bs[i] = b[N*(i+1)-1:N*i];
    end
    endgenerate

    poly_mult_systolic_array #(.N(N), .D(D)) uut (.horz(a), .vert(b), .clk(clk), .rst(1'B0), .p(c));

    initial begin
        $dumpfile("poly_mult_systolic_array_tb.vcd");
        $dumpvars(0, poly_mult_systolic_array_tb);
        for (j=0;j<D;j=j+1) begin
            $dumpvars(1, cs[j]);
            $dumpvars(2, as[j]);
            $dumpvars(3, bs[j]);
        end

        testcase_file = $fopen("./tests/poly_mult_systolic_array/testcase.txt", "r");
        actual_file = $fopen("./tests/poly_mult_systolic_array/actual.txt", "w");
    end
    
    always begin
        if (!$feof(testcase_file)) begin
            $fscanf(testcase_file, "%b\n", buffer);

            a = buffer[2*D*N-1:D*N];
            b = buffer[N*D-1:0];

            for (j=0;j<5*D;j=j+1) begin
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
