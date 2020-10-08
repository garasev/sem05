.586P	;(1) Разрешение трансляции всех команд Pentium
;	Структура для описания дескрипторов сегментов
descr struc		
lim dw 0	
base_l dw 0
base_m db 0
attr_1 db 0
attr_2 db 0
base_h db 0	
descr ends

;	Сегмент данных
data	segment use16
gdt_null descr <0, 0, 0, 0, 0, 0>
gdt_data descr <data_size - 1, 0, 0, 92h, 0, 0>
gdt_code descr <code_size - 1, 0, 0, 98h, 0, 0>
gdt_stack descr <255, 0, 0, 92h, 0, 0>
gdt_screen descr <3999, 8000h, 0Bh, 92h, 0, 0> 
gdt_size=$-gdt_null 

pdescr	df 0			
sym 	db 1			
attr 	db 1Eh			
msg	db 27, '[31:42m Back to real!	', 27, '[0m$'
data_size=$-gdt_null 	
data ends;

;	Сегмент команд
text	segment use16	
		assume CS:text, DS:data
main	proc
		xor EAX, EAX	
		mov AX, data	
		mov DS, AX
; Вычисление 32-битный линейный адрес сегмента данных и
; его загрузка в дескриптор сегмента данных в таблице
; глобальных дескрипторов GDT
		shl	EAX, 4	
		mov	EBP, EAX 	
		mov BX,	offset gdt_data
		mov [BX].base_l, AX
		shr EAX, 16
		mov [BX].base_m, AL
; Вычисление и загрузка в GDT линейный адрес сегмента кода
		xor EAX, EAX
		mov AX, CS
		shl EAX, 4
		mov BX, offset gdt_code
		shr EAX, 16
		mov [BX].base_m, AL
; Вычисление и загрузка в GDT линейный адрес сегмента стека
		xor EAX, EAX
		mov AX, SS
		shl EAX, 4
		mov BX, offset gdt_stack
		shr EAX, 16
		mov [BX].base_m, AL
; Подготовка псевдодескриптора pdescr и загрузка GDTR
		mov dword ptr pdescr + 2, EBP
		mov word ptr pdescr, gdt_size - 1
		lgdt pdescr
; Подготовка к возврату из защищённого режима в реальный
		mov AX, 40h
		mov ES, AX
		mov word ptr ES:[67h], offset return
		mov ES:[69h], CS
		mov AL, 0Fh
		out 70h, AL
		mov AL, 0Ah
		out 71h, AL
		cli
; Переход в защищённый режим
		mov EAX, CR0
		or EAX, 1
		mov CR0, EAX
;
		db 0EAh
		dw offset continue
		dw 16
continue:
		mov AX, 8
		mov DS, AX
; Разрешение адресации стека
		mov AX, 24
		mov SS, AX
; Инициализация ES
		mov AX, 32
		mov ES, AX
; Вывод на экране тестовой символьной строки
		mov DI, 1920
		mov CX, 80
		mov AX, word ptr sym
scrn:	stosw
		inc AL
		loop scrn
; Возвращение в реальный режим
		mov AL, 0FEh;
		out 64h, AL
		hlt
return:
; Восстановление вычислительной среды реального режима
		mov AX, data
		mov DS, AX
		mov AX, stk
		mov SS, AX
		mov SP, 256
		sti
; Работа в DOS
		mov AH, 09h
		mov DX, offset msg;
		int 21h
		mov AX, 4C00h
		int 21h
main 	endp
code_size=$-main
text 	ends

; Сегмент стека
stk 	segment stack use16;
		db 256 dup ('^');
stk 	ends
		end main
