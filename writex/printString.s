.code16 			    
.text 				    

.globl _start

_start:				
  movw $string, %si
  jmp invert_string

print_loop:
  movb $0x0e, %ah		
  movb (%si), %al
  int $0x10
  incw %si
  cmp $0, (%si)
  jne print_loop
  ret

string_length:
  xor %cx, %cx
string_length_loop:
  cmp $0, (%si)
  je loop_final 
  inc %cx
  incw %si
  jmp string_length_loop

invert_string:


loop_final:

  hlt
  
  jmp loop_final

. = _start + 256
string: 
  .asciz "Hello, World!"
counter:
  .byte 0

# Termina o bootloader com 0x55AA no final
. = _start + 510	  

.byte 0x55		        
.byte 0xaa		        
