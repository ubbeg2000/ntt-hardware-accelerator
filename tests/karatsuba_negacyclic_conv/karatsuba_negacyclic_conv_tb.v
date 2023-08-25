`timescale 1ps/1ps

module karatsuba_negacyclic_conv_tb ();
    parameter N = 17, D = 8;
    
    reg clk = 0;
    reg [2*D*N-1:0] a;
    reg [D*N-1:0] b;
    wire [N-1:0] bs [D-1:0];

    genvar k;
    generate
    for (k=0;k<D;k=k+1) begin
        assign bs[k] = b[N*(k+1)-1:N*k];
    end
    endgenerate
    
    integer testcase_file;
    integer actual_file;
    integer i;

    karatsuba_negacyclic_conv #(.N(N), .D(D)) uut(.a(a[2*D*N-1:D*N]), .b(a[D*N-1:0]), .clk(clk), .p(b));

    initial begin
        $dumpfile("karatsuba_negacyclic_conv_tb.vcd");
        $dumpvars(0, karatsuba_negacyclic_conv_tb);
        for (i=0;i<D;i=i+1) begin
            $dumpvars(1, bs[i]);
        end

        testcase_file = $fopen("./tests/karatsuba_negacyclic_conv/testcase.txt", "r");
        actual_file = $fopen("./tests/karatsuba_negacyclic_conv/actual.txt", "w");
    end

    always begin
        if (!$feof(testcase_file)) begin
            $fscanf(testcase_file, "%b\n", a);

            for (i=0;i<D;i=i+1) begin
                #10;
                if (i==D-1) begin
                    $fdisplay(actual_file,"%b", b);
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