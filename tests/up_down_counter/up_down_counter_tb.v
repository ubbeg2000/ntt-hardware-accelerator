`timescale 1ps/1ps

module up_down_counter_tb ();
    parameter N = 3;
    reg [3*N-1+2:0] buffer;
    reg [N-1:0] a, b, tf;
    wire [N-1:0] p;
    reg inv = 1'B0, sub = 1'B0;
    reg clk = 1'B0;
    reg down = 1'B0;

    wire [N-1:0] count;

    integer testcase_file;
    integer actual_file;
    integer i = 0;

    up_down_counter #(.N(N)) uut(.clk(clk), .down(down), .count(count));

    initial begin
        $dumpfile("up_down_counter_tb.vcd");
        $dumpvars(0, up_down_counter_tb);
    end

    always #10 clk = ~clk;

    initial #100 down = ~down;

    initial #500 $finish;
endmodule