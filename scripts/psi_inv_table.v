`timescale 1ps/1ns

module psi_inv_table (
    input [5:0] addr,
    output reg [16:0] value
    );

    always @ (addr) begin
    case (addr)
        6'B000000: value = 1;
        6'B000001: value = 56481;
        6'B000010: value = 94460;
        6'B000011: value = 85549;
        6'B000100: value = 122469;
        6'B000101: value = 91897;
        6'B000110: value = 12796;
        6'B000111: value = 97768;
        6'B001000: value = 80966;
        6'B001001: value = 70777;
        6'B001010: value = 94089;
        6'B001011: value = 61818;
        6'B001100: value = 27271;
        6'B001101: value = 53993;
        6'B001110: value = 101113;
        6'B001111: value = 16401;
        6'B010000: value = 29496;
        6'B010001: value = 9081;
        6'B010010: value = 51694;
        6'B010011: value = 24191;
        6'B010100: value = 95803;
        6'B010101: value = 65672;
        6'B010110: value = 23771;
        6'B010111: value = 34980;
        6'B011000: value = 108801;
        6'B011001: value = 60706;
        6'B011010: value = 97306;
        6'B011011: value = 56382;
        6'B011100: value = 122500;
        6'B011101: value = 11370;
        6'B011110: value = 63082;
        6'B011111: value = 2630;
        6'B100000: value = 77019;
        6'B100001: value = 52438;
        6'B100010: value = 88919;
        6'B100011: value = 38592;
        6'B100100: value = 10943;
        6'B100101: value = 92075;
        6'B100110: value = 90663;
        6'B100111: value = 36255;
        6'B101000: value = 4781;
        6'B101001: value = 29373;
        6'B101010: value = 32976;
        6'B101011: value = 75827;
        6'B101100: value = 118214;
        6'B101101: value = 76071;
        6'B101110: value = 86137;
        6'B101111: value = 19667;
        6'B110000: value = 115219;
        6'B110001: value = 61857;
        6'B110010: value = 4791;
        6'B110011: value = 70915;
        6'B110100: value = 49189;
        6'B110101: value = 83280;
        6'B110110: value = 34734;
        6'B110111: value = 79322;
        6'B111000: value = 130467;
        6'B111001: value = 115834;
        6'B111010: value = 35701;
        6'B111011: value = 14943;
        6'B111100: value = 43826;
        6'B111101: value = 17032;
        6'B111110: value = 99995;
        6'B111111: value = 55254;
    endcase
    end
endmodule
