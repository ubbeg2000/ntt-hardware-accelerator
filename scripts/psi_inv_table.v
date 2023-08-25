`timescale 1ps/1ns

module psi_inv_table (
    input [3:0] addr,
    output reg [16:0] value
    );

    always @ (addr) begin
    case (addr)
        4'B0000: value = 1;
        4'B0001: value = 65281;
        4'B0010: value = 61441;
        4'B0011: value = 65521;
        4'B0100: value = 49153;
        4'B0101: value = 65473;
        4'B0110: value = 64513;
        4'B0111: value = 65533;
        4'B1000: value = 32769;
        4'B1001: value = 65409;
        4'B1010: value = 63489;
        4'B1011: value = 65529;
        4'B1100: value = 57345;
        4'B1101: value = 65505;
        4'B1110: value = 65025;
        4'B1111: value = 65535;
    endcase
    end
endmodule
