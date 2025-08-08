.globl _start
_start:                          # Ponto de entrada principal.

    # Exibe um caractere na tela usando INT 0x10
    movb $'x', %al               # Carrega o caractere 'x' no registrador AL.
    movb $0x0e, %ah              # Configura para o serviço de impressão do BIOS (INT 0x10).
    int  $0x10                   # Chama a interrupção do BIOS para exibir o caractere.

# Some dois números de 16 bits e armazene o resultado em um terceiro.
1:
    movw $0x1234, %ax            # Carrega o número 0x1234 no registrador AX.
    movw $0x5678, %bx            # Carrega o número 0x5678 no registrador BX.
    addw %bx, %ax                # Soma BX a AX.
    movw %ax, %cx                # Armazena o resultado da soma em CX.

# Multiplique dois números de 8 bits e armazene o resultado em um registrador de 16 bits.
2:
    movb $0x12, %al              # Carrega o número 0x12 no registrador AL.
    movb $0x34, %bl              # Carrega o número 0x34 no registrador BL.
    mulb %bl                     # Multiplica AL por BL. O resultado é armazenado em AX.
    movw %ax, %dx                # Move o resultado de AX para DX.

# Divida um número de 16 bits por outro de 8 bits.
3:
    movw $0x1234, %ax            # Carrega o dividendo no registrador AX.
    movb $0x12, %bl              # Carrega o divisor no registrador BL.
    divb %bl                     # Divide AX por BL. O quociente vai para AL, e o resto para AH.
    movw %ax, %si                # Armazena o resultado (quociente e resto) em SI.

# Realize operações lógicas (AND, OR, NOT, XOR) entre dois registradores.
4:
    movb $0x12, %al              # Carrega o número 0x12 em AL.
    movb $0x34, %bl              # Carrega o número 0x34 em BL.
    andb %bl, %al                # Faz AND entre AL e BL.
    orb %bl, %al                 # Faz OR entre AL e BL.
    notb %al                     # Faz NOT em AL.
    xorb %bl, %al                # Faz XOR entre AL e BL.

# Leia um valor de uma posição de memória e armazene em um registrador.
5:
    movw $array, %si             # Define o endereço base do array em SI.
    movw (%si), %di              # Move o valor do primeiro elemento do array para DI.

# Escreva um valor em uma posição específica da memória.
6:
    movw $array, %si             # Define o endereço de destino como o início do array.
    movw $0x5678, %di            # Define o valor a ser escrito.
    movw %di, (%si)              # Escreve o valor de DI no endereço apontado por SI.

# Crie um array de números e calcule a soma de todos os elementos.
7:
    xorw %ax, %ax                # Zera o acumulador (AX).
    xorw %cx, %cx                # Zera o índice do array (CX).
    movw $array, %si             # Define o endereço base do array em SI.

loop_start:
    movw (%si), %dx              # Carrega o elemento atual do array para DX.
    addw %dx, %ax                # Soma o elemento ao acumulador (AX).
    addw $2, %si                 # Avança para o próximo elemento do array (2 bytes por elemento).
    incw %cx                     # Incrementa o contador de elementos.
    cmpw $array_size, %cx        # Compara o contador com o tamanho do array.
    jl loop_start                # Continua no loop se o contador for menor que o tamanho.

    movw %ax, result             # Armazena o resultado da soma em "result".

loop_end:
    hlt                          # Para o programa.

# Dados.
.data
array:      .word 1, 2, 3, 4, 5  # Array com números de 16 bits.
array_size: .equ 5               # Tamanho do array.
result:     .word 0              # Para armazenar o resultado da soma.
