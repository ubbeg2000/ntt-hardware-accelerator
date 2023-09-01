`timescale 1ps/1ps

module ntt_intt_cu_tb ();
    reg clk = 0;
    reg inv = 0;
    wire [2:0] state;

    initial begin
        $dumpfile("ntt_intt_cu_tb.vcd");
        $dumpvars(0, ntt_intt_cu_tb);
    end

    ntt_intt_cu uut(.clk(clk), .inv(inv), .state(state));

    always #10 clk = ~clk;

    initial #200 inv = ~inv;
    initial #1000 $finish;
    
endmodule