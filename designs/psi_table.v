`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 07.08.2023 19:54:21
// Design Name: 
// Module Name: psi_table_32_257
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////

module psi_table (
    input [6:0] addr,
    output reg [16:0] value
    );

    always @ (addr) begin
    case (addr)
        7'B0000000: value = 1;
        7'B0000001: value = 1;
        7'B0000010: value = 1;
        7'B0000011: value = 1;
        7'B0000100: value = 65536;
        7'B0000101: value = 65536;
        7'B0000110: value = 65533;
        7'B0000111: value = 65533;
        7'B0001000: value = 256;
        7'B0001001: value = 256;
        7'B0001010: value = 1024;
        7'B0001011: value = 1024;
        7'B0001100: value = 4096;
        7'B0001101: value = 4096;
        7'B0001110: value = 16384;
        7'B0001111: value = 16384;
        7'B0010000: value = 16;
        7'B0010001: value = 16;
        7'B0010010: value = 64;
        7'B0010011: value = 64;
        7'B0010100: value = 256;
        7'B0010101: value = 256;
        7'B0010110: value = 1024;
        7'B0010111: value = 1024;
        7'B0011000: value = 4096;
        7'B0011001: value = 4096;
        7'B0011010: value = 16384;
        7'B0011011: value = 16384;
        7'B0011100: value = 65536;
        7'B0011101: value = 65536;
        7'B0011110: value = 65533;
        7'B0011111: value = 65533;
        7'B0100000: value = 4;
        7'B0100001: value = 4;
        7'B0100010: value = 16;
        7'B0100011: value = 16;
        7'B0100100: value = 64;
        7'B0100101: value = 64;
        7'B0100110: value = 256;
        7'B0100111: value = 256;
        7'B0101000: value = 1024;
        7'B0101001: value = 1024;
        7'B0101010: value = 4096;
        7'B0101011: value = 4096;
        7'B0101100: value = 16384;
        7'B0101101: value = 16384;
        7'B0101110: value = 65536;
        7'B0101111: value = 65536;
        7'B0110000: value = 65533;
        7'B0110001: value = 65533;
        7'B0110010: value = 65521;
        7'B0110011: value = 65521;
        7'B0110100: value = 65473;
        7'B0110101: value = 65473;
        7'B0110110: value = 65281;
        7'B0110111: value = 65281;
        7'B0111000: value = 64513;
        7'B0111001: value = 64513;
        7'B0111010: value = 61441;
        7'B0111011: value = 61441;
        7'B0111100: value = 49153;
        7'B0111101: value = 49153;
        7'B0111110: value = 1;
        7'B0111111: value = 1;
        7'B1000000: value = 2;
        7'B1000001: value = 2;
        7'B1000010: value = 8;
        7'B1000011: value = 8;
        7'B1000100: value = 32;
        7'B1000101: value = 32;
        7'B1000110: value = 128;
        7'B1000111: value = 128;
        7'B1001000: value = 512;
        7'B1001001: value = 512;
        7'B1001010: value = 2048;
        7'B1001011: value = 2048;
        7'B1001100: value = 8192;
        7'B1001101: value = 8192;
        7'B1001110: value = 32768;
        7'B1001111: value = 32768;
        7'B1010000: value = 65535;
        7'B1010001: value = 65535;
        7'B1010010: value = 65529;
        7'B1010011: value = 65529;
        7'B1010100: value = 65505;
        7'B1010101: value = 65505;
        7'B1010110: value = 65409;
        7'B1010111: value = 65409;
        7'B1011000: value = 65025;
        7'B1011001: value = 65025;
        7'B1011010: value = 63489;
        7'B1011011: value = 63489;
        7'B1011100: value = 57345;
        7'B1011101: value = 57345;
        7'B1011110: value = 32769;
        7'B1011111: value = 32769;
        7'B1100000: value = 2;
        7'B1100001: value = 2;
        7'B1100010: value = 8;
        7'B1100011: value = 8;
        7'B1100100: value = 32;
        7'B1100101: value = 32;
        7'B1100110: value = 128;
        7'B1100111: value = 128;
        7'B1101000: value = 512;
        7'B1101001: value = 512;
        7'B1101010: value = 2048;
        7'B1101011: value = 2048;
        7'B1101100: value = 8192;
        7'B1101101: value = 8192;
        7'B1101110: value = 32768;
        7'B1101111: value = 32768;
        7'B1110000: value = 65535;
        7'B1110001: value = 65535;
        7'B1110010: value = 65529;
        7'B1110011: value = 65529;
        7'B1110100: value = 65505;
        7'B1110101: value = 65505;
        7'B1110110: value = 65409;
        7'B1110111: value = 65409;
        7'B1111000: value = 65025;
        7'B1111001: value = 65025;
        7'B1111010: value = 63489;
        7'B1111011: value = 63489;
        7'B1111100: value = 57345;
        7'B1111101: value = 57345;
        7'B1111110: value = 32769;
        7'B1111111: value = 32769;
    endcase
    end
endmodule
