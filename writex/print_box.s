.code16 			    
.text 				    

.globl _start
_start:				
  movb $'x' , %al	
  movb $0x0e, %ah		

  movb $80, %bl
  movb $22, %cl

  #Funcao print?
  int $0x10		     

print_loop:
  int $0x10
  dec %bl 
  jnz print_loop

jmp_print_space:
  movb $78, %bl

print_space:
  movb $' ', %al
  int $0x10		     
  dec %bl 
  jnz print_space
  movb $'x', %al
  int $0x10		     
  int $0x10		     

loop_print_space:
  dec %cl
  jnz jmp_print_space

jmp_print_loop:
  movb $79, %bl
  movb $'x' , %al

print_loop_final:
  int $0x10
  dec %bl 
  jnz print_loop_final

loop_final:

  hlt
  
  jmp loop_final

# Termina o bootloader com 0x55AA no final
. = _start + 510	  

.byte 0x55		        
.byte 0xaa		        
