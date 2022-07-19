#GLOBAL PIPELINE_BUBBLE VARIABLE
PIPELINE_BUBBLE = 0
Reg_31 = ''
def DotProduct_10(Reg):
 Reg[1] = Reg[0] #addu $r1 $r0 $r0 ; result = 0
 print(Reg)
 print(PIPELINE_BUBBLE )
 return Reg
def done(Reg, Reg_31):
 global PIPELINE_BUBBLE
 if Reg_31: # JR $R31
 Reg_31 = Reg_31

 for idx, register in enumerate(Reg):
 message1 = f"R{str(idx)} = {str(register)}"
 print(message1)
 message2 = f"No. of stalls = {str(PIPELINE_BUBBLE)}"
 print(message2)
 return
def loop(Reg): #loop:
 global PIPELINE_BUBBLE
 while True:
 #CYCLE 2
 if Reg[7] != ' ': #FETCH beq $r7 $r0 done ; done looping?
 True

 #CYCLE 3
 if Reg[7] != ' ': #DECODE beq $r7 $r0 done ; done looping?
 if Reg[2]: # FETCH lw $r2 0($r3) ; load a elem
 True

 #CYCLE 4
 if Reg[7] == Reg[0]: # EXECUTE beq $r7 $r0 done ; done looping?
 print("Dot Product Calculation is Done")
 break;
 else:
 if Reg[2][Reg[3]] != '': # DECODE lw $r2 0($r3)
 if Reg[4]: # FETCH lw $r4 0($r5)
 True
 #CYCLE 5
 if Reg[2][Reg[3]]: # MEM lw $R2 0($R3)
 if len(Reg[4]) >= 0: # EXECUTE lw $R4 0($R5)
 if Reg[4][Reg[5]] != '':# DECODE MUL $R2 $R2 $R4 ;
 if Reg[2]: # FETCH addu $R1 $R1 $R2....
 True
