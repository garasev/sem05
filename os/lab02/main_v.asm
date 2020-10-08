.386P 				
descr	struc					
	limit	dw	0			
	base_l	dw	0			
	base_m	db	0			
	attr_1	db	0			
	attr_2	db	0			
	base_h	db	0			
descr	ends					

data	segment	use16				
	gdt_null descr<>			
	gdt_data descr<data_size-1,,,92h>	
	gdt_code descr<code_size-1,,,98h>	
	gdt_stack descr<255,,,92h>		
	gdt_screen descr<4095,8000h,0Bh,92h>	;
	gdt_data32 descr<0FFFFh,,,92h,0CFh>
gdt_size=$-gdt_null				

	pdescr	df	0			
	msg_rm	db	'Real mode     '
msg_rm_len=$-msg_rm
	msg_pm	db	'Protected mode'
msg_pm_len=$-msg_pm
data_size=$-gdt_null				
data	ends					

print	macro	msg,msg_len,row,col,color
	local	screen
	mov	di,row*160 + col*2
	mov	bx,offset msg
	mov	cx,msg_len
	mov	ah,color
	
screen:	mov	al,byte ptr [bx]
	inc	bx
	stosw
	loop	screen
endm

text	segment	'code' use16			
	assume	cs:text,ds:data			
main	proc					
	mov	ax,data
	mov	ds,ax
	mov	ax,0B800h
	mov	es,ax

	print	msg_rm,msg_rm_len,4,60,0Fh

	xor	eax,eax				
	mov	ax,data				
	mov	ds,ax				

	shl	eax,4				
	mov	ebp,eax				
	mov	bx,offset gdt_data; 
	mov	[bx].base_l,ax			
	rol	eax,16				
	mov	[bx].base_m,al			

	xor	eax,eax				
	mov	ax,cs				
	shl	eax,4				
	mov	bx,offset gdt_code
	mov	[bx].base_l,ax			
	rol	eax,16				
	mov	[bx].base_m,al			

	xor	eax,eax				
	mov	ax,ss				
	shl	eax,4				
	mov	bx,offset gdt_stack		
	mov	[bx].base_l,ax			
	rol	eax,16				
	mov	[bx].base_m,al			

	mov	dword ptr pdescr+2,ebp		
	mov	word ptr pdescr,gdt_size-1	
	lgdt	pdescr				
	

	cli					
	mov	al,80h				
	out	70h,al				
	mov	eax,cr0				
	or	eax,1				
	mov	cr0,eax				

	db	0EAh				
	dw	offset continue			
	dw	16				
continue:					
	mov	ax,8				
	mov	ds,ax				

	mov	ax,24				
	mov	ss,ax				

	mov	ax,32				
	mov	es,ax				

	mov	ax,40
	mov	gs,ax

	print	msg_pm,msg_pm_len,5,60,0Fh


	mov	gdt_data.limit,0FFFFh		
	mov	gdt_code.limit,0FFFFh		
	mov	gdt_stack.limit,0FFFFh		
	mov	gdt_screen.limit,0FFFFh		
	mov	ax,8				
	mov	ds,ax				
	mov	ax,24				
	mov	ss,ax				
	mov	ax,32				
	mov	es,ax				

	db	0EAh				
	dw	offset go			
	dw	16				

go:	mov	eax,cr0				
	and	eax,0FFFFFFFEh			
	mov	cr0,eax				
	db	0EAh				
	dw	offset return			
	dw	text				

return:	mov	ax,data				
	mov	ds,ax				
	mov	ax,stk				
	mov	ss,ax				
	sti					
	mov	al,0				
	out	70h,al				

	print	msg_rm,msg_rm_len,6,60,0Fh

	mov	ax,4C00h			
	int	21h				
main	endp					
code_size=$-main				
text	ends					

stk	segment	stack 'stack'			
	db	256 dup('^')			
stk	ends					
	end	main				
