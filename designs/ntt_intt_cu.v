`timescale 1ps/1ps

module ntt_intt_cu (
    input clk,
    input inv,
    output reg [2:0] state
    );

    // reg [2:0] s;
    
    // initial state <= 3'B101;
    reg [2:0] next_state;

    always @(*) begin
    case (state)
        3'B000: next_state = inv ? 3'B100 : 3'B001;
        3'B001: next_state = inv ? 3'B000 : 3'B010;
        3'B010: next_state = inv ? 3'B001 : 3'B011;
        3'B011: next_state = inv ? 3'B010 : 3'B100;
        3'B100: next_state = 3'B101;
        3'B101: next_state = inv ? 3'B011 : 3'B000;
        default: next_state = 3'B101;
    endcase
    end

    always @(posedge clk) begin
        state <= next_state;
    end
    
    // assign state = s;
endmodule