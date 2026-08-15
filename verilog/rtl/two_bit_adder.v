module two_bit_adder(
    input [1:0] a,
    input [1:0] b,
    output [1:0] sum,
    output carry
);
    wire carry0;

    full_adder fa0 (
        .a(a[0]),
        .b(b[0]),
        .cin(1'b0),
        .sum(sum[0]),
        .cout(carry0)
    );

    full_adder fa1 (
        .a(a[1]),
        .b(b[1]),
        .cin(carry0),
        .sum(sum[1]),
        .cout(carry)
    );
endmodule
