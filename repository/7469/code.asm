section .data
    prompt: db "Enter a string: "
    prompt_len: equ $-prompt
    newline: db 10
    newline_len: equ $-newline
    input: times 256 db 0
    input_len: equ $-input

section .text
    global _start

_start:
    ; Display prompt
    mov eax, 4
    mov ebx, 1
    mov ecx, prompt
    mov edx, prompt_len
    int 0x80

    ; Read input from user
    mov eax, 3
    mov ebx, 0
    mov ecx, input
    mov edx, input_len
    int 0x80

    ; Calculate string length
    xor esi, esi ; Index variable
    mov al, byte [input+esi]
    cmp al, 0
    je print_newline
    inc esi
    loop:
        mov al, byte [input+esi]
        cmp al, 0
        je reverse
        inc esi
        jmp loop

    ; Reverse the string
    reverse:
        dec esi ; Go back one character
        xor edi, edi ; Index variable for reverse string
        mov bl, byte [input+esi]
        cmp bl, 0
        je print_newline
        loop2:
            mov byte [input+edi], bl
            dec esi
            inc edi
            mov bl, byte [input+esi]
            cmp bl, 0
            jne loop2

    ; Print reversed string
    print_newline:
        mov eax, 4
        mov ebx, 1
        mov ecx, newline
        mov edx, newline_len
        int 0x80

        mov eax, 4
        mov ebx, 1
        mov ecx, input
        mov edx, edi ; Length of reversed string
        int 0x80

    ; Exit
    mov eax, 1
    xor ebx, ebx
    int 0x80
