# MIPS 5 STAGE PIPELINING

![image](https://user-images.githubusercontent.com/89673773/179662579-d51c869f-5381-436f-b4d0-88632b6272fe.png)

Fetch, decode, execute, memory access, and write back are the five steps of
instruction execution. A program's execution is made up of a series of these steps. The
second instruction fetch is completed when the first instruction is decoded. When the
pipeline is full, you'll notice that five separate operations are running at the same time.
All these tasks are intertwined. At any given time, five instructions are in progress.
This necessitates the use of five different hardware units. These units must be able to
work on multiple tasks at the same time without interfering with one another. A
storage buffer is used to transmit data from one unit to the nex

# MIPS-ISA-DOT-PRODUCT-PROGRAMMING-WITH-FORWARD-CHAINING

In mathematics, the dot product or scalar product IS an algebraic operation that takes two equal-length sequences of numbers (usually coordinate vectors), and returns a single number. In Euclidean geometry, the dot product of the Cartesian coordinates of two vectors is widely used. It is often called "the" inner product (or rarely projection product) of Euclidean space, even though it is not the only inner product that can be defined on Euclidean space.
The SIMULATION RESULTS for DOT PRODUCT is performed and the code is stated below. 
The Dot Product is done by the function:

![image](https://user-images.githubusercontent.com/89673773/179662142-31ec0661-a44b-4360-b1e7-5f8ea9f37f84.png)

where A(i) and B(i) are Signed and Unsigned Numbers respectively.

The program is given as below –

![image](https://user-images.githubusercontent.com/89673773/179662220-9fc3b78e-6df2-4b70-8b52-fac60aec885b.png)

The ‘r0’ register is hardwired to 0. The addu $r1, $r0, $r0 statement initialize $r1 to 0. The statement beq $r7 $r0 done: check if value of $r7 is equal to 0, if it is equal execute statement tagged ‘done’, if it is not equal keep executing the following statements sequentially.

Lw $r2, 0($r3), load the first element of a which is stored in r3 to r2. Lw $r4, 0($r5), load the first element of b which is stored in r5 to r4. Mul $r2, $r2, r4. Multiple the first elements of a and b and store it in r2. Addu $r1, $r1, adds the newly multiplied value. Accumulation is done here. Addiu $r3, $r3, #4 and Addiu $r5, $r5, #4 fetches the next element in a and b. Addiu $r7, $r7, #-1 is used for reducing the value of $r7. It is basically the count. J loop is unconditional jump. The program execution will jump to the beginning to statement tagged ‘loop’. Then loop continue to take place as long as the condition is met.

![image](https://user-images.githubusercontent.com/89673773/179662356-ca17e37f-e30b-43b8-8a82-c5d646a8c16c.png)


