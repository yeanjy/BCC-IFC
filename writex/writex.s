.code16 			    
.text 				    

.globl _start
_start:				
  movb $'x' , %al	

  movb $0x0e, %ah		

  #Funcao print?
  int  $0x10		     

loop_final:

  hlt
  
  jmp loop_final



# Termina o bootloader com 0x55AA no final
. = _start + 510	  

.byte 0x55		        
.byte 0xaa		        
