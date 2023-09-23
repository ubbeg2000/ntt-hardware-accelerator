`timescale 1ps/1ps

module modred_v2_tb;
    parameter N = 17;
    reg [2*N-1:0] buffer;
    reg [2*N-1:0] a;
    wire [N-1:0] s;

    integer testcase_file;
    integer actual_file;
    integer i = 0;

    modred_v2 #(.LOGQ(N)) uut(.a(a), .s(s));

    initial begin
        $dumpfile("modred_v2_tb.vcd");
        $dumpvars(0, modred_v2_tb);

        testcase_file = $fopen("./tests/modred_v2/testcase.txt", "r");
        actual_file = $fopen("./tests/modred_v2/actual.txt", "w");
    end
    
    always begin
        if (!$feof(testcase_file)) begin
            $fscanf(testcase_file, "%b\n", buffer);
            a = buffer[2*N-1:0];
            #10;
            $fdisplay(actual_file,"%b", s);

        end else begin
            $finish;
            $fclose(testcase_file);
            $fclose(actual_file);
        end

        #10;
    end
endmodule