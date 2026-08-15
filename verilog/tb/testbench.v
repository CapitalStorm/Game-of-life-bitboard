module testbench;
    reg [1:0] a;
    reg [1:0] b;
    wire [1:0] sum;
    wire carry;

    two_bit_adder adder1 (
        .a(a),
        .b(b),
        .sum(sum),
        .carry(carry)
    );

    integer i; // Loop variable for generating test cases
    reg [3:0] test_vector; // test vector to hold the combined value of a and b

    initial begin
        for (i = 0; i < 16; i = i + 1) begin
            test_vector = i; // Assign the loop variable to the test vector
            a = test_vector[3:2]; // Assign the upper 2 bits of test_vector to a
            b = test_vector[1:0]; // Assign the lower 2 bits of test_vector to b
            #5; // Wait for 5 time units
            $display("a: %b, b: %b, sum: %b, carry: %b", a, b, sum, carry);
        end
        $finish; // End the simulation
    end
endmodule