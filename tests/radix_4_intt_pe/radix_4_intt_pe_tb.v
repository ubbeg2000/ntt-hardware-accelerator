`timescale 1ps/1ps

module radix_4_intt_pe_tb ();
    parameter N = 5;
    reg [4*N-1+1:0] buffer;
    reg [N-1:0] a, b, tf;
    wire [N-1:0] p;
    reg inv = 1'B0;
    reg clk = 1'B0;

    integer testcase_file;
    integer actual_file;
    integer i = 0;

    reg [N-1:0] tf0, tf1, tf2;
    reg [N-1:0] a0, a1, a2, a3;
    wire [N-1:0] b0, b1, b2, b3;

    // [[4], [2, 8]]

    radix_4_intt_pe #(.N(N)) uut(
        .an(a0),
        .bn(a1),
        .cn(a2),
        .dn(a3),
        .tf(65473),
        .a(b0),
        .b(b1),
        .c(b2),
        .d(b3)
    );

    initial begin
        $dumpfile("radix_4_intt_pe_tb.vcd");
        $dumpvars(0, radix_4_intt_pe_tb);

        testcase_file = $fopen("./tests/radix_4_intt_pe/testcase.txt", "r");
        actual_file = $fopen("./tests/radix_4_intt_pe/actual.txt", "w");
    end
    
    always begin
        if (!$feof(testcase_file)) begin
            $fscanf(testcase_file, "%b\n", buffer);
            a3 = buffer[4*N-1+1:3*N+1];
            a1 = buffer[3*N-1+1:2*N+1];
            a2 = buffer[2*N-1+1:1*N+1];
            a0 = buffer[1*N-1+2:0*N+1];
            inv = buffer[0];
            #10;
            $fdisplay(actual_file,"%b%b%b%b", b3, b2, b1, b0);

        end else begin
            $finish;
            $fclose(testcase_file);
            $fclose(actual_file);
        end

        #10;
    end

    always #10 clk = ~clk;
endmodule