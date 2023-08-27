`timescale 1ps/1ps

module ntt_intt_pe_cell_tb ();
    parameter N = 17;
    reg [3*N-1+2:0] buffer;
    reg [N-1:0] a, b, tf;
    wire [N-1:0] p;
    reg inv = 1'B0, sub = 1'B0;
    reg clk = 1'B0;

    integer testcase_file;
    integer actual_file;
    integer i = 0;

    ntt_intt_pe_cell #(.N(N)) uut(.a(a), .b(b), .tf(tf), .inv(inv), .sub(sub), .p(p));

    initial begin
        $dumpfile("ntt_intt_pe_cell_tb.vcd");
        $dumpvars(0, ntt_intt_pe_cell_tb);

        testcase_file = $fopen("./tests/ntt_intt_pe_cell/testcase.txt", "r");
        actual_file = $fopen("./tests/ntt_intt_pe_cell/actual.txt", "w");
    end
    
    always begin
        if (!$feof(testcase_file)) begin
            $fscanf(testcase_file, "%b\n", buffer);
            a = buffer[3*N-1+2:2*N+2];
            b = buffer[2*N-1+2:N+2];
            tf = buffer[N-1+2:2];
            sub = buffer[1];
            inv = buffer[0];
            #10;
            $fdisplay(actual_file,"%b", p);

        end else begin
            $finish;
            $fclose(testcase_file);
            $fclose(actual_file);
        end

        #10;
    end

    always #10 clk = ~clk;
endmodule