`timescale 1ps/1ns

module psi_table (
    input [5:0] addr,
    output reg [16:0] value
    );

    always @ (addr) begin
    case (addr)
        6'B000000: value = 1;
        6'B000001: value = 74336;
        6'B000010: value = 45268;
        6'B000011: value = 36357;
        6'B000100: value = 33049;
        6'B000101: value = 118021;
        6'B000110: value = 38920;
        6'B000111: value = 8348;
        6'B001000: value = 114416;
        6'B001001: value = 29704;
        6'B001010: value = 76824;
        6'B001011: value = 103546;
        6'B001100: value = 68999;
        6'B001101: value = 36728;
        6'B001110: value = 60040;
        6'B001111: value = 49851;
        6'B010000: value = 128187;
        6'B010001: value = 67735;
        6'B010010: value = 119447;
        6'B010011: value = 8317;
        6'B010100: value = 74435;
        6'B010101: value = 33511;
        6'B010110: value = 70111;
        6'B010111: value = 22016;
        6'B011000: value = 95837;
        6'B011001: value = 107046;
        6'B011010: value = 65145;
        6'B011011: value = 35014;
        6'B011100: value = 106626;
        6'B011101: value = 79123;
        6'B011110: value = 121736;
        6'B011111: value = 101321;
        6'B100000: value = 75563;
        6'B100001: value = 30822;
        6'B100010: value = 113785;
        6'B100011: value = 86991;
        6'B100100: value = 115874;
        6'B100101: value = 95116;
        6'B100110: value = 14983;
        6'B100111: value = 350;
        6'B101000: value = 51495;
        6'B101001: value = 96083;
        6'B101010: value = 47537;
        6'B101011: value = 81628;
        6'B101100: value = 59902;
        6'B101101: value = 126026;
        6'B101110: value = 68960;
        6'B101111: value = 15598;
        6'B110000: value = 111150;
        6'B110001: value = 44680;
        6'B110010: value = 54746;
        6'B110011: value = 12603;
        6'B110100: value = 54990;
        6'B110101: value = 97841;
        6'B110110: value = 101444;
        6'B110111: value = 126036;
        6'B111000: value = 94562;
        6'B111001: value = 40154;
        6'B111010: value = 38742;
        6'B111011: value = 119874;
        6'B111100: value = 92225;
        6'B111101: value = 41898;
        6'B111110: value = 78379;
        6'B111111: value = 53798;
    endcase
    end
endmodule
