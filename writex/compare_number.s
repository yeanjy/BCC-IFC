.code16
.text

.globl _start
_start:                
  movb $'x', %al           # Carrega o caractere 'x' em %al
  movb $0x0e, %ah          # Modo de escrita de caractere
  int $0x10                # Chama a interrupção para imprimir

. = _start + 400           # Define um espaço para variáveis

var1: .byte 0x01
var2: .byte 0x02
var3: .byte 0x03

compare1:
  movb var1, %bl          # Move var1 para %bl
  movb var2, %cl          # Move var2 para %cl
  cmp %cl, %bl            # Compara %bl (var1) com %cl (var2)
  jg compare2             # Se var1 > var2, vai para compare2
  movb %cl, %bl           # Caso contrário, %bl = var2

compare2:
  movb var3, %cl          # Move var3 para %cl
  cmp %cl, %bl            # Compara %bl com %cl (var3)
  jg print_number         # Se %bl > var3, vai para print_number
  movb %cl, %bl           # Caso contrário, %bl = var3

print_number:
  addb $'0', %bl          # Converte o número para ASCII (0-9)
  movb %bl, %al           # Carrega o caractere ASCII em %al
  movb $0x0e, %ah         # Prepara para imprimir
  int $0x10               # Imprime o número

loop_final:
  hlt                     # Hibernar até uma interrupção
  jmp loop_final         # Fica em loop

# Finaliza o bootloader com 0x55AA
. = _start + 510         
.byte 0x55                
.byte 0xaa               
