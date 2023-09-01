module twiddle_factor_generator_tb();
    parameter N = 17, D = 8;

    reg [2*N*D-1+1+$clog2($clog2(D)):0] buffer;
    reg [N*D-1:0] a, b;
    wire [N*D-1:0] c;
    wire [N-1:0] cs [D-1:0], as [D-1:0], bs [D-1:0];
    reg inv;
    reg [$clog2($clog2(D))-1:0] stage;

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

    twiddle_factor_generator #(.N(N), .D(D)) uut (.tf_in(a), .tf_in_inv(b), .inv(inv), .stage(stage), .tf(c));

    initial begin
        $dumpfile("twiddle_factor_generator_tb.vcd");
        $dumpvars(0, twiddle_factor_generator_tb);
        for (j=0;j<D;j=j+1) begin
            $dumpvars(1, cs[j]);
            $dumpvars(2, as[j]);
            $dumpvars(3, bs[j]);
        end

        testcase_file = $fopen("./tests/twiddle_factor_generator/testcase.txt", "r");
        actual_file = $fopen("./tests/twiddle_factor_generator/actual.txt", "w");
    end
    
    always begin
        if (!$feof(testcase_file)) begin
            $fscanf(testcase_file, "%b\n", buffer);

            a = buffer[2*D*N+1+$clog2($clog2(D))-1:D*N+1+$clog2($clog2(D))];
            b = buffer[D*N+1+$clog2($clog2(D))-1:1+$clog2($clog2(D))];
            inv = buffer[$clog2($clog2(D))];
            stage = buffer[$clog2($clog2(D))-1:0];

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