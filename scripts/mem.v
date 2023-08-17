`timescale 1ps/1ps

module psi_table (
    input [N-1:0] addr,
    output [N-1:0] value
)

    always @ (addr) begin
    case (addr)
        4B'001: value = 4; 
        default: 
    endcase
    end

endmodule