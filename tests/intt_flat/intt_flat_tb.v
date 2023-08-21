`timescale 1ns/1ns

module intt_flat_tb();
    parameter N = 17, D = 16, NINV = 61441;

    reg clk = 0, mode = 0;
    reg [D*N-1:0] a;
    wire [D*N-1:0] b;
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

    intt_flat #(.N(N), .D(D), .NINV(NINV)) uut(.clk(clk), .a(a), .b(b));

    initial begin
        $dumpfile("intt_flat_tb.vcd");
        $dumpvars(0, intt_flat_tb);
        for (i=0;i<D;i=i+1) begin
            $dumpvars(1, bs[i]);
        end

        testcase_file = $fopen("./tests/intt_flat/testcase.txt", "r");
        actual_file = $fopen("./tests/intt_flat/actual.txt", "w");
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