.386p

far_jump macro label, segment ;(сегмент смещение)
    db	0EAh 
    dd	offset label
    dw	segment
endm

print_str macro str ; вывод строки на экран
    mov ah, 09h
    lea dx, str
    int 21h
endm

wait_key macro ; ожидание ввода символа с клавиатуры
    push eax
    mov ah, 10h
    int 16h
    pop eax
endm

set_interrupt_base macro base
;чтобы начать инициализицию пик, нужно на порт команды 20h отправить команду 11h (заставляет контроллер ждать слова инициализации)
            mov	al, 11h						; команда - инициализировать ведущий контроллер
            out	20h, al						; отправить команду по шине данных ведущему контроллеру
			
			;отправляем новой базовый линейный адрес
            mov	al, 32						; базовый вектор (начальное смещение для обработчика) установить в 32
            out	21h, al						; отправить базовый вектор ведущему контроллеру

            mov	al, 4						; 4 = 0000 0100 
            out	21h, al                     ; сообщить mask_master PIC, что mask_slave подключён к IRQ2

            mov	al, 1						; указываем, что нужно будет посылать
            out	21h, al                     ; команду завершения обработчика прерывания
endm

clear_screen macro ; очистить экран
    mov	ax, 3
    int	10h
endm

load_gdt macro gdt_desc
    shl eax, 4                        ; eax - линейный базовый адрес (*2^4 = 16) (в eax был seg => он выравнен по параграфу => линейный адрес seg * 16)
    mov word ptr gdt_desc.base_l, ax  ; загрузка младшей часть базы
    shr eax, 16                       ; старшую половину eax в ax
    mov byte ptr gdt_desc.base_m, al  ; загрузка средней часть базы
    mov byte ptr gdt_desc.base_h, ah  ; загрузка старшей часть базы
endm

load_gdtr macro reg                 ; в reg полный линейный адрес GDT
    mov	dword ptr gdtr + 2, reg	    ; кладём полный линейный адрес в старшие 4 байта переменной gdtr
    mov word ptr  gdtr, gdt_size-1	; в младшие 2 байта заносим размер gdt, из-за определения gdt_size (через $) настоящий размер на 1 байт меньше
    lgdt fword ptr gdtr 		    ; загрузим GDT
endm

load_idt macro idt_desc
    mov	idt_desc.offs_l, ax ; загрузить младшую часть смещения
    shr	eax, 16             ; переместить старшую часть в младшую
    mov	idt_desc.offs_h, ax ; загрузить старшую часть смещения
endm

init_idtr macro reg                 ; в reg полный линейный адрес GDT
    mov	 dword ptr idtr + 2, reg	; загрузить полный линейный адрес в старшие 4 байта переменной idtr
    mov  word ptr  idtr, idt_size-1	; в младшие 2 байта заносим размер idt
endm


memory_string macro 
    mov dI, 100
    mov ah, 0Fh
    mov al, 'M'
    stosw
    mov al, 'e'
    stosw
    mov al, 'm'
    stosw
    mov al, 'o'
    stosw
    mov al, 'r'
    stosw
    mov al, 'y'
    stosw
    mov al, ':'
    stosw                 
endm

timer_string macro 
    mov dI, 400
    mov ah, 0Fh
    mov al, 'T'
    stosw
    mov al, 'i'
    stosw
    mov al, 'm'
    stosw
    mov al, 'e'
    stosw
    mov al, 'r'
    stosw
    mov al, ':'
    stosw                 
endm

pm_string macro 
    mov dI, 0
    mov ah, 0Fh
    mov al, 'P'
    stosw
    mov al, 'r'
    stosw
    mov al, 'o'
    stosw
    mov al, 'c'
    stosw
    mov al, 'e'
    stosw
    mov al, 's'
	stosw
	mov al, 's'
    stosw
    mov al, 'o'
    stosw
    mov al, 'r'
    stosw
    mov al, ' '
    stosw
    mov al, 'w'
    stosw
    mov al, 'o'
    stosw
    mov al, 'r'
	stosw
	mov al, 'k'
    stosw
    mov al, ' '
    stosw
    mov al, 'i'
    stosw
    mov al, 'n'
    stosw
    mov al, ' '
    stosw
	mov al, 'p'
    stosw
    mov al, 'r'
    stosw
    mov al, 'o'
    stosw
    mov al, 't'
    stosw
    mov al, 'e'
    stosw
    mov al, 'c'
    stosw
    mov al, 't'
	stosw
	mov al, 'e'
    stosw
    mov al, 'd'
    stosw
    mov al, ' '
    stosw
    mov al, 'm'
	stosw
    mov al, 'o'
    stosw   
	mov al, 'd'
	stosw
    mov al, 'e'
    stosw  
endm
; СТРУКТУРА ДЕСКРИПТОРА СЕГМЕНТА В ТАБЛИЦЕ ГЛОБАЛЬНЫХ ДЕСКРИПТОРОВ GDT
seg_descr struc    
    lim 	dw 0	; Граница (биты 0..15)  - размер сегмента в байтах
    base_l 	dw 0	; Младшие 16 битов адресной базы - базовый адрес задаётся в виртуальном адресном пространстве
    base_m 	db 0	; Следующие 8 битов адресной базы.
    attr_1	db 0	; атрибуты
    attr_2	db 0	; атрибуты
    base_h 	db 0	; Последние 8 битов адресной базы.
seg_descr ends

; Дескриптор прерываний(находится в IDT)
int_descr struc 
    offs_l 	dw 0  ; Младшие 16 битов адреса, куда происходит переход в случае возникновения прерывания.
    sel		dw 0  ; Селектор сегмента с кодом прерывания/Переключатель сегмента ядра
    cntr    db 0  ; Счётчик, не используется в данной программе. 
    attr	db 0  ; Атрибуты
    offs_h 	dw 0  ; Старшие 16 битов адреса, куда происходит переход.
int_descr ends

; сегмент стека
stack_seg segment  para stack 'STACK'
    stack_start	db	100h dup(?)
    stack_size = $-stack_start
stack_seg 	ENDS

; 32х разрядный сегмент данных 
data_seg segment para 'DATA'

    ;ГЛОБАЛЬНАЯ ТАБЛИЦА ДЕСКРИПТОРОВ СЕГМЕНТОВ

    ; обязательный нулевой дескриптор 
    gdt_null  seg_descr <>
    
    ; 16-битный сегмент кода - для реального режима
    gdt_CS_16bit seg_descr <rm_code_size-1, 0, 0, 10011000b, 00000000b, 0>

	; сегмент кода
    gdt_DS_flat seg_descr <0FFFFh, 0, 0, 10010010b, 11001111b, 0>  

    ; 32-битный сегмент кода - для защищенного режима
    gdt_CS_32bit seg_descr <pm_code_size-1, 0, 0, 10011000b, 01000000b, 0>

    ; 32-битный сегмент данных - для защищенного режима
    gdt_DS_32bit seg_descr <data_size-1, 0, 0, 10010010b, 01000000b, 0>

    ; 32-битный сегмент стека - для защищенного режима 
    gdt_SS_32bit seg_descr <stack_size-1, 0, 0, 10010110b, 01000000b, 0>
        
    ; 32-битный сегмент видеопамяти == сегмент данных видеобуфера
    gdt_VB_32bit seg_descr <3999, 8000h, 0Bh, 10010010b, 01000000b, 0>

    gdt_size = $-gdt_null ; размер таблицы  GDT 
    gdtr	df 0	      ; тут будет храниться базовый линейный адрес и размер таблицы GDT

    ; смещения дескрипторов сегментов в таблице
    ; GDT - размер дескриптора 8 байт
    sel_CS_16bit    equ    8   
    sel_DS_16bit    equ   16   
    sel_CS_32bit    equ   24
    sel_DS_32bit    equ   32
    sel_SS_32bit    equ   40
    sel_videobuffer equ   48
	
    ; ТАБЛИЦА ДЕСКРИПТОРОВ ПРЕРЫВАНИЙ 
    
    IDT	label byte ;метка (для получения размера IDT) говорит что это начало таблицы

    ; первые 32 дескриптора - исключения, в программе не используются
	trap1 int_descr 12 dup (<0, sel_CS_32bit, 0, 10001111b, 0>) 
	trap13 int_descr <0, sel_CS_32bit, 0, 10001111b, 0>
	trap2 int_descr 19 dup (<0, sel_CS_32bit, 0, 10001111b, 0>) 

    ; дескриптор прерывания от таймера
    int08 int_descr <0, sel_CS_32bit, 0, 10001110b, 0>  ; аппаратное прерывание

    ; дескриптор прерывания от клавиатуры
    int09 int_descr	<0, sel_CS_32bit, 0, 10001110b, 0> 

    idt_size = $-IDT ; размер таблицы IDT

    idtr df 0                       ; будет хранить базовый линейный адрес (4 байта) таблицы IDT и ее размер (2 байта)
    idtr_backup dw	3FFh, 0, 0      ; чтобы запомнить предыдущее значение и восстановить его при переходе обратно в реальный режим 3FF - первый килобайт, лимит - 1кб, линейный базовый адрес 0.

    mask_master	db 0		; маска прерывания ведущего контроллера
    mask_slave	db 0		; маска прерывания ведомого контроллера

	; Номер скан кода (с клавиатры) символа ASCII == номеру соответствующего элемента в таблице:
	ascii	db 0, 0, 49, 50, 51, 52, 53, 54, 55, 56, 57, 48, 45, 61, 0, 0
			db 81, 87, 69, 82, 84, 89, 85, 73, 79, 80, 91, 93, 0, 0, 65, 83
			db 68, 70, 71, 72, 74, 75, 76, 59, 39, 96, 0, 92, 90, 88, 67
			db 86, 66, 78, 77, 44, 46, 47
			
    enter_pressed	    db 0				 
    cnt_time	        dd 0		    ; счетчик тиков таймера
    symbol_position     dd 650         ; Позиция выводимого символа

    msg_in_rm   db 'In real mode. $'
    msg_move_pm db 'To enter Protected Mode press any key!$'
    msg_out_pm  db 'Returned to Real Mode!$'

    data_size = $-gdt_null ; размер сегмента данных
data_seg ends


PM_code_seg segment para public 'CODE' use32

    assume cs:PM_code_seg, ds:data_seg, ss:stack_seg

    pm_start:
		; в сегментные регистры загружаем селекторы
            mov	ax, sel_DS_32bit 
            mov	ds, ax
            mov	ax, sel_videobuffer
            mov	es, ax
            mov	ax, sel_SS_32bit
            mov	ss, ax
            mov	eax, stack_size
            mov	esp, eax

        sti ; разрешить прерывания, запрещенные в реальном режиме
            ; выход из цикла - по нажатию Enter

        ; вывод строк - сохранение символов в видеопамять
        pm_string
        memory_string
		timer_string

        ; подсчет и вывод объема доступной памяти
        call countAvailableMemory


        ; Возвращение в реальный режим происходит по нажатию
        ; клавиши 'enter' - это будет обработано в коде обработчика прервания 
        ; чтобы программа не завершалась до этого момента, нужен бескончный цикл
    inf_proc:
        test enter_pressed, 1
        jz	inf_proc

        ; запрещаем прерывания
        ; немаскируемые уже запрещены
        cli ; сброс флага прерывания IF = 0
        far_jump return_rm, sel_CS_16bit
    
		simple proc
			iret
		simple endp
	
		exc13 proc
			pop eax
			iret
		exc13 endp
		;обработчик системного таймера
        int08_handler proc uses eax 

                ; получили текущее количество тиков
                mov  eax, cnt_time

                ; вывели время
                call print_time

                ; увеличили текущее количество счетчиков
                inc eax

                ; сохранили 
                mov cnt_time, eax

                ; отправили EOI ведущему контроллеру прерываний
                mov	al, 20h 
                out	20h, al
                
                iretd
        int08_handler endp

        int09_handler proc uses eax ebx edx 
            in	al, 60h      ; Получить скан-код нажатой клавиши из порта клавиатуры

            cmp	al, 1Ch 	        ; Сравниваем с кодом enter
            jne	print_value         ; Если не enter - выведем, то что ввели
            or enter_pressed, 1     ; Если enter - устанавливаем флаг, возврата в реальный режим
            jmp allow_handle_keyboard 
            
            print_value:
                cmp al, 80h  ; Сравним какой скан-код пришел: нажатой клавиши или отжатой?
                ja allow_handle_keyboard 	 ; Если отжатой, то ничего не выводим
                                
                xor ah, ah	 ; Если нажатой, то выведем на экран
                
                xor ebx, ebx
                mov bx, ax
                

                mov dl, ascii[ebx]   ; Получим ASCII код нажатой клавиши по скан коду из таблицы
                mov ebx, symbol_position   ; Текущая позиция вывода символа
                mov es:[ebx], dl

                add ebx, 2          ; Увеличим текущую позицию вывода текста
                mov symbol_position, ebx

            allow_handle_keyboard: 
                in	al, 61h ; сообщаем контроллеру о приёме скан кода:
                or	al, 80h ; установкой старшего бита 
                out	61h, al ; содержимого порта B
                and al, 7Fh ; и последующим его сбросом
                out	61h, al

                mov	al, 20h ; End of Interrupt ведущему контроллеру прерываний
                out	20h, al

                iretd
        int09_handler endp
		;подсчёт памяти
		;первый мегабайт пропускаем, начиная со второго мегабайта сохраняем байт или слово памяти, сохраняем туда сигнатуру
		;прочитаем сигнатуру и сравниваем с сигнатурой в программе, если сигнатуры совпали, то это память

        countAvailableMemory proc uses ds eax ebx
            mov ax, sel_DS_16bit
            mov ds, ax
            
            mov ebx, 100001h ; пропустить первый мегабайт (потому что данные BIOS readonly, а мы попытаемся изменить их)
            mov dl, 10101010b ; пишем сигнатуру
            
            mov	ecx, 0FFEFFFFEh; количество оставшейся памяти (до превышения лимита в 4ГБ) - защита от переполнения

            iterate_through_memory:
                mov dh, ds:[ebx] ; сохраняем байт памяти

                mov ds:[ebx], dl        ; пишем в память
                cmp ds:[ebx], dl        ; проверяем - если записано то, что мы пытались записать
                                                ; то это доступная память
                jnz print_memory_counter        ; иначе мы дошли до конца паямти - надо вывести
            
                mov	ds:[ebx], dh ; восстановить байт памяти
                inc ebx          ; если удалось записать - увеличиваем счетчик памяти 
            loop iterate_through_memory

            print_memory_counter:
                mov eax, ebx ; переводим в Mb
                xor edx, edx

                mov ebx, 100000h ; 1 Mb
                div ebx

                mov ebx, 120
                call print_eax

            ret
        countAvailableMemory endp


        ; вывод значения eax в видеобуффер
        ; в ebx позиция вывода на экран 
        print_eax proc uses ecx ebx edx     
                add ebx, 10h 
                mov ecx, 8   
            
            print_symbol: 
                mov dl, al
                and dl, 0Fh      
                
                cmp dl, 10
                jl add_zero_sym
                add dl, 'A' - '0' - 10 

            add_zero_sym:
                add dl, '0'
                
                mov es:[ebx], dl ; записать в видеобуффер
                ror eax, 4       ; циклически сдвинуть вправо (FEDC) -> (CFED) -> (DCFE) -> (EDCF) -> (FEDC)
                sub ebx, 2       ; печатаем след символ
                loop print_symbol
            ret
        print_eax endp


        print_dl proc uses eax ebx ecx edx; al < 100
            mov al, dl
            xor ecx, ecx

            add ebx, 4
            mov cl, 2

            mov dl, 10
            print_al:
                xor ah, ah
                div dl
                add ah, '0'
                mov es:[ebx], ah ; записать в видеобуффер остаток
                sub ebx, 2
                loop print_al
            ret
        print_dl endp

        print_time proc uses eax ebx ecx edx ; в eax кол-во тиков с полуночи
            mov ecx, 65536
            xor edx, edx
            mul ecx
            mov ecx, 1193180
            div ecx  ;перевод из количества тиков в количество секунд(18.2)
            
            xor edx, edx
            mov ecx, 60
            div ecx
            
            mov ebx, 450
            call print_dl

            mov dh, ':'
            mov es:[ebx], dh
            sub ebx, 6
            
            xor edx, edx
            div ecx
            call print_dl

            mov dh, ':'
            mov es:[ebx], dh
            sub ebx, 6
            xor dh, dh
            
            mov dl, al
            call print_dl

            ret
        print_time endp

    pm_code_size = $-pm_start 	
PM_code_seg ends

RM_code_seg segment para public 'CODE' use16
    assume cs:RM_code_seg, ds:data_seg, ss: stack_seg

    start:
        mov ax, data_seg
        mov ds, ax

        mov ax, PM_code_seg
        mov es, ax

        print_str msg_in_rm  
        print_str msg_move_pm

        wait_key
        clear_screen 

		;Заполняем gdt
        xor	eax, eax
		
		;загружаем базовые линейные адреса в дескрипторы соответствующих сегментов
        mov	ax, RM_code_seg 
        load_gdt gdt_CS_16bit

        mov ax, PM_code_seg
        load_gdt gdt_CS_32bit

        mov ax, data_seg
        load_gdt gdt_DS_32bit

        mov ax, stack_seg
        load_gdt gdt_SS_32bit

        mov ax, data_seg  
        shl eax, 4  ;линейный базовый адрес сегмента data_seg

        add	eax, offset gdt_null ;в eax линейный базовый адрес gdt
        load_gdtr eax
		
			lea eax, es:simple
            load_idt trap1
			
			lea eax, es:simple
            load_idt trap2
			
			lea eax, es:exc13
            load_idt trap13;

            lea eax, es:int08_handler  ; в eax смиещение 8 обработчика относительно 32-разрядного сегмента кода
            load_idt int08 ; прерывание таймера

            lea eax, es:int09_handler
            load_idt int09; прерывание клавиатуры
            
            mov ax, data_seg
            shl eax, 4
            add	eax, offset IDT; в eax полный линейный адрес IDT
            init_idtr eax

            in	al, 21h						; получить набор масок (флагов) mask_master  (маски пика) 21h - порт данных мастера
            mov	mask_master, al					; сохраняем в переменной mask_master (понадобится для возвращения в RM)
            in	al, 0A1h					; аналогично ведомого  A1h - порт данных slave
            mov	mask_slave, al
			
			set_interrupt_base 32ё

            ; Запретим все прерывания в ведущем контроллере, кроме IRQ0 (таймер) и IRQ1(клавиатура)
            mov	al, 0FCh
            out	21h, al

            ; запретим все прерывания в ведомом контроллере
            mov	al, 0FFh
            out	0A1h, al

            lidt fword ptr idtr             
			
			; открываем линию А20 
            mov al, 0D1h ; команда управления
			out 64h, al ; линией А20
			mov al, 0DFh ; код открытия линии А20
			out 60h, al

            cli         ; отключить маскируемые прерывания
            in	al, 70h ; и немаскируемые прерывания получить адрес EFLAGS
            or	al, 80h ;
            out	70h, al

            push ds
                mov	ax, 40h
                mov	ds, ax
                mov eax, dword ptr ds:[6Ch] ; счётчик реального времени bios
            pop ds
            mov dword ptr cnt_time, eax
			
			;ПЕРЕХОД В ЗАЩИЩЁННЫЙ 
            mov	eax, cr0
            or eax, 1     ; перейти в непосредственно защищенный режим
            mov	cr0, eax

            db	66h ; far jmp sel_CS_32bit:pm_start ?
            far_jump pm_start, sel_CS_32bit


    return_rm:
	
			; закрыть линию А20(Рудаков стр 305)
			mov al, 0D1h ; команда управления линией А20
			out 64h, al
			mov al, 0DDh ; команда закрытия
			out 60h, al ; в порт контроллера интерфейса PS/2
			
			;ПЕРЕХОД в реальный режим
            mov	eax, cr0
            and	al, 0FEh 				; сбрасываем флаг защищенного режима
            mov	cr0, eax

            ; этот дальний переход необходим для модификации теневого регистра cs
            db	0EAh	; far jmp RM_code_seg:$+4
            dw	$+4	    ; *выполнить следующую после dw	RM_code_seg команду
            dw	RM_code_seg

            mov	eax, data_seg	; загружаем в сегментные регистры "нормальные" (реальные) сегменты
            mov	ds, ax          ; это позволит загрузить их в теневые регистры
            mov eax, PM_code_seg
            mov	es, ax
            mov	ax, stack_seg
            mov	ss, ax
            mov	ax, stack_size
            mov	sp, ax

            set_interrupt_base 8
            out	21h, al

            mov	al, mask_master ; восстанавить маски контроллеров прерываний
            out	21h, al
            mov	al, mask_slave
            out	0A1h, al

            ; загружаем таблицу дескриптров прерываний реального режима
            lidt	fword ptr idtr_backup

            in	al, 70h ; разрешить немаскируемые прерывания
            and	al, 7FH
            out	70h, al
            sti     ; и маскируемые

        clear_screen
        print_str msg_out_pm
        
        mov	ax, 4C00h
        int	21h

    rm_code_size = $-start 	; длина сегмента RM_code_seg
RM_code_seg	ends
end start